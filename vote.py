#!/usr/bin/env python
# coding: utf-8

import sys
import re
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import Qt
from prenom import Ui_MainWindow
from results import Ui_results


class Ballots:
    def __init__(self,filename):
        """open file and parse ballots"""
        #ballots[frozenset(p1,p2)]=(winner,sep,other,count)
        self.ballots=[]
        self.has_ballots=set()
        self.filename=filename
        try:
            for l in open(filename):
                l.strip()
                self.add(self.parse_ballot(l))
        except IOError:
            print("Ballot file not found")
    def is_in(self,ballot):
        return self.get_couple(ballot) in self.has_ballots
    def get_couple(self,ballot):
        winner,sep,other,count=ballot
        winner,sep,other,count=ballot
        winner=winner.capitalize()
        other=other.capitalize()
        couple=frozenset((winner,other))
        return couple
    def add(self,ballot):
        winner,sep,other,count=ballot
        winner=winner.capitalize()
        other=other.capitalize()
        self.ballots.append((winner,sep,other,count))
        self.has_ballots.add(self.get_couple(self.ballots[-1]))
    def parse_ballot(self,string):
        #string=str(string)
        count,rest=string.split(":")
        count=int(count)
        winner,sep,other = re.search("([^=^>]*)(=|>)(.*)",rest).groups()
        #We don't support multiple ballots
        assert(not re.search("([^=^>]*)(=|>)(.*)",other))
        return (winner,sep,other,count)
    def ballot_repr(self,ballot):
        winner,sep,other,count=ballot
        return str(repr(count))+":"+winner+sep+other
    def save(self):
        with open(self.filename,"w") as f:
            for ballot in self.ballots:
                f.write(self.ballot_repr(ballot)+"\n")

class NumericalTableItem(QtGui.QTableWidgetItem):
    def __ge__(self,other):
        return float(self.text())>=float(other.text())
    def __lt__(self,other):
        return float(self.text())<float(other.text())

class ResultWindow(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui= Ui_results()
        self.ui.setupUi(self)
    def show_results(self,prenoms):
        import rpvote
        import glob
        ballots = []
        for f in glob.glob("ballots_*.txt"):
            b = Ballots(f)
            ballots.extend(b.ballots)
        contest = rpvote.Contest(prenoms)
        for winner,delim,loser,count in ballots:
            contest.addballot([[winner],[loser]])
        contest.computemargins()
        #contest.printmargins()

        outcome = contest.compute()
        #outcome.printout()
        #outcome.printresult()
        table=self.ui.table
        table.setRowCount(len(prenoms))
        for n,(rank,name,res) in enumerate(outcome.getresult()):
            table.setItem(n,0,NumericalTableItem(rank))
            table.setItem(n,1,NumericalTableItem(name))
            table.setItem(n,2,NumericalTableItem(str(res)))
        table.resizeColumnsToContents()
        self.exec_()

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.prenoms=[x.strip().capitalize() for x in open("prenoms.txt",encoding="utf-8")]

        # Get user name
        ok = False
        while not ok:
            login, ok = QtGui.QInputDialog.getText(self, 'Nom', 'Votre nom SVP:')

        self.ballots=Ballots("ballots_%s.txt"%login)
        self.combis=[]
        for n,p in enumerate(self.prenoms):
            for p2 in self.prenoms[n+1:]:
                self.combis.append((p,p2))
        import random
        random.shuffle(self.combis)

        # limit the number of votes to 50
        self.combis = self.combis[:50]

        QtCore.QObject.connect(self.ui.button1,QtCore.SIGNAL("clicked()"), self.callback_1)
        QtCore.QObject.connect(self.ui.button2,QtCore.SIGNAL("clicked()"), self.callback_2)
        QtCore.QObject.connect(self.ui.button_equal,QtCore.SIGNAL("clicked()"), self.callback_eq)
        QtCore.QObject.connect(self.ui.actionQuit,QtCore.SIGNAL("triggered()"), sys.exit)
        QtCore.QObject.connect(self.ui.actionResults,QtCore.SIGNAL("triggered()"), self.show_results)
        self.update()
        #print self.prenoms
    def callback_1(self):
        self.count_ballot_and_update(1)
    def callback_2(self):
        self.count_ballot_and_update(2)
    def callback_eq(self):
        self.count_ballot_and_update(0)
    def update(self):
        p1,p2=None,None
        while p1 is None or frozenset((p1,p2)) in self.ballots.has_ballots:
            if not self.combis:
                self.ui.button1.setEnabled(False)
                self.ui.button2.setEnabled(False)
                self.ui.button_equal.setEnabled(False)
                self.show_results()
                sys.exit(0)
            else:
                p1,p2=self.combis.pop()
        self.ui.prenom1.setText(p1)
        self.ui.prenom2.setText(p2)
    def show_results(self):
        self.show()
        res_win=ResultWindow()
        res_win.show_results(self.prenoms)
    def count_ballot_and_update(self,win):
        if win == 0:
            b=(str(self.ui.prenom1.text()),"=",str(self.ui.prenom2.text()),1)
        elif win==1:
            b=(str(self.ui.prenom1.text()),">",str(self.ui.prenom2.text()),1)
        elif win==2:
            b=(str(self.ui.prenom2.text()),">",str(self.ui.prenom1.text()),1)
        self.ballots.add(b)
        self.ballots.save()
        self.update()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

