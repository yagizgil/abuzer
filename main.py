# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys,os

import menu,screen
import statusbar as sb


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(400, 100, 1200, 800)
        
        self.setWindowTitle("Abuzer")
        self.setUI()
        
        self.mymenu.onoff.btn.mousePressEvent("None")
        
    def setUI(self):
        w = QWidget()
        w.setObjectName("wid")
        w.setStyleSheet("#wid {background: #f0f0f0;}")
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        self.mymenu = menu.Menu(self)
        h.addWidget(self.mymenu)
        
        self.myscreen = screen.Screen(self)
        h.addWidget(self.myscreen)
        
        v.addLayout(h)
        
        self.statusbar = sb.StatusBar(self)
        v.addWidget(self.statusbar)
        
        w.setLayout(v)
        self.setCentralWidget(w)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())