# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class IcerikProje(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setStyleSheet(open("style/icerik.css").read())

        self.setUI()

    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        sp = QSplitter(Qt.Horizontal)
            
        self.arayuz = Arayuz(self.me)
        self.medya = Medya(self.me)
        
        
        sp.addWidget(self.arayuz)
        sp.addWidget(self.medya)
        
        
        v.addWidget(sp)
        h.addLayout(v)
        self.setLayout(h)


class Arayuz(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("f")
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        search_main_vbox = QVBoxLayout()
        search_hbox = QHBoxLayout()
        
        self.search = QLineEdit()
        self.search.setPlaceholderText("Ara..")
        self.search.textChanged.connect(self.ara)
        
        self.filtre_cb = QComboBox()
        self.filtre_cb.setCursor(QCursor(Qt.PointingHandCursor))
        self.filtre_cb.setMinimumWidth(150)
        self.filtre_cb.setMaximumWidth(250)
        self.filtre_cb.addItem("Tümü")
        
        frm = QFrame()
        frm.setFrameShape(QFrame.HLine)

        search_hbox.addWidget(self.search)
        search_hbox.addWidget(self.filtre_cb) 
        
        search_main_vbox.addLayout(search_hbox)
        search_main_vbox.addWidget(frm)
        
        v.addLayout(search_main_vbox)
        
        
        
        self.scr = Scroll(self.me)
        v.addWidget(self.scr)
        
        
        mh.addLayout(v)
        self.setLayout(mh)
        
    def ara(self):
        for i in ArayuzFrame.liste:
            if self.search.text() not in i.header.text():
                i.setVisible(False)
            else:
                i.setVisible(True)
        

class Scroll(QScrollArea):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("arayuz_scr")
        
        self.setWidgetResizable(True)
        self.setUI()
    
    def setUI(self):
        w = QWidget()
        self.f = QFormLayout()
        
        self.f.addRow(ArayuzFrame(self.me,"Duru"))
        self.f.addRow(ArayuzFrame(self.me,"Yakamoz"))
        self.f.addRow(ArayuzFrame(self.me,"Toprak"))
        self.f.addRow(ArayuzFrame(self.me,"Çiselemek"))
        self.f.addRow(ArayuzFrame(self.me,"Birlik"))
        self.f.addRow(ArayuzFrame(self.me,"Üstad"))
        self.f.addRow(ArayuzFrame(self.me,"Hazan"))
        self.f.addRow(ArayuzFrame(self.me,"Işıl"))
        self.f.addRow(ArayuzFrame(self.me,"Dandik"))
        self.f.addRow(ArayuzFrame(self.me,"Başak"))
        self.f.addRow(ArayuzFrame(self.me,"Vatan"))
        self.f.addRow(ArayuzFrame(self.me,"Gönenç"))
        self.f.addRow(ArayuzFrame(self.me,"Hayat"))
        self.f.addRow(ArayuzFrame(self.me,"Gökyüzü"))
        self.f.addRow(ArayuzFrame(self.me,"Deniz"))
        self.f.addRow(ArayuzFrame(self.me,"Gönül"))
        self.f.addRow(ArayuzFrame(self.me,"Kof"))
        self.f.addRow(ArayuzFrame(self.me,"Kutlu"))
        self.f.addRow(ArayuzFrame(self.me,"Barış"))
        self.f.addRow(ArayuzFrame(self.me,"Sevmek"))
        self.f.addRow(ArayuzFrame(self.me,"Sarmak"))
        
        self.f.addRow(ArayuzFrame(self.me,"Dudu"))
        self.f.addRow(ArayuzFrame(self.me,"Cennet "))
        self.f.addRow(ArayuzFrame(self.me,"Kelam"))
        self.f.addRow(ArayuzFrame(self.me,"Aşk"))
        self.f.addRow(ArayuzFrame(self.me,"Bilakis"))
        self.f.addRow(ArayuzFrame(self.me,"Deniz"))
        self.f.addRow(ArayuzFrame(self.me,"Yasal"))
        self.f.addRow(ArayuzFrame(self.me,"Yeniden"))
        
        w.setLayout(self.f)
        self.setWidget(w)
        
class ArayuzFrame(QFrame):
    state = False
    liste = list()
    a_etiket = ""
    a_olust = ""
    a_degist = ""
    
    def __init__(self, me, asd):
        super().__init__()
        self.me = me
        self.a = asd
        self.setObjectName("af")
        self.liste.append(self)
        
        self.setUI()
        
    def setUI(self):
        h = QHBoxLayout()
        
        
        #-------------------------------------------Logo---------------------------
        logo_frm = QFrame()
        logo_frm.setObjectName("lg")
        logo_frm.setMaximumWidth(150)
        logo_mv = QVBoxLayout()
        logo_h = QHBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("plogo")
        self.pixmap = QPixmap("image/default-project-logo.png")
        self.pixmap = self.pixmap.scaled(QSize(100,100))
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(100,100)
        
        logo_h.addWidget(self.logo)
        logo_mv.addLayout(logo_h)
        logo_frm.setLayout(logo_mv)
        #-----------------------------------------Logo------------------------
        v = QVBoxLayout()
        #-------------------------------------Header---------------------------
        header_hbox = QHBoxLayout()
        
        header_vbox = QVBoxLayout()
        
        self.header = QLabel(self.a)
        self.header.setObjectName("header")
        
        self.id = QLabel("13052021012645")
        self.id.setObjectName("id")
        
        header_vbox.addWidget(self.header)
        header_vbox.addWidget(self.id)
        
        self.detals = QPushButton("")
        self.detals.setObjectName("details")
        self.detals.setFixedSize(40, 40)
        self.detals.setMaximumWidth(40)
        self.detals.setMaximumHeight(40)
        self.detals.setIcon(QIcon("image/details.png"))
        self.detals.setIconSize(QSize(35,35))
        self.detals.setCursor(QCursor(Qt.PointingHandCursor))
        self.detals.setVisible(False)
        
        self.btn = QPushButton("Yükle")
        self.btn.setObjectName("btn")
        self.btn.setFixedHeight(35)
        self.btn.setMaximumWidth(250)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn.clicked.connect(self.yuklendi)
        
        header_hbox.addLayout(header_vbox)
        header_hbox.addWidget(self.detals)
        header_hbox.addWidget(self.btn)
        #--------------------------------Header----------------------
        v.addLayout(header_hbox)
        #-------------------------------Content-------------
        content_vbox = QVBoxLayout()
    
        self.aciklama = QLabel("""""")
        self.aciklama.setWordWrap(True)
        
        content_vbox.addWidget(self.aciklama)
        #------------------------------Content--------------------
        v.addLayout(content_vbox)
        #------------------------------content2---------------------
        content_hbox = QHBoxLayout()
        
        self.etiket = QLabel("Etiket: menu")
        self.etiket.setObjectName("etiket")
        
        self.dosya_boyut = QLabel("Dosya Boyutu: 15 mb")
        self.dosya_boyut.setObjectName("boyut")
        
        self.olustarih = QLabel("Oluşturulma Tarihi: 11/05/2021")
        self.olustarih.setObjectName("otarih")
        
        self.yukletarih = QLabel("Yüklenme Tarihi: 12/05/2021")
        self.yukletarih.setObjectName("ytarih")
        
        content_hbox.addWidget(self.etiket)
        content_hbox.addWidget(self.dosya_boyut)
        content_hbox.addStretch()
        content_hbox.addWidget(self.olustarih)
        content_hbox.addWidget(self.yukletarih)
        #----------------------------content2-------------------
        v.addLayout(content_hbox)
        
        h.addWidget(logo_frm)
        h.addLayout(v)
        self.setLayout(h)
        
    
    def yuklendi(self):
        if self.state == False:
            self.setStyleSheet(open("style/icerik_selected.css").read())
            self.btn.setText("Yüklendi")
            self.btn.setCursor(QCursor(Qt.ArrowCursor))
            
            self.detals.setVisible(True)
            
            print("yüklendi")
            self.state = True
        else:
            print("nasıl tekrar yüklücen mk")






class Medya(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("f")
        self.setMinimumWidth(280)
        self.setMaximumWidth(350)
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        search_main_vbox = QVBoxLayout()
        
        self.search = QLineEdit()
        self.search.setPlaceholderText("Ara..")
        self.search.textChanged.connect(self.ara)
        self.search.setObjectName("medya_search")
        
        self.filtre_cb = QComboBox()
        self.filtre_cb.setCursor(QCursor(Qt.PointingHandCursor))
        self.filtre_cb.setObjectName("medya_cb")

        self.filtre_cb.addItems(["Tümü","Resim","Video","Ses"])
        
        frm = QFrame()
        frm.setFrameShape(QFrame.HLine)
        
        search_main_vbox.addWidget(self.search)
        search_main_vbox.addWidget(self.filtre_cb)
        search_main_vbox.addWidget(frm)
        
        v.addLayout(search_main_vbox)

        self.scr = MedyaScroll(self.me)
        v.addWidget(self.scr)
        
        
        mh.addLayout(v)
        self.setLayout(mh)
        
    def ara(self):
        pass

class MedyaScroll(QScrollArea):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("arayuz_scr")
        
        self.setWidgetResizable(True)
        self.setUI()
    
    def setUI(self):
        w = QWidget()

        
        self.f = QFormLayout()
        
        self.f.addRow(MedyaFrame(self.me,"Duru"))
        self.f.addRow(MedyaFrame(self.me,"Yakamoz"))
        self.f.addRow(MedyaFrame(self.me,"aksdfghjsdfghjklwertyuıopxchjklşlkjhgfdertyuı"))

        w.setLayout(self.f)
        self.setWidget(w)
        
class MedyaFrame(QFrame):
    detay_state = False
    liste = list()
    m_olust = ""
    m_tur  = ""
    
    def __init__(self, me, asd):
        super().__init__()
        self.me = me
        self.a = asd
        self.setObjectName("af")
        self.liste.append(self)
        self.setMaximumWidth(250)
        
        self.setUI()
        
    def setUI(self):
        v = QVBoxLayout()
        
        #-------------------------------------------Logo---------------------------
        logo_fh = QHBoxLayout()
        logo_frm = QFrame()
        logo_frm.setObjectName("lg")
        logo_frm.setMaximumWidth(200)
        logo_mv = QVBoxLayout()
        logo_h = QHBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("plogo")
        self.pixmap = QPixmap("image/default-project-logo.png")
        self.pixmap = self.pixmap.scaled(QSize(150,150))
        self.logo.setPixmap(self.pixmap)
        self.logo.resize(150,150)
        
        logo_h.addWidget(self.logo)
        logo_mv.addLayout(logo_h)
        logo_frm.setLayout(logo_mv)
        logo_fh.addStretch()
        logo_fh.addWidget(logo_frm)
        logo_fh.addStretch()
        #-----------------------------------------Logo------------------------
        v.addLayout(logo_fh)
        #-------------------------------------Header---------------------------
        self.header = QLabel()
        self.header.setObjectName("medya_header")
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setWordWrap(True)
        if len(self.a) > 10:
            f = self.a[0:10]
            if len(self.a[10::]) > 10:
                b = self.a[10:20]
                if len(self.a[20::]) > 10:
                    c = self.a[20:30]
                    if len(self.a[30::]) > 10:
                        d = self.a[30:40]
                        if len(self.a[40::]) > 10:
                            e = self.a[40:50]
                            self.header.setText(str(f+'\n'+b+'\n'+c+'\n'+d+'\n'+e))
                        else:
                            self.header.setText(str(f+'\n'+b+'\n'+c+'\n'+d))
                    else:
                        self.header.setText(str(f+'\n'+b+'\n'+c))
                else:
                    self.header.setText(str(f+'\n'+b))
            else:
                self.header.setText(str(self.a))
        else:
            self.header.setText(str(self.a))
        #--------------------------------Header----------------------
        v.addWidget(self.header)
        #--------------------------------Btn------------
        btn_hbox = QHBoxLayout()
        
        fram = QFrame()
        fram.setObjectName("fram")
        fh = QHBoxLayout()
        
        self.btn = QPushButton("Aç")
        self.btn.setObjectName("m_btn")
        self.btn.setFixedHeight(35)
        self.btn.setMinimumWidth(110)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.onoff = QPushButton()
        self.onoff.setObjectName("m_on_btn")
        self.onoff.setFixedSize(35,35)
        self.onoff.setMaximumSize(35,35)
        self.onoff.setCursor(QCursor(Qt.PointingHandCursor))
        self.onoff.setIcon(QIcon("image/down-arrow.png"))
        self.onoff.setIconSize(QSize(25,25))
        self.onoff.clicked.connect(self.detay_onoff)
        
        fh.addWidget(self.btn)
        fh.addWidget(self.onoff)
        
        fram.setLayout(fh)
        
        btn_hbox.addStretch()
        btn_hbox.addWidget(fram)
        btn_hbox.addStretch()
        #--------------------------------Btn------------
        v.addLayout(btn_hbox)
        #-----------------------------------content-------------
        self.detay_frm = QFrame()
        content_vbox = QVBoxLayout()
        
        self.olus_t = QLabel("Oluşturma Tarihi: 14/05/2021")
        self.olus_t.setAlignment(Qt.AlignCenter)
        
        self.süre = QLabel("Süre: 3.16 dk")
        self.süre.setAlignment(Qt.AlignCenter)
        
        self.goruntu_boyut = QLabel("Boyut: 480 / 360")
        self.goruntu_boyut.setAlignment(Qt.AlignCenter)
        
        self.dosya_boyut = QLabel("Dosya Boyutu: 2.5 mb")
        self.dosya_boyut.setAlignment(Qt.AlignCenter)
        
        
        self.btn = QPushButton("Detaylar")
        self.btn.setObjectName("btn")
        self.btn.setFixedHeight(35)
        self.btn.setMaximumWidth(250)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        content_vbox.addWidget(self.olus_t)
        
        if self.m_tur == "Resim":
            content_vbox.addWidget(self.goruntu_boyut)
            
        elif self.m_tur == "Video":
            content_vbox.addWidget(self.goruntu_boyut)
            content_vbox.addWidget(self.süre)
            
        elif self.m_tur == "Ses":
            content_vbox.addWidget(self.süre)
            
        else:
            content_vbox.addWidget(self.goruntu_boyut)
            content_vbox.addWidget(self.süre)
        
        
        content_vbox.addWidget(self.dosya_boyut)
        content_vbox.addWidget(self.btn)
        
        self.detay_frm.setLayout(content_vbox)
        self.detay_frm.setVisible(False)
        #-------------------------------------content------------------------
        v.addWidget(self.detay_frm)
        
        self.setLayout(v)
        
    
    def detay_onoff(self):
        if self.detay_state == False:
            self.detay_frm.setVisible(True)
            self.onoff.setIcon(QIcon("image/up-arrow.png"))
            self.detay_state = True
        else:
            self.detay_frm.setVisible(False)
            self.onoff.setIcon(QIcon("image/down-arrow.png"))
            self.detay_state = False


