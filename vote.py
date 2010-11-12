#!/usr/bin/env python2
# coding: utf-8

import sys
import re
from PyQt4 import QtCore, QtGui
from prenom import Ui_MainWindow


class Ballots:
    def __init__(self,filename):
        """open file and parse ballots"""
        #ballots[frozenset(p1,p2)]=(sep,count)
        ballots={}
    def is_in(self,ballot):
        return self.get_couple(ballot) in self.ballots.keys()
    def get_couple(self,ballot):
        winner,sep,other,count=ballot
        couple=frozenset((winner,other))
        return couple
    def add(self,ballot):
        winner,sep,other,count=ballot
        if not self.is_in(ballot):
            self.ballots[self.get_couple(ballot)]=(sep,count)
        else:
            old_sep,old_count=self.ballots[self.get_couple(ballot)]
            assert(old_sep==sep)
            self.ballots[self.get_couple(ballot)]=(sep,old_count+count)
    def parse_ballot(self,string):
        count,rest=string.split(":")
        count=int(count)
        winner,sep,other = re.search("([^=^>]*)(=|>)(.*)",rest).groups()
        #We don't support multiple ballots
        assert(not re.search("([^=^>]*)(=|>)(.*)",other))
        return (winner,sep,other,count)

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    prenoms=[x.strip() for x in open("prenoms.txt")]
    #print prenoms
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())

