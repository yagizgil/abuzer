from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os,sys

class BtnSil(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(100,100)
        self.setObjectName("preffr")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/delete.png")
        pix = pix.scaled(QSize(40,40))
        logo.setPixmap(pix)
        logo.resize(45,45)
        
        lbl = QLabel("Sil")
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("btnlbl")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)
    
    def setFile(self, file):
        self.file = file


class BtnAc(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(100,100)
        self.setObjectName("preffr")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/edit.png")
        pix = pix.scaled(QSize(35,35))
        logo.setPixmap(pix)
        logo.resize(40,40)
        
        lbl = QLabel("Düzenle\n(Aç)")
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("btnlbl")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)
    
    def setFile(self, file):
        self.file = file
        

class BtnAdlandır(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(100,100)
        self.setObjectName("preffr")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/edit.png")
        pix = pix.scaled(QSize(35,35))
        logo.setPixmap(pix)
        logo.resize(40,40)
        
        lbl = QLabel("Yeniden\nAdlandır")
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("btnlbl")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)
    
    def setFile(self, file):
        self.file = file



class BtnKlasor(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(100,100)
        self.setObjectName("preffr")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/folder2.png")
        pix = pix.scaled(QSize(35,35))
        logo.setPixmap(pix)
        logo.resize(40,40)
        
        lbl = QLabel("Klasörde Aç")
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("btnlbl")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)
    
    def setFile(self, file):
        self.file = file



class BtnCalistir(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(100,100)
        self.setObjectName("preffr")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/console2.png")
        pix = pix.scaled(QSize(45,45))
        logo.setPixmap(pix)
        logo.resize(55,55)
        
        lbl = QLabel("Çalıştır")
        lbl.setWordWrap(True)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("btnlbl")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)
    
    def setFile(self, file):
        self.file = file




