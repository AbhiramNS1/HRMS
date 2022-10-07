
from PyQt5.QtWidgets import QWidget,QGraphicsDropShadowEffect
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class ProgressIndicator(QWidget):
    def __init__(self):
        QWidget.__init__(self)
       
        self.value=40
        self.width=200
        self.height=200
        self.progress_width=10
        self.progress_roundcap=True
        self.progress_color=0xff2052
        self.max_value=100
        self.suffix="%"
        self.enable_shadow=True
        self.shadow=QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(35)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,190))
        self.setGraphicsEffect(self.shadow)
        self.setFont(QFont("Helvetica",20))
        self.userText=None
    def paintEvent(self,event):
        width=self.width-self.progress_width
        height=self.height-self.progress_width
        margin=int(self.progress_width/2)
        value=self.value*360 / self.max_value
  
        painter=QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect=QRect(0,0,self.width,self.height)
        painter.setPen(Qt.NoPen)
        painter.drawRect(rect)

        pen=QPen()
        # clr=QColor(0x000000)
        # clr.setAlphaF(0.1)
        # pen.setColor(clr)
        # pen.setWidth(self.progress_width+20)
        # pen.setCapStyle(Qt.RoundCap)
        # painter.setPen(pen)
        # painter.drawArc(margin,margin,height,width,0,360*16)


        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        pen.setCapStyle(Qt.RoundCap)

        painter.setPen(pen)
        painter.drawArc(margin,margin,height,width,-90*16,int(-value*16))

        pen.setColor(QColor(self.progress_color))
        # pen.setWidth(self.progress_width+20)
        # pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        painter.drawText(rect,Qt.AlignCenter,f"{self.value}{self.suffix}")

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
 
