#!/usr/bin/env python2
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
        self.ballots={}
        self.filename=filename
        try:
            for l in open(filename):
                l.strip()
                self.add(self.parse_ballot(l))
        except IOError:
            print "Ballot file not found"
    def is_in(self,ballot):
        return self.get_couple(ballot) in self.ballots.keys()
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
        if not self.is_in(ballot):
            self.ballots[self.get_couple(ballot)]=(winner,sep,other,count)
        else:
            d1,d2,old_sep,old_count=self.ballots[self.get_couple(ballot)]
            assert(old_sep==sep)
            self.ballots[self.get_couple(ballot)]=(winner,sep,other,old_count+count)
    def parse_ballot(self,string):
        string=unicode(string,"utf-8")
        count,rest=string.split(":")
        count=int(count)
        winner,sep,other = re.search("([^=^>]*)(=|>)(.*)",rest).groups()
        #We don't support multiple ballots
        assert(not re.search("([^=^>]*)(=|>)(.*)",other))
        return (winner,sep,other,count)
    def ballot_repr(self,ballot):
        winner,sep,other,count=ballot
        return unicode(repr(count))+u":"+winner+sep+other
    def save(self):
        with open(self.filename,"w") as f:
            for ballot in self.ballots.values():
                f.write((self.ballot_repr(ballot)+u"\n").encode("utf-8"))

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
    def show_results(self,ballots):
        counts={}
        for winner,delim,loser,count in ballots.values():
            if delim != ">" : continue
            else:
                counts[winner]=counts.get(winner,0)+1
                counts[loser]=counts.get(loser,0)-1
        #Make sure the lowest score is 0
        min_score=min(counts.values())
        for k in counts.keys():
            counts[k]+=abs(min_score)

        table=self.ui.table
        table.setRowCount(len(counts))
        for n,(key,value) in enumerate(counts.iteritems()):
            table.setItem(n,0,NumericalTableItem(key))
            table.setItem(n,1,NumericalTableItem(str(value)))
        table.sortItems(1,Qt.DescendingOrder)
        table.resizeColumnsToContents()
        self.setFixedSize(table.horizontalHeader().length() + 43, table.verticalHeader().length() + 88) 
        self.exec_()

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        prenoms=[unicode(x.strip(),"utf-8").capitalize() for x in open("prenoms.txt")]
        self.ballots=Ballots("ballots.txt")
        self.combis=[]
        for n,p in enumerate(prenoms):
            for p2 in prenoms[n+1:]:
                self.combis.append((p,p2))
        import random
        random.shuffle(self.combis)
        QtCore.QObject.connect(self.ui.button1,QtCore.SIGNAL("clicked()"), self.callback_1)
        QtCore.QObject.connect(self.ui.button2,QtCore.SIGNAL("clicked()"), self.callback_2)
        QtCore.QObject.connect(self.ui.button_equal,QtCore.SIGNAL("clicked()"), self.callback_eq)
        self.update()
        #print prenoms
    def callback_1(self):
        self.count_ballot_and_update(1)
    def callback_2(self):
        self.count_ballot_and_update(2)
    def callback_eq(self):
        self.count_ballot_and_update(0)
    def update(self):
        p1,p2=None,None
        while p1 is None or frozenset((p1,p2)) in self.ballots.ballots.keys():
            if not self.combis:
                self.ui.button1.setEnabled(False)
                self.ui.button2.setEnabled(False)
                self.ui.button_equal.setEnabled(False)
                self.show()
                res_win=ResultWindow()
                res_win.show_results(self.ballots.ballots)
                sys.exit(0)
            else:
                p1,p2=self.combis.pop()
        self.ui.prenom1.setText(p1)
        self.ui.prenom2.setText(p2)


    def count_ballot_and_update(self,win):
        if win == 0:
            b=(unicode(self.ui.prenom1.text()),u"=",unicode(self.ui.prenom2.text()),1)
        elif win==1:
            b=(unicode(self.ui.prenom1.text()),u">",unicode(self.ui.prenom2.text()),1)
        elif win==2:
            b=(unicode(self.ui.prenom2.text()),u">",unicode(self.ui.prenom1.text()),1)
        self.ballots.add(b)
        self.ballots.save()
        self.update()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

