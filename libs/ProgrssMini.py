
from PyQt5.QtWidgets import QFrame,QGraphicsDropShadowEffect
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class ProgressIndicatorMini(QFrame):
    def __init__(self,color='orange',height=180,width=180,value=40,shadow=None):
        QFrame.__init__(self)
       
        self.value=value
        self.width=height
        self.height=width
        self.progress_width=10
        self.progress_roundcap=True
        self.progress_color=color
        self.max_value=100
        self.suffix="%"
        self.enable_shadow=True
        if(shadow):self.setGraphicsEffect(shadow)
        self.setFont(QFont("Helvetica",20))
        self.userText=None
        self.setStyleSheet("background-color:red")

        
    def paintEvent(self,event):
        width=self.width-self.progress_width
        height=self.height-self.progress_width
        margin=int(self.progress_width/2)+40
        value=self.value*360 / self.max_value
        painter=QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect=QRect(0,0,self.width+20,self.height+20)
       
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

        pen=QPen()
        clr=QColor(0x000000)
        clr.setAlphaF(0.1)
        pen.setColor(clr)
        pen.setWidth(self.progress_width+10)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawArc(margin,margin-30,height,width,0,360*16)


        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        pen.setCapStyle(Qt.RoundCap)

        painter.setPen(pen)
        painter.drawArc(margin,margin-30,height,width,90*16,int(-value*16))

        pen.setColor(QColor(self.progress_color))
        # pen.setWidth(self.progress_width+20)
        # pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawText(QPointF(width/2+10,height/2+30),f"{self.value}{self.suffix}")

        if(self.userText):
            pen.setColor(QColor(0x0))
            self.setFont(QFont("times",13))
            painter.setPen(pen)
            painter.drawText(self.textX,230,self.userText)
        


        painter.end()

    def setProgress(self,value):
        self.value=value
        self.repaint()
    def setText(self,text,x,y=230):
        self.textX=x
        self.userText=text
 
