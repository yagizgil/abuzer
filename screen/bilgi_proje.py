# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class BilgiProje(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setStyleSheet(open("style/bilgi.css").read())
        self.setUI()

    def setUI(self):
        v = QVBoxLayout()
        
        sp = QSplitter(Qt.Horizontal)
        self.form1 = f1()
        self.form2 = f2()
        
        sp.addWidget(self.form1)
        sp.addWidget(self.form2)
        
        v.addWidget(sp)
        self.setLayout(v)


class f1(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setUI()
        self.setF()
        
    def setUI(self):
        f = QFormLayout()
        
        self.ad = QLineEdit()
        self.surum = QLineEdit()
        self.id = QLabel("110521172136")
        
        self.boyut = QLabel("Bekleniyor...")
        
        self.tariholus = QLabel("Bekleniyor...")
        
        self.tarihduzen = QLabel("Bekleniyor...")
        
        self.yol = QLineEdit()
        
        self.pysurum = QLabel("3.6")
        
        self.maindosya = QComboBox()
        self.lisanstur = QComboBox()
        
        self.amac = QTextEdit()
        
        
        f.addRow(QLabel("Proje Adı: "), self.ad)
        f.addRow(QLabel("Proje Sürümü: "), self.surum)
        f.addRow(QLabel("Proje ID'si: "), self.id)
        f.addRow(QLabel("Proje Boyutu: "), self.boyut)
        f.addRow(QLabel("Oluşturulma Tarihi: "), self.tariholus)
        f.addRow(QLabel("Son Düzenleme Tarihi: "), self.tarihduzen)
        f.addRow(QLabel("Proje Yolu: "), self.yol)
        f.addRow(QLabel("Python Sürümü: "), self.pysurum)
        f.addRow(QLabel("Main Dosyası: "), self.maindosya)
        f.addRow(QLabel("Lisans Türü: "), self.lisanstur)
        f.addRow(QLabel("Proje Amacı: "), self.amac)
        
        
        self.setLayout(f)
        
    def setF(self):        
        self.lisanstur.addItems(["-","MIT","APACHE","GNU"])
        
        
        

class f2(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        v = QVBoxLayout()
        
        f1 = QFormLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("plogo")
        self.pixmap = QPixmap("image/default-project-logo.png")
        self.pixmap = self.pixmap.scaled(QSize(100,100))
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(100,100)
        
        self.yol = QLabel("image/default-project-logo.png")
        self.yol.setAlignment(Qt.AlignCenter)
        
        h = QHBoxLayout()
        
        foto_kaldır = QPushButton("Kaldır")
        foto_kaldır.setObjectName("fk")
        foto_kaldır.setCursor(QCursor(Qt.PointingHandCursor))
        foto_kaldır.setMaximumWidth(200)
        foto_kaldır.setMinimumWidth(90)
        
        foto_yeni = QPushButton("Yeni")
        foto_yeni.setObjectName("fy")
        foto_yeni.setCursor(QCursor(Qt.PointingHandCursor))
        foto_yeni.setMaximumWidth(200)
        foto_yeni.setMinimumWidth(90)
        
        h.addStretch()
        h.addWidget(foto_kaldır)
        h.addWidget(foto_yeni)
        h.addStretch()
        
        f1.addRow(self.logo)
        f1.addRow(self.yol)
        f1.addRow(h)
        
        w = QWidget()
        w.setObjectName("wb")
        mv = QVBoxLayout()
        
        lbl = QLabel("Proje Kütüphaneleri")
        lbl.setAlignment(Qt.AlignCenter)
        
        self.moduller = Moduller()
        for i in range(100):
            self.moduller.addItem(str(i))
        mv.addWidget(self.moduller)
        
        w.setLayout(mv)
        
        v.addLayout(f1)
        v.addWidget(lbl)
        v.addWidget(w)
        self.setLayout(v)
        


class Moduller(QListWidget):
    
    def __init__(self):
        super().__init__()
        
        
        
        
        
