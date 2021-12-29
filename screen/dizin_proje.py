# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys,os
from widgets.prefences import *
from widgets.content import *
from widgets.dizin_menu import *

import datetime
import locale

locale.setlocale(locale.LC_ALL, '')


class DizinProje(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setStyleSheet(open("style/dizin.css").read())

        self.setUI()

    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        sp1 = QSplitter(Qt.Horizontal)
        sp2 = QSplitter(Qt.Vertical)
        
        
        self.fryeni = YeniFrame(self.me)
        self.frdizin = Dizin(self.me)
        self.frsagfr = SagFrame(self.me)
        
        sp2.addWidget(self.fryeni)
        sp2.addWidget(self.frdizin)
        
        sp1.addWidget(sp2)
        sp1.addWidget(self.frsagfr)
        
        v.addWidget(sp1)
        h.addLayout(v)
        self.setLayout(h)
        


class YeniFrame(QFrame):
    yeniframe_liste = list()
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.yeniframe_liste.append(self)
        self.setMaximumHeight(100)
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        #---------------------------btns--------------
        btn_h = QHBoxLayout()
        
        self.new = QPushButton()
        self.new.setObjectName("new")
        self.new.setIcon(QIcon("image/btn/new-b.png"))
        self.new.setIconSize(QSize(130,50))
        self.new.setMinimumSize(220,50)
        self.new.setMaximumSize(220,50)
        self.new.setCursor(QCursor(Qt.PointingHandCursor))
        self.new.clicked.connect(self.newonoff)
        
        self.imp = QPushButton()
        self.imp.setObjectName("imp")
        self.imp.setIcon(QIcon("image/btn/import-b.png"))
        self.imp.setIconSize(QSize(130,50))
        self.imp.setMinimumSize(220,50)
        self.imp.setMaximumSize(220,50)
        self.imp.setCursor(QCursor(Qt.PointingHandCursor))
        
        btn_h.addWidget(self.new)
        btn_h.addWidget(self.imp)
        btn_h.addStretch()
        #------------------------btns--------------------
        v.addLayout(btn_h)
        #-------------------------------btns2----------------
        self.btn_fr = QFrame()
        self.btn_fr.setMaximumWidth(500)
        self.btn_fr.setMaximumHeight(110)
        bfr_v = QVBoxLayout()
        btn2_h = QHBoxLayout()
        btn2_h2 = QHBoxLayout()
        
        self.pyt = QPushButton()
        self.pyt.setObjectName("new")
        self.pyt.setIcon(QIcon("image/btn/python-b.png"))
        self.pyt.setIconSize(QSize(90,40))
        self.pyt.setMinimumSize(120,40)
        self.pyt.setMaximumSize(120,40)
        self.pyt.setCursor(QCursor(Qt.PointingHandCursor))
        self.pyt.clicked.connect(self.newpy)
        
        
        self.css = QPushButton()
        self.css.setObjectName("new")
        self.css.setIcon(QIcon("image/btn/css-b.png"))
        self.css.setIconSize(QSize(90,35))
        self.css.setMinimumSize(90,40)
        self.css.setMaximumSize(90,40)
        self.css.setCursor(QCursor(Qt.PointingHandCursor))
        self.css.clicked.connect(self.newcss)
        
        
        self.dbs = QPushButton()
        self.dbs.setObjectName("new")
        self.dbs.setIcon(QIcon("image/btn/db-b.png"))
        self.dbs.setIconSize(QSize(120,35))
        self.dbs.setMinimumSize(140,40)
        self.dbs.setMaximumSize(140,40)
        self.dbs.setCursor(QCursor(Qt.PointingHandCursor))
        self.dbs.clicked.connect(self.newdb)
        
        
        self.jsn = QPushButton()
        self.jsn.setObjectName("new")
        self.jsn.setIcon(QIcon("image/btn/json-b.png"))
        self.jsn.setIconSize(QSize(90,35))
        self.jsn.setMinimumSize(100,40)
        self.jsn.setMaximumSize(100,40)
        self.jsn.setCursor(QCursor(Qt.PointingHandCursor))
        self.jsn.clicked.connect(self.newjson)
        
        
        self.xml = QPushButton()
        self.xml.setObjectName("new")
        self.xml.setIcon(QIcon("image/btn/xml-b.png"))
        self.xml.setIconSize(QSize(90,35))
        self.xml.setMinimumSize(100,40)
        self.xml.setMaximumSize(100,40)
        self.xml.setCursor(QCursor(Qt.PointingHandCursor))
        self.xml.clicked.connect(self.newxml)
        
        
        self.txt = QPushButton()
        self.txt.setObjectName("new")
        self.txt.setIcon(QIcon("image/btn/metin-b.png"))
        self.txt.setIconSize(QSize(90,35))
        self.txt.setMinimumSize(110,40)
        self.txt.setMaximumSize(110,40)
        self.txt.setCursor(QCursor(Qt.PointingHandCursor))
        self.txt.clicked.connect(self.newtxt)
        
        
        self.ozl = QPushButton()
        self.ozl.setObjectName("new")
        self.ozl.setIcon(QIcon("image/btn/ozel-b.png"))
        self.ozl.setIconSize(QSize(90,35))
        self.ozl.setMinimumSize(110,40)
        self.ozl.setMaximumSize(110,40)
        self.ozl.setCursor(QCursor(Qt.PointingHandCursor))
        self.ozl.clicked.connect(self.newspc)
        
        
        self.ipt = QPushButton()
        self.ipt.setObjectName("ipt")
        self.ipt.setIcon(QIcon("image/btn/iptal-b.png"))
        self.ipt.setIconSize(QSize(90,35))
        self.ipt.setMinimumSize(100,40)
        self.ipt.setMaximumSize(100,40)
        self.ipt.setCursor(QCursor(Qt.PointingHandCursor))
        self.ipt.clicked.connect(self.newcancel)
        
        
        btn2_h.addWidget(self.pyt)
        btn2_h.addWidget(self.css)
        btn2_h.addWidget(self.dbs)
        btn2_h.addWidget(self.jsn)
        btn2_h2.addWidget(self.xml)
        btn2_h2.addWidget(self.txt)
        btn2_h2.addWidget(self.ozl)
        btn2_h2.addWidget(self.ipt)
        
        bfr_v.addLayout(btn2_h)
        bfr_v.addLayout(btn2_h2)
        self.btn_fr.setLayout(bfr_v)
        self.btn_fr.setVisible(False)
        #-------------------------btns2------------------
        v.addWidget(self.btn_fr)
        
        self.n = NewFile(self.me)
        self.n.setVisible(False)
        v.addWidget(self.n)
        
        mh.addLayout(v)
        self.setLayout(mh)
        
    
    def newonoff(self):
        self.btn_fr.setVisible(True)
        self.setMaximumHeight(190)
        self.n.setVisible(False)
    def newcancel(self):
        self.btn_fr.setVisible(False)
        self.setMaximumHeight(100)
        
    def newpy(self):
        self.n.setVisible(True)
        self.n.setFile("py")
        self.btn_fr.setVisible(False)
        
    def newcss(self):
        self.n.setVisible(True)
        self.n.setFile("css")
        self.btn_fr.setVisible(False)
        
    def newdb(self):
        self.n.setVisible(True)
        self.n.setFile("db")
        self.btn_fr.setVisible(False)
        
    def newjson(self):
        self.n.setVisible(True)
        self.n.setFile("json")
        self.btn_fr.setVisible(False)
        
    def newxml(self):
        self.n.setVisible(True)
        self.n.setFile("xml")
        self.btn_fr.setVisible(False)
    
    def newtxt(self):
        self.n.setVisible(True)
        self.n.setFile("txt")
        self.btn_fr.setVisible(False)
    
    def newspc(self):
        self.n.setVisible(True)
        self.n.setFile("")
        self.btn_fr.setVisible(False)
        

class NewFile(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("newfile")
        
        self.setUI()
        
    def setUI(self):
        mv = QVBoxLayout()
        h = QHBoxLayout()
        info_v = QVBoxLayout()
        
        #-----------------------------------header------------
        header_frm = QFrame()
        header_h = QHBoxLayout()
        
        self.name = QLineEdit()
        self.name.setObjectName("name")
        self.name.setMinimumWidth(150)
        
        self.ext = QLineEdit("py")
        self.ext.setObjectName("ext")
        self.ext.setMaximumWidth(100)
        
        self.path = QLineEdit("/")
        self.path.setObjectName("path")
        self.path.setMinimumWidth(180)
        
        self.path_btn = QPushButton()
        self.path_btn.setObjectName("path_btn")
        self.path_btn.setIcon(QIcon("image/folder.png"))
        self.path_btn.setIconSize(QSize(25,25))
        self.path_btn.setMinimumSize(30,30)
        self.path_btn.setMaximumSize(30,30)
        self.path_btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        header_h.addWidget(QLabel("Ad: "))
        header_h.addWidget(self.name)
        header_h.addWidget(QLabel("."))
        header_h.addWidget(self.ext)
        header_h.addWidget(QLabel("Konum: "))
        header_h.addWidget(self.path)
        header_h.addWidget(self.path_btn)
        header_h.addStretch()
        header_frm.setLayout(header_h)
        #-------------------------header------------------
        info_v.addWidget(header_frm)
        #-----------------------------content-------------
        self.content_fr = QFrame()
        content_h = QHBoxLayout()
        
        fr1 = QFrame()
        fr1.setObjectName("contentfr")
        fr1_mv = QVBoxLayout()
        fr1_h = QHBoxLayout()
        
        self.content_mods = Content("")
        
        fr1_h.addWidget(self.content_mods)
        fr1_mv.addLayout(fr1_h)
        fr1.setLayout(fr1_mv)
        #--------------------------------ok----------------------
        ok = QFrame()
        ok_v = QVBoxLayout()
        
        one = QLabel()
        one.setAlignment(Qt.AlignCenter)
        one.setObjectName("plogo")
        pix1 = QPixmap("image/right-arrow2.png")
        pix1 = pix1.scaled(QSize(50,50))
        one.setPixmap(pix1)
        one.resize(50,50)
        
        two = QLabel()
        two.setAlignment(Qt.AlignCenter)
        two.setObjectName("plogo")
        pix2 = QPixmap("image/right-arrow2.png")
        pix2 = pix2.scaled(QSize(50,50))
        two.setPixmap(pix2)
        two.resize(50,50)
        
        ok_v.addWidget(one)
        ok_v.addWidget(two)
        
        ok.setLayout(ok_v)
        #--------------------------------ok----------------------
        
        #-------------------codes------------------
        fr2 = QFrame()
        fr2.setObjectName("codesfr")
        fr2_mv = QVBoxLayout()
        fr2_h = QHBoxLayout()
        
        self.codes = QTextEdit()
        
        fr2_h.addWidget(self.codes)
        fr2_mv.addLayout(fr2_h)
        fr2.setLayout(fr2_mv)
        #-------------------codes------------------
        
        
        content_h.addWidget(fr1)
        content_h.addWidget(ok)
        content_h.addWidget(fr2)
        self.content_fr.setLayout(content_h)
        #-------------------------------content-----------
        info_v.addWidget(self.content_fr)
        
        #------------cizgi-------------
        cizgi = QFrame()
        cizgi.setFrameShape(QFrame.VLine)
        #---------cizg-----------

        #--------------------------------------btns-------------
        btn_fr = QFrame()
        btn_v = QVBoxLayout()
        
        self.save = QPushButton()
        self.save.setObjectName("save")
        self.save.setIcon(QIcon("image/save.png"))
        self.save.setIconSize(QSize(50,50))
        self.save.setMinimumSize(50,50)
        self.save.setMaximumSize(50,50)
        self.save.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.reset = QPushButton()
        self.reset.setObjectName("reset")
        self.reset.setIcon(QIcon("image/refresh.png"))
        self.reset.setIconSize(QSize(50,50))
        self.reset.setMinimumSize(50,50)
        self.reset.setMaximumSize(50,50)
        self.reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset.clicked.connect(self.__reset)
        
        
        self.cancel = QPushButton()
        self.cancel.setObjectName("cancel")
        self.cancel.setIcon(QIcon("image/cancel.png"))
        self.cancel.setIconSize(QSize(50,50))
        self.cancel.setMinimumSize(50,50)
        self.cancel.setMaximumSize(50,50)
        self.cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel.clicked.connect(self.__cancel)
        
        
        btn_v.addWidget(self.save)
        btn_v.addWidget(self.reset)
        btn_v.addStretch()
        btn_v.addWidget(self.cancel)
        btn_fr.setLayout(btn_v)
        #-------------------------------btns--------------------
        
        
        h.addLayout(info_v)
        h.addWidget(cizgi)
        h.addWidget(btn_fr)
        mv.addLayout(h)
        self.setLayout(mv)
        
    def setFile(self, exten):
        self.ext.setText(exten)
        self.codes.clear()
        YeniFrame.yeniframe_liste[0].setMaximumHeight(5000)
        
    def __reset(self):
        self.name.clear()
        self.path.setText("/")
        self.codes.clear()
        
    def __cancel(self):
        self.__reset()
        self.setVisible(False)
        YeniFrame.yeniframe_liste[0].setMaximumHeight(100)


class Content(QScrollArea):
    
    def __init__(self, new):
        super().__init__()
        self.setObjectName("contentsc")
        
        self.setWidgetResizable(True)
        self.setUI()

    
    def setUI(self):
        w = QWidget()
        self.f = QFormLayout()
        
        self.f.addRow(ContentMods("abuzer"))
        self.f.addRow(ContentMods("duru"))
        self.f.addRow(ContentMods("esrar"))
        self.f.addRow(ContentMods("gizem"))
        self.f.addRow(ContentMods("aspder"))
        self.f.addRow(ContentMods("abuzer"))
        self.f.addRow(ContentMods("duru"))
        self.f.addRow(ContentMods("esrar"))
        self.f.addRow(ContentMods("gizem"))
        self.f.addRow(ContentMods("aspder"))
        self.f.addRow(ContentMods("abuzer"))
        self.f.addRow(ContentMods("duru"))
        self.f.addRow(ContentMods("esrar"))
        self.f.addRow(ContentMods("gizem"))
        self.f.addRow(ContentMods("aspder"))
        
        w.setLayout(self.f)
        self.setWidget(w)


class ContentMods(QFrame):
    state = False
    liste = list()
    a_etiket = ""
    a_olust = ""
    a_degist = ""
    
    def __init__(self,  asd):
        super().__init__()
        self.a = asd
        self.setObjectName("af")
        self.liste.append(self)
        
        self.setUI()
        
    def setUI(self):
        h = QHBoxLayout()
        
        v = QVBoxLayout()
        #-------------------------------------Header---------------------------
        self.header = QLabel(self.a)
        self.header.setObjectName("header")
        #--------------------------------Header----------------------
        v.addWidget(self.header)
        #-------------------------------Content-------------
        content_vbox = QVBoxLayout()
    
        self.aciklama = QLabel("""""")
        self.aciklama.setWordWrap(True)
        
        content_vbox.addWidget(self.aciklama)
        #------------------------------Content--------------------
        v.addLayout(content_vbox)
        
        
        #--------------------------------set----------
        set_v = QVBoxLayout()
        
        self.set_btn = QPushButton()
        self.set_btn.setObjectName("set_btn")
        self.set_btn.setIcon(QIcon("image/right-arrow.png"))
        self.set_btn.setIconSize(QSize(50,50))
        self.set_btn.setMinimumSize(60,60)
        self.set_btn.setMaximumSize(60,60)
        self.set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        set_v.addWidget(self.set_btn)
        #----------------------------set----------------------
        
        h.addLayout(v)
        h.addLayout(set_v)
        self.setLayout(h)











class Dizin(QFrame):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setObjectName("frs")
        
        self.setUI()
        
    def setUI(self):
        mv = QVBoxLayout()
        h = QHBoxLayout()
        
        sp = QSplitter(Qt.Horizontal)
        
        self.filetree = FileTree(os.getcwd(),self)
        sp.addWidget(self.filetree)
        
        self.dizindetails = DizinFileDetails()
        sp.addWidget(self.dizindetails)
        
        self.dizindetails.setVisible(False)
        
        h.addWidget(sp)
        mv.addLayout(h)
        self.setLayout(mv)
        
    

class FileTree(QTreeView):
    
    def __init__(self, path, dizin):
        super().__init__()
        self.path = path
        self.dizin = dizin
        
        self.setUI()
    
    def setUI(self):
        self.filemodel = QFileSystemModel()
        self.filemodel.setRootPath(self.path)
        
        self.setModel(self.filemodel)
        self.setRootIndex(self.filemodel.index(self.path))
        
        self.setAnimated(True)
        
        self.clicked.connect(self.getpath)

    def getpath(self, index):
        path = self.sender().model().filePath(index)
        
        if os.path.isfile(path):
            self.dizin.dizindetails.setFile(path)
        
        if os.path.isdir(path):
            self.dizin.dizindetails.setVisible(False)



class DizinFileDetails(QFrame):
    file = ""
    def __init__(self):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        cizgi1 = QFrame()
        cizgi1.setFrameShape(QFrame.VLine)
        
        #---------------------header----------------
        header_h = QHBoxLayout()
        
        self.close = QPushButton("X")
        self.close.setObjectName("close")
        self.close.setFixedSize(40,40)
        self.close.setCursor(QCursor(Qt.PointingHandCursor))
        self.close.clicked.connect(self.__close)
        
        self.name = QLabel("main.py")
        self.name.setObjectName("name")
        
        self.run = QPushButton()
        self.run.setObjectName("run")
        self.run.setIcon(QIcon("image/open.png"))
        self.run.setIconSize(QSize(35,35))
        self.run.setMinimumSize(40,40)
        self.run.setMaximumSize(40,40)
        self.run.setCursor(QCursor(Qt.PointingHandCursor))
        
        header_h.addWidget(self.close)
        header_h.addWidget(self.name)
        header_h.addStretch()
        header_h.addWidget(self.run)
        #------------------header-------------
        v.addLayout(header_h)
        #--------------------------------------------------
        cizgi2 = QFrame()
        cizgi2.setFrameShape(QFrame.HLine)
        #--------------------------------------------------
        v.addWidget(cizgi2)
        #------------------------------özellikller----------
        pref_h = QHBoxLayout()
        
        self.prefext = ExtPref()
        self.prefmain = MainPref()
        self.prefsize = SizePref()
        
        self.prefmain.setVisible(False)
        
        pref_h.addStretch()
        pref_h.addWidget(self.prefext)
        pref_h.addWidget(self.prefmain)
        pref_h.addWidget(self.prefsize)
        pref_h.addStretch()
        #---------------------------------özellikler--------
        v.addLayout(pref_h)
        #----------------------içindeki dosyalar---------------       
        sc_area = QScrollArea()
        sc_area.setWidgetResizable(True)
        sc_w = QWidget()
        self.sc_f = QFormLayout()
        
        
        sc_w.setLayout(self.sc_f)
        sc_area.setWidget(sc_w)
        #----------------------içindeki dosyalar---------------
        v.addWidget(sc_area)
        #--------------------------------------------------
        cizgi3 = QFrame()
        cizgi3.setFrameShape(QFrame.HLine)
        #--------------------------------------------------
        v.addWidget(cizgi3)
        #----------------alt bölum--------------------
        bmenu_h = QHBoxLayout()
        
        self.delet = QPushButton()
        self.delet.setObjectName("delet")
        self.delet.setIcon(QIcon("image/delete.png"))
        self.delet.setIconSize(QSize(50,50))
        self.delet.setMinimumSize(60,60)
        self.delet.setMaximumSize(60,60)
        self.delet.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        detay_frm = QFrame()
        detay_frm.setObjectName("detay_frm")
        detay_h = QHBoxLayout()
        
        self.detay = QPushButton()
        self.detay.setObjectName("set_btn")
        self.detay.setIcon(QIcon("image/right-arrow.png"))
        self.detay.setIconSize(QSize(40,40))
        self.detay.setMinimumSize(55,55)
        self.detay.setMaximumSize(55,55)
        self.detay.setCursor(QCursor(Qt.PointingHandCursor))
        self.detay.clicked.connect(self.__setDetay)
        
        detay_h.addWidget(QLabel("Detaylı Yönetim"))
        detay_h.addWidget(self.detay)
        
        detay_frm.setLayout(detay_h)
        
        bmenu_h.addWidget(self.delet)
        bmenu_h.addWidget(detay_frm)
        #---------------------------alt bolum-----------------
        v.addLayout(bmenu_h)

        mh.addWidget(cizgi1)
        mh.addLayout(v)
        self.setLayout(mh)
        
    def setFile(self,file):
        self.file = file
        while self.sc_f.count():
            child = self.sc_f.takeAt(0)
            childWidget = child.widget()
            if childWidget:
                childWidget.setParent(None)
                childWidget.deleteLater()
        
        self.prefext.setFile(file)
        self.prefsize.setFile(file)
        
        self.name.setText(os.path.split(file)[1])
        
        try:
            l = list()
    
            with open(file,"r") as f:
                a = f.readlines()
                for i in a:
                    if "setStyleSheet(open(" in i:
                        b = i.split('"')[1]
                        if b not in l:
                            cf = ContentFile(b)
                            cf.setDetayWidget(DetayWidget.liste[0])
                            self.sc_f.addRow(cf)
    
        except:
            pass
        
        self.setVisible(True)
    
    
    def __close(self):
        self.setVisible(False)
    
    def __setDetay(self):
        a = os.path.split(self.file)[1].split(".")[1]
        if a in ["py","cs","css","cpp","qss","c","h","db","dbs","sql","html","java","json","xml","txt"]:
            DetayWidget.liste[0].setFile(self.file)






class SagFrame(QTabWidget):
    liste = list()
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.liste.append(self)
        self.setMinimumWidth(460)
        
        self.setUI()
        
    def setUI(self):
        self.dizinw = DizinWidget()
        self.detayw = DetayWidget()
        
        self.addTab(self.dizinw,"")
        self.addTab(self.detayw,"")
        


class DizinWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        search_main_vbox = QVBoxLayout()
        
        self.search = QLineEdit()
        self.search.setPlaceholderText("Ara..")
        self.search.setObjectName("file_search")
        self.search.textChanged.connect(self.ara)
        
        self.filtre_cb = QComboBox()
        self.filtre_cb.setCursor(QCursor(Qt.PointingHandCursor))
        self.filtre_cb.setObjectName("medya_cb")

        self.filtre_cb.addItems(["Tümü"])
        
        frm = QFrame()
        frm.setFrameShape(QFrame.HLine)
        
        search_main_vbox.addWidget(self.search)
        search_main_vbox.addWidget(self.filtre_cb)
        search_main_vbox.addWidget(frm)
        
        v.addLayout(search_main_vbox)
        
        #------------files---------------
        self.fs = FileScroll()
        v.addWidget(self.fs)
        
        
        mh.addLayout(v)
        self.setLayout(mh)
        
    def ara(self):
        for i in FileFrame.liste:
            if self.search.text() not in i.path.text():
                i.setVisible(False)
            else:
                i.setVisible(True)
        


class FileScroll(QScrollArea):
    
    def __init__(self):
        super().__init__()
        
        self.setWidgetResizable(True)
        self.setUI()

    def setUI(self):
        w = QWidget()
        h = QHBoxLayout()
        self.f = QFormLayout()
        
        for a,b,c in os.walk(os.getcwd()):
            for i in c:
                try:
                    name, ext = os.path.splitext(os.sep.join([a, i]))
                except:
                    name, ext = os.path.splitext(os.sep.join([a, i]))
                if ext in [".py",".cs",".css",".cpp",".qss",".c",".h",".db",".dbs",".sql",".html",".java",".json",".xml",".txt"]:
                    self.f.addRow(FileFrame(os.sep.join([a, i])))
        
        h.addStretch()
        h.addLayout(self.f)
        h.addStretch()
        w.setLayout(h)
        self.setWidget(w)



class FileFrame(QFrame):
    file = ""
    liste = list()
    def __init__(self, file):
        super().__init__()
        self.setObjectName("af")
        self.setMinimumWidth(400)
        
        self.liste.append(self)
        
        self.setUI()
        self.setFile(file)
        
    def setUI(self):
        mv = QVBoxLayout()
        h = QHBoxLayout()
        
        #----------------logo-------------
        logo_frm = QFrame()
        logo_frm.setObjectName("")
        logo_frm.setMaximumWidth(120)
        logo_mv = QVBoxLayout()
        logo_h = QHBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("plogo")
        self.logo.resize(100,100)
        
        logo_h.addWidget(self.logo)
        logo_mv.addLayout(logo_h)
        logo_frm.setLayout(logo_mv)
        #----------------logo-------------
        h.addWidget(logo_frm)
        #---------------------------------------
        cizgi1 = QFrame()
        cizgi1.setFrameShape(QFrame.VLine)
        #---------------------------------------
        h.addWidget(cizgi1)
        #-------------------------------------------info-------------
        info_v = QVBoxLayout()
        #---------header-------
        header_h = QHBoxLayout()
        
        self.name = QLabel()
        
        self.rename = QPushButton()
        self.rename.setObjectName("rename")
        self.rename.setIcon(QIcon("image/edit2.png"))
        self.rename.setIconSize(QSize(25,25))
        self.rename.setMinimumSize(30,30)
        self.rename.setMaximumSize(30,30)
        self.rename.setCursor(QCursor(Qt.PointingHandCursor))
        
        header_h.addWidget(self.name)
        header_h.addWidget(self.rename)
        #---------header-------
        info_v.addLayout(header_h)
        #---------path--------
        self.path = QLabel()
        self.path.setObjectName("filefrpath")
        #--------path-------
        info_v.addWidget(self.path)
        #----------btn--------------
        menu_h = QHBoxLayout()
        
        self.delet = QPushButton()
        self.delet.setObjectName("dizinbtn")
        self.delet.setIcon(QIcon("image/delete.png"))
        self.delet.setIconSize(QSize(40,40))
        self.delet.setMinimumSize(45,45)
        self.delet.setMaximumSize(45,45)
        self.delet.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.openfolder = QPushButton()
        self.openfolder.setObjectName("dizinbtn")
        self.openfolder.setIcon(QIcon("image/folder.png"))
        self.openfolder.setIconSize(QSize(35,35))
        self.openfolder.setMinimumSize(45,45)
        self.openfolder.setMaximumSize(45,45)
        self.openfolder.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.edit = QPushButton()
        self.edit.setObjectName("dizinbtn")
        self.edit.setIcon(QIcon("image/edit.png"))
        self.edit.setIconSize(QSize(35,35))
        self.edit.setMinimumSize(45,45)
        self.edit.setMaximumSize(45,45)
        self.edit.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.open = QPushButton()
        self.open.setObjectName("dizinbtn")
        self.open.setIcon(QIcon("image/open.png"))
        self.open.setIconSize(QSize(35,35))
        self.open.setMinimumSize(45,45)
        self.open.setMaximumSize(45,45)
        self.open.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.execrun = QPushButton()
        self.execrun.setObjectName("dizinbtn")
        self.execrun.setIcon(QIcon("image/console2.png"))
        self.execrun.setIconSize(QSize(35,35))
        self.execrun.setMinimumSize(45,45)
        self.execrun.setMaximumSize(45,45)
        self.execrun.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        self.set_btn = QPushButton()
        self.set_btn.setObjectName("dizinbtn")
        self.set_btn.setIcon(QIcon("image/right-arrow.png"))
        self.set_btn.setIconSize(QSize(35,35))
        self.set_btn.setMinimumSize(45,45)
        self.set_btn.setMaximumSize(45,45)
        self.set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.set_btn.clicked.connect(self.yonetim)
        
        menu_h.addWidget(self.delet)
        menu_h.addWidget(self.openfolder)
        menu_h.addWidget(self.edit)
        menu_h.addWidget(self.open)
        menu_h.addWidget(self.execrun)
        menu_h.addStretch()
        menu_h.addWidget(self.set_btn)
        #----------btn--------------
        info_v.addLayout(menu_h)
        #-------------------------------------------info-------------
        
        
        
        h.addLayout(info_v)
        mv.addLayout(h)
        self.setLayout(mv)
        
    
    def setFile(self, file):
        self.file = os.path.abspath(file)
        name, ext = os.path.splitext(self.file)
        if ext == ".py":
            pix = QPixmap("image/python-logo.png")
            self.open.setVisible(False)

        elif ext == ".css":
            pix = QPixmap("image/css-logo.png")
            self.execrun.setVisible(False)
            self.open.setVisible(False)
        
        elif ext == ".html":
            pix = QPixmap("image/html-logo.png")
            self.execrun.setVisible(False)
        
        elif ext == ".c":
            pix = QPixmap("image/file/c-logo.png")
            self.open.setVisible(False)
        
        elif ext == ".cpp":
            pix = QPixmap("image/file/cpp-logo.png")
            self.open.setVisible(False)
        
        elif ext == ".cs":
            pix = QPixmap("image/file/csharp-logo.png")
            self.open.setVisible(False)
        
        elif ext == ".h":
            pix = QPixmap("image/file/ccpph-logo.png")
            self.open.setVisible(False)
            self.execrun.setVisible(False)
        
        elif ext == ".exe":
            pix = QPixmap("image/file/exe-logo.png")
            self.execrun.setVisible(False)
            self.edit.setVisible(False)
            
        elif ext == ".java" or ext == ".jar":
            pix = QPixmap("image/file/java-logo.png")
            self.open.setVisible(False)
        
        elif ext in [".db",".sql",".dbs"]:
            pix = QPixmap("image/database-logo.png")
            self.execrun.setVisible(False)
            self.open.setVisible(False)

        elif ext == ".json":
            pix = QPixmap("image/file/json-logo.png")
            self.execrun.setVisible(False)
            self.open.setVisible(False)

        elif ext == ".xml":
            pix = QPixmap("image/file/xml-logo.png")
            self.execrun.setVisible(False)
            self.open.setVisible(False)

        elif ext == ".txt":
            pix = QPixmap("image/text-logo.png")
            self.execrun.setVisible(False)
            self.open.setVisible(False)

        elif ext in [".png",".jpg",".gif",".tiff"]:
            pix = QPixmap("image/image-logo.png")
            self.execrun.setVisible(False)
            self.edit.setVisible(False)

        else:
            pix = QPixmap("image/script-logo.png")
            self.execrun.setVisible(False)
            self.edit.setVisible(False)
            
        pix = pix.scaled(QSize(75,75))    
        self.logo.setPixmap(pix)
        self.name.setText(os.path.split(file)[1])
        self.path.setText(os.path.abspath(file))

    
    def yonetim(self):
        DetayWidget.liste[0].setFile(self.file)
        





class DetayWidget(QWidget):
    liste = list()
    menu_state = False
    def __init__(self):
        super().__init__()
        self.liste.append(self)
        
        self.setUI()
        
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        #----------header-------------
        header_h = QHBoxLayout()
        
        self.back = QPushButton()
        self.back.setObjectName("dizinbtn")
        self.back.setIcon(QIcon("image/left-arrow.png"))
        self.back.setIconSize(QSize(40,40))
        self.back.setMinimumSize(50,50)
        self.back.setMaximumSize(50,50)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.clicked.connect(self.__back)
        
        yonetim_lbl = QLabel("Yönetim")
        yonetim_lbl.setObjectName("yonetim_lbl")
        yonetim_lbl.setAlignment(Qt.AlignCenter)
        
        header_h.addWidget(self.back)
        header_h.addWidget(yonetim_lbl)
        #--------------header-----------
        v.addLayout(header_h)
        #---------------------
        cizgi1 = QFrame()
        cizgi1.setFrameShape(QFrame.HLine)
        #------------------------
        v.addWidget(cizgi1)
        #------------------------------bolum11111-------------
        bolum1_mv = QVBoxLayout()
        
        name_h = QHBoxLayout()
        self.name = QLabel("main.py")
        self.name.setObjectName("yonetim_name")
        
        self.prefmain = MainPrefM()
        self.prefmain.setVisible(True)
        
        name_h.addWidget(self.name)
        name_h.addWidget(self.prefmain)
        bolum1_mv.addLayout(name_h)
        
        
        self.path = QLabel()
        bolum1_mv.addWidget(self.path)
        self.path.setObjectName("filepath")
        
        
        pref_h = QHBoxLayout()
        self.prefext = ExtPref()
        self.prefsize = SizePref()
        
        pref_h.addWidget(self.prefext)
        pref_h.addWidget(self.prefsize)
        pref_h.addStretch()
        bolum1_mv.addLayout(pref_h)
        
        if os.name == "nt":
            self.olust = QLabel("Oluşturulma Tarihi: ")
            bolum1_mv.addWidget(self.olust)
        self.duzent = QLabel("Son Düzenleme Tarihi: ")
        bolum1_mv.addWidget(self.duzent)
        #------------------------------bolum11111-------------
        v.addLayout(bolum1_mv)
        #---------------------
        cizgi2 = QFrame()
        cizgi2.setFrameShape(QFrame.HLine)
        #------------------------
        v.addWidget(cizgi2)
        #---------------------------içerik----------
        self.icerik = FileContent()
        #------------------------------içerik------------
        v.addWidget(self.icerik)
        #-----------------------------alt menu btn------------
        menu_btn_h = QHBoxLayout()
        
        self.onoff = QPushButton()
        self.onoff.setObjectName("onoff")
        self.onoff.setIcon(QIcon("image/up-arrow.png"))
        self.onoff.setIconSize(QSize(20,20))
        self.onoff.setMinimumSize(25,25)
        self.onoff.setMaximumSize(25,25)
        self.onoff.setCursor(QCursor(Qt.PointingHandCursor))
        self.onoff.clicked.connect(self.__onoff)
        
        menu_btn_h.addStretch()
        menu_btn_h.addWidget(self.onoff)
        #-----------------------------alt menu btn------------
        v.addLayout(menu_btn_h)
        #---------------------
        cizgi3 = QFrame()
        cizgi3.setFrameShape(QFrame.HLine)
        #------------------------
        v.addWidget(cizgi3)
        #------------------------------menu----------------
        menu_l = QGridLayout()
        
        self.btnDelete = BtnSil()
        self.btnAdlandır = BtnAdlandır()
        
        self.btnDelete.setVisible(False)
        self.btnAdlandır.setVisible(False)
        
        self.btnKlasor = BtnKlasor()
        self.btnAc = BtnAc()
        self.btnCalistir = BtnCalistir()
        
        menu_l.addWidget(self.btnDelete, 1,1)
        menu_l.addWidget(self.btnAdlandır, 1,3)
        
        menu_l.addWidget(self.btnKlasor, 2,1)
        menu_l.addWidget(self.btnCalistir, 2,2)
        menu_l.addWidget(self.btnAc, 2,3)
        #------------------------------menu----------------
        v.addLayout(menu_l)
        
        
        mh.addLayout(v)
        self.setLayout(mh)
    
    def __onoff(self):
        if self.menu_state == False:
            self.btnDelete.setVisible(True)
            self.btnAdlandır.setVisible(True)
            self.onoff.setIcon(QIcon("image/down-arrow.png"))
            self.menu_state = True
        else:
            self.btnDelete.setVisible(False)
            self.btnAdlandır.setVisible(False)
            self.onoff.setIcon(QIcon("image/up-arrow.png"))
            self.menu_state = False
    
    
    def __back(self):
        SagFrame.liste[0].setCurrentIndex(0)
        
    
    def setFile(self, file):
        a = os.path.split(file)[1].split(".")[1]
        if a in ["py","cpp","c","java","cs","exe"]:
            self.btnCalistir.setVisible(True)
        else:
            self.btnCalistir.setVisible(False)
        
        SagFrame.liste[0].setCurrentIndex(1)
        self.name.setText(os.path.split(file)[1])
        self.path.setText(file)
        
        self.prefext.setFile(file)
        self.prefsize.setFile(file)
        
        dosya = os.stat(file)
        o = datetime.datetime.fromtimestamp(dosya.st_ctime)
        d = datetime.datetime.fromtimestamp(dosya.st_mtime)
        
        ot = str(datetime.datetime.strftime(o,"%c"))
        dt = str(datetime.datetime.strftime(d,"%c"))
        
        if os.name == "nt":
            self.olust.setText("Oluşturulma Tarihi: " + ot)
        self.duzent.setText("Son Düzenleme Tarihi: " + dt)
        
        self.icerik.setFile(file)
        
        self.btnDelete.setFile(file)
        self.btnAdlandır.setFile(file)
        self.btnKlasor.setFile(file)
        self.btnAc.setFile(file)
        self.btnCalistir.setFile(file)
