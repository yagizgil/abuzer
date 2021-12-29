# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StatusBar(QFrame):

    def __init__(self, me):
        super().__init__()
        self.me = me

        self.setStyleSheet(open("style/status.css", "r").read())
        
        self.setMaximumHeight(35)
        self.setUI()

    def setUI(self):
        me = self.me
        h = QHBoxLayout()
        
        h.addWidget(QLabel("Seçilen Proje: ....."))
        
        refresh = QPushButton()
        refresh.setObjectName("refresh")
        refresh.setFixedSize(40, 30)
        refresh.setIcon(QIcon("image/refresh.png"))
        refresh.setCursor(QCursor(Qt.PointingHandCursor))
        
        save = QPushButton()
        save.setObjectName("save")
        save.setFixedSize(40, 30)
        save.setIcon(QIcon("image/save.png"))
        save.setCursor(QCursor(Qt.PointingHandCursor))
        
        run = QPushButton()
        run.setObjectName("run")
        run.setFixedSize(40, 30)
        run.setIcon(QIcon("image/run.png"))
        run.setCursor(QCursor(Qt.PointingHandCursor))
        
        h.addStretch()
        h.addStretch()
        h.addWidget(refresh)
        h.addWidget(save)
        h.addWidget(run)
        
        self.setLayout(h)
        
        