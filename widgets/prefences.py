from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

class MainPref(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(80,80)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/run.png")
        pix = pix.scaled(QSize(25,25))
        logo.setPixmap(pix)
        logo.resize(25,25)
        
        lbl = QLabel("main")
        lbl.setAlignment(Qt.AlignCenter)
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)


class MainPrefM(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(50,50)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        logo = QLabel()
        logo.setAlignment(Qt.AlignCenter)
        logo.setObjectName("preflogo")
        pix = QPixmap("image/run.png")
        pix = pix.scaled(QSize(15,15))
        logo.setPixmap(pix)
        logo.resize(20,20)
        
        lbl = QLabel("main")
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setObjectName("pmenum")
        
        v.addWidget(logo)
        v.addWidget(lbl)
        
        self.setLayout(v)



class ExtPref(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(80,80)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        self.logo = QLabel()
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setObjectName("preflogo")
        
        self.logo.resize(50,50)
        
        self.lbl = QLabel("python")
        self.lbl.setObjectName("preflbl")
        self.lbl.setAlignment(Qt.AlignCenter)
        
        v.addWidget(self.logo)
        v.addWidget(self.lbl)
        
        self.setLayout(v)
        
    def setFile(self,file):
        ext = os.path.split(file)[1].split(".")[1]
        if ext == "py":
            pix = QPixmap("image/python-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("python")
        
        elif ext == "css":
            pix = QPixmap("image/css-logo.png")
            pix = pix.scaled(QSize(29,29))
            self.logo.setPixmap(pix)
            self.lbl.setText("css")
            
        elif ext == "html":
            pix = QPixmap("image/html-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("html")
        
        elif ext == "c":
            pix = QPixmap("image/file/c-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c")
        
        elif ext == "cpp":
            pix = QPixmap("image/file/cpp-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c++")
        
        elif ext == "cs":
            pix = QPixmap("image/file/csharp-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("c-sharp")
        
        elif ext == "h":
            pix = QPixmap("image/file/ccpph-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("header")
        
        elif ext == "exe":
            pix = QPixmap("image/file/exe-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("executable")
            
        elif ext == "java" or ext == "jar":
            pix = QPixmap("image/file/java-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.open.setVisible(False)
        
        elif ext in ["db","sql","dbs"]:
            pix = QPixmap("image/database-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("database")
            
        elif ext == "json":
            pix = QPixmap("image/file/json-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("json")
        
        elif ext == "xml":
            pix = QPixmap("image/file/xml-logo.png")
            pix = pix.scaled(QSize(40,40))
            self.logo.setPixmap(pix)
            self.lbl.setText("xml")
        
        elif ext == "txt":
            pix = QPixmap("image/text-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("text")
        
        elif ext in ["png","jpg","gif","tiff"]:
            pix = QPixmap("image/image-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("resim")
        
        else:
            pix = QPixmap("image/script-logo.png")
            pix = pix.scaled(QSize(25,25))
            self.logo.setPixmap(pix)
            self.lbl.setText("özel")

        
class SizePref(QFrame):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(80,80)
        self.setObjectName("preffr")
        v = QVBoxLayout()
        
        self.size = QLabel()
        self.size.setAlignment(Qt.AlignCenter)
        self.size.setObjectName("sizelbl")

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        
        v.addWidget(self.size)
        v.addWidget(self.lbl)
        
        self.setLayout(v)
    
    
    def setFile(self,file):
        s = ConvertSize(os.path.getsize(file))
        s = s.get()
        
        try:
            self.size.setText(str(s[0])[0:5])
        except:
            self.size.setText(str(s[0]))
            
        self.lbl.setText(s[1])


class ConvertSize():
    l = list()
    def __init__(self,b):
        self.l.clear()
        if b < 1024:
            self.l.append(b)
            self.l.append('b')

        elif b >= 1024 and b < 1048576:
            self.l.append(b/1024)
            self.l.append('kb')
        
        elif b >= 1048576 and b < 1073741824:
            self.l.append(b/1024/1024)
            self.l.append('mb')
            
        elif b >= 1073741824 and b < 1099511627776:
            self.l.append(b/1024/1024/1024)
            self.l.append('gb')

    def get(self):
        return self.l


