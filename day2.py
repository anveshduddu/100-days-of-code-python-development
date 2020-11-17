# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 01:39:44 2020

@author: anves
"""


import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
 
 
 
 
app = QApplication(sys.argv)
 
web = QWebEngineView()
 
web.load(QUrl("https://www.anvesh.tk"))
 
web.show()
 
 
sys.exit(app.exec_())