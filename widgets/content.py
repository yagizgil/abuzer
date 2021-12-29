from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os,sys
import xml.etree.ElementTree as et
import json

import sqlite3 as sql




class ContentFile(QFrame):
    state = False
    liste = list()
    a_etiket = ""
    a_olust = ""
    a_degist = ""
    
    detay = ""
    def __init__(self,  file):
        super().__init__()
        self.file = file
        self.setObjectName("af")
        self.liste.append(self)
        
        self.setUI()
        self.setFile()
        
    def setUI(self):
        v = QVBoxLayout()
        h = QHBoxLayout()
        
        
        #-------------------------------------logo---------------------------
        logo_frm = QFrame()
        logo_frm.setFixedSize(150,80)
        logo_frm.setStyleSheet("QFrame {border: none;}")
        content_v = QVBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("contentlogo")
        
        self.logo.resize(25,25)
        
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        
        content_v.addWidget(self.logo)
        content_v.addWidget(self.lbl)
        logo_frm.setLayout(content_v)
        #--------------------------------logo----------------------
        h.addWidget(logo_frm)
        #-------------------------------header-------------
        self.header = QLabel()
        #------------------------------header--------------------
        h.addWidget(self.header)
        #--------------------------------set----------
        set_v = QVBoxLayout()
        
        self.set_btn = QPushButton()
        self.set_btn.setObjectName("set_btn")
        self.set_btn.setIcon(QIcon("image/right-arrow.png"))
        self.set_btn.setIconSize(QSize(40,40))
        self.set_btn.setMinimumSize(50,50)
        self.set_btn.setMaximumSize(50,50)
        self.set_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.set_btn.clicked.connect(self.__setDetay)
        
        set_v.addWidget(self.set_btn)
        #----------------------------set----------------------
        h.addLayout(set_v)
        
        v.addLayout(h)
        self.setLayout(v)
    
    
    def setDetayWidget(self, d):
        self.detay = d
    
    def setFile(self):
        ext = self.file.split(".")[1]
        if ext == "css":
            pix = QPixmap("image/css-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("stylesheet")
            
        self.header.setText(self.file)
    
    def __setDetay(self):
        self.detay.setFile(self.file)
   


class FileContent(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setObjectName("filecontent")
        
        self.setUI()
        
    def setUI(self):
        self.fpyw = pyw()
        self.fcssw = cssw()
        self.fdbw = dbw()
        self.fjsnw = jsnw()
        self.fxmlw = xmlw()
        self.ftxtw = txtw()
    
    def setFile(self, file):
        ext = file.split(".")[1]
        self.setUI()
        if ext == "py":
            self.setCentralWidget(self.fpyw)
            self.fpyw.t.setFile(file)
        
        if ext == "css":
            self.setCentralWidget(self.fcssw)
            self.fcssw.t.setFile(file)
        
        if ext in ["db","sql","dbs"]:
            self.setCentralWidget(self.fdbw)
            self.fdbw.t.setFile(file)
        
        if ext == "json":
            self.setCentralWidget(self.fjsnw)
            self.fjsnw.t.setFile(file)
        
        if ext == "xml":
            self.setCentralWidget(self.fxmlw)
            self.fxmlw.t.setFile(file)
        
        if ext == "txt":
            self.setCentralWidget(self.ftxtw)
            self.ftxtw.t.setFile(file)
        

    
class pyw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = PyTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)

class cssw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = CssTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)
        
class dbw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = DbTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)

class jsnw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = JsnTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)
        
class xmlw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = XmlTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)
        
class txtw(QWidget):
    
    def __init__(self):
        super().__init__()
        h = QHBoxLayout()
        v = QVBoxLayout()
        
        self.t = TxtTree()
        v.addWidget(self.t)
        
        h.addLayout(v)
        self.setLayout(h)
        




