# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys,os

class AyarProje(QWidget):
    
    def __init__(self, me):
        super().__init__()
        self.me = me
        self.setStyleSheet(open("style/ayar.css").read())

        self.setUI()

    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        sp = QSplitter(Qt.Horizontal)
            
        self.cikti = Cikti()
        
        
        sp.addWidget(self.cikti)
        
        
        v.addWidget(sp)
        h.addLayout(v)
        self.setLayout(h)
    

class Cikti(QTabWidget):
    
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        
        self.setUI()
        
    
    def setUI(self):
        self.exe = Executable()
        self.archiv = Archieve()
        
        self.addTab(self.exe, "Çalıştırabilir Dosya Çıktısı")
        self.addTab(self.archiv, "Arşiv")


class Executable(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setUI()
    
    def setUI(self):
        mh = QHBoxLayout()
        v = QVBoxLayout()
        
        #----------çalıştırılacak dosya------------------
        file_f = QFormLayout()
        
        self.file_to_exe = QComboBox()
        self.file_to_exe.addItems(["main.py","exec.py","dfgjddgf.py"])
        
        file_f.addRow(QLabel("Çıktısı Alınacak Dosya: "), self.file_to_exe)
        #----------çalıştırılacak dosya------------------
        v.addLayout(file_f)
        #----------------------not---------------
        not1_h = QHBoxLayout()
        not1 = QLabel("(Uygulamanın tam .exe uzantılı çıktısı için main dosyası standart olarak ayarlandı.)")
        not1.setObjectName("not1")
        not1_h.addStretch()
        not1_h.addWidget(not1)
        #----------------------not---------------
        v.addLayout(not1_h)
        #------------------------------------------------------------------------------
        icerik_v = QVBoxLayout()
        
        self.picon = QCheckBox("İkon")
        self.picon.setFixedSize(250,40)
        self.picon.setCursor(QCursor(Qt.PointingHandCursor))
        
        picon_h = QHBoxLayout()
        self.picon_path = QLineEdit()
        self.picon_path.setMinimumHeight(38)
        
        self.picon_path_btn = QPushButton()
        self.picon_path_btn.setObjectName("path_btn")
        self.picon_path_btn.setIcon(QIcon("image/folder.png"))
        self.picon_path_btn.setIconSize(QSize(35,35))
        self.picon_path_btn.setFixedSize(40,40)
        self.picon_path_btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        picon_h.addWidget(self.picon)
        picon_h.addWidget(self.picon_path)
        picon_h.addWidget(self.picon_path_btn)
        
        
        self.poffconcole = QCheckBox("Konsolu Kapat")
        self.poffconcole.setFixedSize(250,40)
        self.poffconcole.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.ponefile = QCheckBox("Tek Dosya")
        self.ponefile.setFixedSize(250,40)
        self.ponefile.setCursor(QCursor(Qt.PointingHandCursor))
        
        
        
        
        icerik_v.addLayout(picon_h)
        icerik_v.addWidget(self.poffconcole)
        icerik_v.addWidget(self.ponefile)
        #------------------------------------------------------------------------------
        v.addLayout(icerik_v)
        #----------------------------çıktı konumu-------
        ckonum_h = QHBoxLayout()
        
        self.konum = QLineEdit()
        self.konum.setMinimumHeight(38)
        
        self.konum_btn = QPushButton()
        self.konum_btn.setObjectName("path_btn")
        self.konum_btn.setIcon(QIcon("image/folder.png"))
        self.konum_btn.setIconSize(QSize(35,35))
        self.konum_btn.setFixedSize(40,40)
        self.konum_btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        ckonum_h.addWidget(QLabel("Çıktı Konumu: "))
        ckonum_h.addWidget(self.konum)
        ckonum_h.addWidget(self.konum_btn)
        #----------------------------çıktı konumu-------
        v.addLayout(ckonum_h)
        #----------------not----------
        not2 = QLabel("Uygulamada tanımlı olan; veritabanları, medyalar gibi python dosyası hariç dosyaları çıktının yanında barındırın.")
        not2.setWordWrap(True)
        not2.setAlignment(Qt.AlignCenter)
        #----------------not----------
        v.addWidget(not2)
        #-----------------------filetreee-------------
        file_group = QGroupBox("Çıktı Yanına Kopyalanacak Öğeler")
        file_mv = QVBoxLayout()
        file_h = QHBoxLayout()
        
        self.filetree = FileTree(os.getcwd(),self)
        
        file_h.addWidget(self.filetree)
        
        file_mv.addLayout(file_h)
        file_group.setLayout(file_mv)
        #-----------------------filetreee-------------
        #v.addWidget(file_group)
        #---------------------btn--------------
        btn_h = QHBoxLayout()
        
        self.btn = QPushButton("Çıktıyı Al")
        self.btn.setObjectName("cikti_btn")
        self.btn.setFixedHeight(35)
        self.btn.setMaximumWidth(250)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        
        #btn_h.addStretch()
        btn_h.addWidget(self.btn)
        #---------------------btn--------------
        v.addLayout(btn_h)
        
        
        
        mh.addLayout(v)
        self.setLayout(mh)
        


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
        











class Archieve(QWidget):
    
    def __init__(self):
        super().__init__()











