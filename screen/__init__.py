# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from screen.home import *
from screen.bilgi_proje import *
from screen.icerik_proje import *
from screen.dizin_proje import *
from screen.ayar_proje import *
from screen.ayarlar import *

class Screen(QWidget):
    
    def __init__(self,  me):
        super().__init__()
        self.me = me
        
        self.setUI()
        
    def setUI(self):
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.tabwidget = TabWidget(self.me)
        v.addWidget(self.tabwidget)
        
        h.addLayout(v)
        self.setLayout(h)
        

class TabWidget(QTabWidget):

    def __init__(self, me):
        super().__init__()
        self.me = me

        bar = QTabBar()
        bar.setObjectName("bar")
        self.setTabBar(bar)
        self.setObjectName("tab")

        self.setStyleSheet("""#tab {
                                width: 0px;
                                height: 0px;
                                border-style: none;
                                
                                }
                            #bar::tab {
                                width: 0px;
                                height: 0px;
                                border-style: none;
                            }
                            #tab::pane {
                                border-style: none;
                            }  
                            """)

        self.setUI()

    def setUI(self):
        self.home = Anasayfa(self.me)
        self.projebilgi = BilgiProje(self.me)
        self.projeicerik = IcerikProje(self.me)
        self.projedizin = DizinProje(self.me)
        self.projeayar = AyarProje(self.me)
        self.ayarlar = Ayarlar(self.me)

        self.addTab(self.home, "") 
        self.addTab(self.projebilgi, "")
        self.addTab(self.projeicerik, "")
        self.addTab(self.projedizin, "")
        self.addTab(self.projeayar, "")
        self.addTab(self.ayarlar, "")
        
        
        
        