class PyTree(QTreeWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setHeaderLabels([""])
        self.header().hide()

    
    def setFile(self,file):
        self.clear()
        self.moduls = QTreeWidgetItem(self,["Kütüphaneler"])
        self.classs = QTreeWidgetItem(self,["Sınıflar"])
        self.defs = QTreeWidgetItem(self,["Fonksiyonlar"])
        self.veriables = QTreeWidgetItem(self,["Değişkenler"])
        
        with open(file,"r") as f:
            a = f.readlines()
            
            for i in a:
                if "import " in i:
                    if "(" not in i and ":" not in i and '"' not in i and "'" not in i:
                        QTreeWidgetItem(self.moduls,[i])
            
            for i in a:
                if "class" in i:
                    if i.strip()[0:5] == "class":
                        if "(" in i and "):" in i:
                            tw = QTreeWidgetItem(self.classs,[i.split("(")[0].split(" ")[1].strip()])
                        elif str(i.split(" ")[1][::1]) + ":" in i:
                            tw = QTreeWidgetItem(self.classs,[i.split(" ")[1][::1].strip()])
                             
            
            for i in a:
                if "def" in i:
                    if i.strip()[0:3] == "def":
                        if "(" in i:
                            QTreeWidgetItem(self.defs,[i.split("(")[0]])
                        else:
                            QTreeWidgetItem(self.defs,[i.split(" ")[1][::1]])
            
            for i in a:
                if "if" not in i or "elif" not in i:
                    if "==" not in i and "!=" not in i and "<=" not in i and ">=" not in i:
                        if "=" in i:
                            if i[i.index("=")-1] != '"' and i[i.index("=")+1] != '"':
                                QTreeWidgetItem(self.veriables,[i.split("=")[0].strip()])
        
        
class CssTree(QTreeWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setHeaderLabels([""])
        self.header().hide()
    
    def setFile(self,file):
        self.clear()
        
        with open(file, "r") as f:
            a = f.read()
            l = a.split("\n")
        
        for i in l:  
            if i.startswith("  "):
                QTreeWidgetItem(tw,[i.replace("}", "").replace("{", "")])
            else:
                if i != "" and i != "\n" and i != " " and i.isspace() == False:
                    
                    tw = QTreeWidgetItem(self,[i.replace("}", "").replace("{", "")])
                      
    
class DbTree(QTreeWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setHeaderLabels(["Kolon Adı","Kolon Türü"])
    
    def setFile(self, file):
        self.clear()
        
        try:
            vt = sql.connect(file)
            im = vt.cursor()
            
            im.execute("SELECT * FROM sqlite_master WHERE type = 'table'")
            datas = list()
            for i in im.fetchall():
                datas.append(list(i))
            
            for i in datas:
                tw = QTreeWidgetItem(self,[i[1]])
                for j in i[4].splitlines():
                    if "CREATE TABLE" not in j and j != ")":
                        a = j.rsplit('"')
                        QTreeWidgetItem(tw,[a[1],a[2].strip().replace(",","")])
        
        except Exception as ex:
            print(ex)
            
        

class JsnTree(QTreeWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setHeaderLabels([""])
        self.header().hide()
    
    def setFile(self,file):
        self.clear()
        
        def fill_item(item, value):
            def new_item(parent, text, val=None):
                child = QTreeWidgetItem([text])
                child.setFlags(child.flags())
                fill_item(child, val)
                parent.addChild(child)
                child.setExpanded(True)
            
            if value is None: return
            
            elif isinstance(value, dict):
                for key, val in sorted(value.items()):
                    new_item(item, str(key), val)
            
            elif isinstance(value, (list, tuple)):
                for val in value:
                    text = (str(val) if not isinstance(val, (dict, list, tuple))
                            else '[%s]' % type(val).__name__)
                    new_item(item, text, val)
            else:
                new_item(item, str(value))
        
        val=json.load(open(file,"r"))
        fill_item(self.invisibleRootItem(), val)
            
    
class XmlTree(QTreeWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setHeaderLabels([""])
        self.header().hide()
    
    def setFile(self,file):
        self.clear()
        
        with open(file, "r") as f:
            tree = et.fromstring(f.read())
        
        a = QTreeWidgetItem([tree.tag])
        self.addTopLevelItem(a)
        
        def displayTree(a,s):
            for child in s:
                branch = QTreeWidgetItem([child.tag])
                a.addChild(branch)
                displayTree(branch, child)
            
            if s.text is not None:
                content = s.text
                a.addChild(QTreeWidgetItem([content]))
            
            
        displayTree(a, tree)
    
    
class TxtTree(QTextEdit):
    
    def __init__(self):
        super().__init__()
        
    def setFile(self,file):
        a = open(file,"r").read()
        self.setText(a)
        self.setReadOnly(True)
    
