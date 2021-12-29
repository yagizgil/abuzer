# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Menu(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("menufr")
        self.setStyleSheet(open("style/menu/menu.css", "r").read())
        self.setMaximumWidth(260)  #menu büyük olmaması için sınırlama
        self.setUI()
    
    def setUI(self):
        layout = QVBoxLayout()
        
        
        anasayfa = Tab("home",self.me)
        bilgi = Tab("bilgi",self.me)
        icerik = Tab("icerik",self.me)
        dizin = Tab("dizin",self.me)
        ayar = Tab("ayar",self.me)
        manager = Tab("manager",self.me)
        self.onoff = LogoMenu(self.me)
        
        
        
        layout.addWidget(self.onoff)
        layout.addWidget(anasayfa)
        layout.addWidget(bilgi)
        layout.addWidget(icerik)
        layout.addWidget(dizin)
        layout.addWidget(ayar)
        layout.addStretch()
        layout.addWidget(manager)
        
        
        self.setLayout(layout)
        

class LogoMenu(QFrame):
    ls = list()
    def __init__(self,me):
        super().__init__()
        self.setStyleSheet(open("style/menu/logo.css", "r").read())
        self.me = me
        self.setObjectName("fr")
        self.setFixedSize(250, 70)
        self.ls.append(self)
        
        f = QVBoxLayout()
        f2 = QHBoxLayout()
        
        self.btn = OnOff(me, Tab.liste)
        self.logo = Logo()
        
        f2.addWidget(self.logo)
        f2.addStretch()
        f2.addWidget(self.btn)   
        
        f.addLayout(f2)
        
        self.setLayout(f)

class Tab(QFrame):
    
    liste = list()
    
    def __init__(self,tab,me):
        super().__init__()
        self.setStyleSheet(open("style/menu/default.css", "r").read())
        self.liste.append(self)
        self.tab = tab
        self.me = me
        
        self.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.setFixedSize(250, 70)
        
        f = QVBoxLayout()
        f2 = QHBoxLayout()
        
    
        if tab == "home":
            self.btn = HomeButton(me, self.liste)
            self.lbl = QLabel("Anasayfa")
            
            self.btn.setObjectName("")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
            
            self.setStyleSheet("""QPushButton {
                                    border: none;
                                    outline: 0;
                                    text-align: center;
                                }
                                QFrame {
                                    background: #f7f1e3;
                                }
                                QFrame:hover {
                                    background: #f7f1e3;
                                }
                                
                                QLabel {
                                    font-size: 20px;
                                    color: #2c2c54;
                                }""")
        
        elif tab == "bilgi":
            self.btn = PBilgiButton(me, self.liste)
            self.lbl = QLabel("Proje Bilgisi")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
        
        elif tab == "icerik":
            self.btn = PIcerikButton(me, self.liste)
            self.lbl = QLabel("Proje İçeriği")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
            
        elif tab == "dizin":
            self.btn = PDizinButton(me, self.liste)
            self.lbl = QLabel("Proje Dizini")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
        
        elif tab == "ayar":
            self.btn = PAyarButton(me, self.liste)
            self.lbl = QLabel("Proje Ayarları")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
            
        elif tab == "manager":
            self.btn = ManagerButton(me, self.liste)
            self.lbl = QLabel("Abuzer")
            
            f2.addWidget(self.btn)
            f2.addWidget(self.lbl)
            f.addLayout(f2)
        
        
        self.setLayout(f)
        
    def mousePressEvent(self, event):
        if self.tab == "home":
            self.me.myscreen.tabwidget.setCurrentIndex(0)
            self.liste[0].setStyleSheet(open("style/menu/selected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())
            
        elif self.tab == "bilgi":
            self.me.myscreen.tabwidget.setCurrentIndex(1)
            self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/selected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())
            
        elif self.tab == "icerik":
            self.me.myscreen.tabwidget.setCurrentIndex(2)
            self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/selected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())
        
        elif self.tab == "dizin":
            self.me.myscreen.tabwidget.setCurrentIndex(3)
            self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/selected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())
            
        elif self.tab == "ayar":
            self.me.myscreen.tabwidget.setCurrentIndex(4)
            self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/selected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())
            
        elif self.tab == "manager":
            self.me.myscreen.tabwidget.setCurrentIndex(5)
            self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
            self.liste[5].setStyleSheet(open("style/menu/selected.css", "r").read())
        

class Logo(QLabel):
    ls = list()
    def __init__(self):
        super().__init__()
        self.ls.append(self)
        
        self.pixmap = QPixmap("image/logo.png")
        self.pixmap = self.pixmap.scaled(QSize(160,40))
        self.setPixmap(self.pixmap)
        self.resize(160,40)


class OnOff(QPushButton):
    state = 1
    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        self.setObjectName("menu")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.setIcon(QIcon("image/menu.png"))
        self.setFixedSize(60, 60)
        self.setIconSize(QSize(45,45))
        
    
    def mousePressEvent(self, event):
        if self.state == 1:
            for i in self.liste:
                i.lbl.setVisible(False)   
                
            Logo.ls[0].setVisible(False)
            LogoMenu.ls[0].setFixedSize(70,70)
            
            for i in self.liste:
                i.setFixedSize(80, 70)
                
            self.me.mymenu.setFixedWidth(90)
            
            self.state = 0
        else:
            for i in self.liste:
                i.lbl.setVisible(True)
                
            Logo.ls[0].setVisible(True)
            LogoMenu.ls[0].setFixedSize(250,70)
            
            for i in self.liste:
                i.setFixedSize(250, 70)
                
            self.me.mymenu.setFixedWidth(260)
                
            self.state = 1
        

        
class HomeButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/home.png"))
        self.setIconSize(QSize(50,50))

    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(0)
        self.liste[0].setStyleSheet(open("style/menu/selected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())


class PBilgiButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/belge-bilgi.png"))
        self.setIconSize(QSize(50,50))
    
    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(1)
        self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/selected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())


class PIcerikButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/belge-icerik.png"))
        self.setIconSize(QSize(50,50))

    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(2)
        self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/selected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())


class PDizinButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/belge-dizin.png"))
        self.setIconSize(QSize(50,50))

    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(3)
        self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/selected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())


class PAyarButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/belge-ayarlar.png"))
        self.setIconSize(QSize(50,50))

    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(4)
        self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/selected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/unselected.css", "r").read())


class ManagerButton(QPushButton):

    def __init__(self, me, liste):
        super().__init__()
        self.me = me
        self.liste = liste
        
        self.setCursor(QCursor(Qt.PointingHandCursor))

        self.setLayoutDirection(Qt.RightToLeft)
        self.setFixedSize(50,50)
        self.setIcon(QIcon("image/manager.png"))
        self.setIconSize(QSize(50,50))

    def mousePressEvent(self, event):
        self.me.myscreen.tabwidget.setCurrentIndex(5) 
        self.liste[0].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[1].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[2].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[3].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[4].setStyleSheet(open("style/menu/unselected.css", "r").read())
        self.liste[5].setStyleSheet(open("style/menu/selected.css", "r").read())
        
        
        