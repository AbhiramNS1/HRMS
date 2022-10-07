from turtle import heading
from typing import List
from PyQt5 import QtWidgets as qw
import PyQt5.QtGui as gui

class Table(qw.QFrame):
    def __init__(self,heading=None,headingsList=None):
        super().__init__()

        self.setObjectName('parent')
        self.setStyleSheet('''
        QFrame#parent{
            background-color:#dddddd
        }
        QFrame#table{
            border:1px solid black;
           
        }
        ''')
        widgetLayout=qw.QVBoxLayout()
        if(heading):
            head=qw.QLabel(heading)
            # head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            head.setFont(gui.QFont('Helvatica',15))
            widgetLayout.addWidget(head)
       

        self.table=qw.QFrame()
        # self.table.setContentsMargins(0,0,0,0)
       
        self.tableLayout=qw.QVBoxLayout()
        self.tableLayout.setContentsMargins(0,0,0,0)
        self.tableLayout.setSpacing(0)
        self.table.setObjectName('table')
        self.tableLayout.addWidget(self.Headings(headingsList))
        self.table.setLayout(self.tableLayout)
        
        widgetLayout.addWidget(self.table)
        self.setLayout(widgetLayout)
    #add a row to the table
    def __lt__(self,datsList:List):
        row=qw.QFrame()
        rowl=qw.QHBoxLayout()
        rowl.setContentsMargins(6,6,6,6)
        for i in datsList:
            label=qw.QLabel(i)
            label.setFont(gui.QFont('Helvetica',10))
            label.setStyleSheet('color:#404040;padding:10px')
            rowl.addWidget(label)
        row.setLayout(rowl)
        row.setStyleSheet('''
            QFrame#ele{
                border-top:1px solid red;
                background-color:#bfbfbf;
                }
            ''')
        row.setObjectName('ele')
        self.table.layout().addWidget(row)
  

    def Headings(self,headings):
        header=qw.QFrame()
        headl=qw.QHBoxLayout()
     
        for i in headings:
            label=qw.QLabel(i)
            font=gui.QFont('Helvetica',15)
            font.setBold(True)
            label.setFont(font)
            headl.addWidget(label)
        header.setLayout(headl)

        return header
    
