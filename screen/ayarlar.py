# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Ayarlar(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me

        self.setUI()

    def SetMe(self, me):
        self.me = me

    def setUI(self):
        QLineEdit(self)
