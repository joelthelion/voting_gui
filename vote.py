#!/usr/bin/env python2
# coding: utf-8

import sys
import re
from PyQt4 import QtCore, QtGui
from prenom import Ui_MainWindow


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
            old_sep,old_count=self.ballots[self.get_couple(ballot)]
            assert(old_sep==sep)
            self.ballots[self.get_couple(ballot)]=(winner,sep,other,old_count+count)
    def parse_ballot(self,string):
        count,rest=string.split(":")
        count=int(count)
        winner,sep,other = re.search("([^=^>]*)(=|>)(.*)",rest).groups()
        #We don't support multiple ballots
        assert(not re.search("([^=^>]*)(=|>)(.*)",other))
        return (winner,sep,other,count)
    def ballot_repr(self,ballot):
        winner,sep,other,count=ballot
        return repr(count)+":"+winner+sep+other
    def save(self):
        with open(self.filename,"w") as f:
            for ballot in self.ballots.values():
                f.write((self.ballot_repr(ballot)+"\n").encode("utf-8"))

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        prenoms=[unicode(x.strip(),"utf-8") for x in open("prenoms.txt")]
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
        p1,p2=self.combis.pop()
        self.ui.prenom1.setText(p1)
        self.ui.prenom2.setText(p2)
    def count_ballot_and_update(self,win):
        if win == 0:
            b=(unicode(self.ui.prenom1.text()),"=",unicode(self.ui.prenom2.text()),1)
        elif win==1:
            b=(unicode(self.ui.prenom1.text()),">",unicode(self.ui.prenom2.text()),1)
        elif win==2:
            b=(unicode(self.ui.prenom2.text()),">",unicode(self.ui.prenom1.text()),1)
        self.ballots.add(b)
        self.ballots.save()
        self.update()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

