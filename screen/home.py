# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Anasayfa(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me

        self.setUI()


    def setUI(self):
        v = QVBoxLayout()
        
        logo = Logo()
        
        h2 = QHBoxLayout()
        
        yeni = Yeni(self.me)
        dahil = DahilEt(self.me)
        
        h2.addStretch()
        h2.addStretch()
        h2.addWidget(yeni)
        h2.addStretch()
        h2.addWidget(dahil)
        h2.addStretch()
        h2.addStretch()
        
        
        
        h3 = QHBoxLayout()
        
        projeler = GroupAc(self.me)
        h3.addWidget(projeler)
        
        butonlar = Btns(projeler)
        
        v.addWidget(logo)
        v.addLayout(h2)
        v.addLayout(h3)
        v.addLayout(butonlar)
        
        self.setLayout(v)


class Logo(QFrame):
    
    def __init__(self):
        super().__init__()
        self.setMaximumHeight(120)
        
        logo = QLabel()
        self.pixmap = QPixmap("image/logo.png")
        self.pixmap = self.pixmap.scaled(QSize(400,95))
        logo.setPixmap(self.pixmap)
        logo.resize(400,95)
        
        v = QVBoxLayout()
        v.addWidget(logo)
        v.addStretch()
        v.addStretch()
        
        h1 = QHBoxLayout()
        h1.addStretch()
        h1.addLayout(v)
        h1.addStretch()
        
        self.setLayout(h1)

class Yeni(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.setObjectName("yeni")
        self.setStyleSheet(open("style/anasayfa.css").read())
        
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMaximumHeight(200)
        self.setMaximumWidth(210)
        self.setMinimumHeight(100)
        self.setMinimumWidth(160)
        
        v = QVBoxLayout()
        
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        
        logo = QLabel()
        self.pixmap = QPixmap("image/new3.png")
        self.pixmap = self.pixmap.scaled(QSize(70,70))
        logo.setPixmap(self.pixmap)
        logo.resize(70,70)
        
        metin = QLabel("Proje Oluştur")
        
        h1.addStretch()
        h1.addWidget(logo)
        h1.addStretch()
        
        h2.addStretch()
        h2.addWidget(metin)
        h2.addStretch()
        
        v.addLayout(h1)
        v.addLayout(h2)
        self.setLayout(v)
        
class DahilEt(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.setObjectName("dahil")
        self.setStyleSheet(open("style/anasayfa.css").read())
        
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setMaximumHeight(200)
        self.setMaximumWidth(210)
        self.setMinimumHeight(100)
        self.setMinimumWidth(160)
        
        v = QVBoxLayout()
        
        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        
        logo = QLabel()
        self.pixmap = QPixmap("image/import.png")
        self.pixmap = self.pixmap.scaled(QSize(70,70))
        logo.setPixmap(self.pixmap)
        logo.resize(70,70)
        
        metin = QLabel("Proje Dahil Et")
        
        h1.addStretch()
        h1.addWidget(logo)
        h1.addStretch()
        
        h2.addStretch()
        h2.addWidget(metin)
        h2.addStretch()
        
        v.addLayout(h1)
        v.addLayout(h2)
        self.setLayout(v)

class GroupAc(QGroupBox):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setTitle("Projelerim")
        self.setStyleSheet(open("style/anasayfa.css").read())
        
        self.setUI()
        
    def setUI(self):
        pass
        
class Btns(QHBoxLayout):
    
    def __init__(self, group):
        super().__init__()
        
        with open("style/anasayfa-btn.css") as f:
            style = f.read()
        
        self.sil = QPushButton("Projeyi Sil")
        self.sil.setObjectName("sil")
        self.sil.setCursor(QCursor(Qt.PointingHandCursor))
        self.sil.setStyleSheet(style)
        
        self.kaldır = QPushButton("Projeyi Kaldır")
        self.kaldır.setObjectName("kaldir")
        self.kaldır.setCursor(QCursor(Qt.PointingHandCursor))
        self.kaldır.setStyleSheet(style)
        
        self.ac = QPushButton("Projeyi Aç")
        self.ac.setObjectName("ac")
        self.ac.setCursor(QCursor(Qt.PointingHandCursor))
        self.ac.setStyleSheet(style)
        
        
        self.addWidget(self.sil)
        self.addStretch()
        self.addWidget(self.kaldır)
        self.addWidget(self.ac)
    
    
    
    
    
