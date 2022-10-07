


import PyQt5.QtWidgets as qw
import PyQt5.QtGui as gui
import PyQt5.QtCore
from libs.Auth import deleteToken
from libs.BasicWidets import Spacer
from libs.CircularProgressIndicator import ProgressIndicator

from libs.Assets import resource
from libs.ProgrssMini import ProgressIndicatorMini
from libs.Table import Table
class Main(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.currentHomeWidget=None
        self.setWindowTitle('HRMS')
        self.setWindowIcon(gui.QIcon(resource('assets/logo.png')))
        self.setLayout(qw.QVBoxLayout())
        self.setMinimumSize(1340,800)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0,0,0,0) #making the default margin to 0
        self.layout().addWidget(self.CreateTopBar())

        mainFrame=qw.QFrame()
        mainFrame.setLayout(qw.QHBoxLayout())
        mainFrame.layout().setContentsMargins(0,0,0,0)
        mainFrame.layout().setSpacing(0)
        mainFrame.layout().addWidget(self.SideNavPanel(),1)
        mainFrame.layout().addWidget(self.HomePanel(),3)
        self.currentHomeWidget=self.DashBoard()
        self.homePanel.layout().addWidget(self.currentHomeWidget)

        self.layout().addWidget(mainFrame)



        self.show()
    def CreateTopBar(self):
        TopBar=qw.QFrame()
        TopBar.setFixedHeight(80)
        layout=qw.QHBoxLayout()
        

        #adding icon 
        icon=gui.QPixmap(resource('assets/logo.png'))
        icon=icon.scaled(60,60)
        label=qw.QLabel()
        label.setPixmap(icon)
        label.setStyleSheet("margin-left:20px")
        layout.addWidget(label)

        heading =qw.QLabel('HRMS')
        heading.setFont(gui.QFont("Helvatica",20))
        layout.addWidget(heading)
        heading.setStyleSheet("margin-left:7px")

        layout.addStretch()

        Image=gui.QPixmap(resource('admin.jpg'))
        Image=Image.scaled(50,50)
        imagelabel=qw.QLabel()
        imagelabel.setPixmap(Image)
        email=qw.QLabel('hrmsadmin@techtok4u.com')
        email.setStyleSheet('margin-right:20px')
        email.setFont(gui.QFont("Helvatica",10))
        layout.addWidget(imagelabel)
        layout.addWidget(email)
        logout=qw.QPushButton('logout')
        layout.addWidget(logout)
        def SignOut():
            deleteToken()
            self.close()
            global WINDOW
            from src.Login import Login
            WINDOW = Login()

        logout.clicked.connect(SignOut)
        TopBar.setStyleSheet("""
        QFrame{
            background-color:#D9D9D9;
        }
        """)
        TopBar.setLayout(layout)
        return TopBar
    def SideNavPanel(self):
        def Element(icon:str,text:str,onClick=None):
            button=qw.QPushButton('   '+text)
            button.setIcon(gui.QIcon(resource('assets/'+icon)))
            button.setIconSize(PyQt5.QtCore.QSize(35,35))
            button.setStyleSheet("""
            QPushButton{
                background-color:#0085FF;
                height:60;
                border:none;
                color:white;
                text-align:left;
                padding-left:20px;
                font-size:21px;
                font-weight:300;
                line-height:100;
            }
            QPushButton:hover{
                background-color:#0065C2;
            }
            """)
            if(onClick):
                def run():
                    if(self.currentHomeWidget):self.homePanel.layout().removeWidget(self.currentHomeWidget)
                    onClick()
                button.clicked.connect(run)
            return button
        panel=qw.QFrame()
        
        layout=qw.QVBoxLayout()
        layout.setSpacing(0)
        
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(Element('dashboard.png','Dashboard',self.DashBoard))
        layout.addWidget(Element('account_box.png','Attendence',self.Emp_Attendence))
        layout.addWidget(Element('settings.png','Settings'))
        layout.addWidget(Element('messages.png','Messages'))

        spacer=qw.QFrame()
        spacer.setLayout(qw.QHBoxLayout())
        textlabel=qw.QLabel('Admin')
        textlabel.setFont(gui.QFont("Helvatica",13))
        spacer.layout().addWidget(textlabel)
        spacer.setStyleSheet('background-color:black;color:white;height:30px;')
        layout.addWidget(spacer)
        layout.addWidget(Element('group.png','Attendence'))
        layout.addWidget(Element('timetrack.png','TimeTracking'))
        layout.addWidget(Element('screenshot.png','ScreenShots'))
        layout.addWidget(Element('account_circle.png','Employee'))
        layout.addWidget(Element('teams.png','Teams'))
        layout.addWidget(Element('chat_bubble.png','Feedbacks'))
        layout.addWidget(Element('chat.png','Messages'))


        layout.addStretch()
        
        
        panel.setMaximumWidth(330)
        panel.setMinimumWidth(300)

        panel.setStyleSheet("""
        QFrame{
            background-color:#0085FF;
        }
        """)
        panel.setLayout(layout)
        return panel

    def HomePanel(self):
        self.homePanel=qw.QFrame()
        layout=qw.QVBoxLayout()
        self.homePanel.setStyleSheet("background-color:#CFCFCF")
        self.homePanel.setLayout(layout)
        self.homePanel.setMinimumWidth(1150)
        return self.homePanel
    def DashBoard(self):
        def ProgressIndicatorWidget(color='#33ff33',value=10):
            widget=qw.QFrame()
            widget.setFixedWidth(300)
            widget.setFixedHeight(400)
            shadow = qw.QGraphicsDropShadowEffect()
            shadow.setBlurRadius(16)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            widget.setGraphicsEffect(shadow)
            widget.setStyleSheet('''
            QFrame{
                background-color:#eeeeee;
                padding:10px;
            }
            ''')

            widgetLayout=qw.QVBoxLayout()
            head=qw.QLabel("Salary paid")
            head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            head.setFont(gui.QFont('Helvatica',15))

           
            progress=ProgressIndicatorMini(color=color,value=value)
            progress.setStyleSheet('''QFrame{margin-left:30px;}''')

            button=qw.QPushButton('View All')
            button.setStyleSheet('''
            QPushButton{
            background-color:'''+color+''';
            width:100px;
            border:none;
            padding:5px;
            }
            QPushButton:hover{
            background-color:green
            }
            ''')
            button.setGraphicsEffect(shadow)

            maintext=qw.QLabel("120/156")
            maintext.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            maintext.setFont(gui.QFont('Helvatica',13))

            widgetLayout.addWidget(head)
            widgetLayout.addWidget(progress,PyQt5.QtCore.Qt.AlignCenter)
            widgetLayout.addWidget(maintext,PyQt5.QtCore.Qt.AlignHCenter)
            widgetLayout.addWidget(button)
            widgetLayout.setAlignment(button,PyQt5.QtCore.Qt.AlignHCenter)
            
            # widgetLayout.setAlignment(PyQt5.QtCore.Qt.AlignTop)
            widget.setLayout(widgetLayout)
            return widget
        def UpcomingEvents():
            widget=qw.QFrame()
            widget.setMinimumWidth(400)
            head=qw.QLabel("Upcomming Events")
            head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            head.setFont(gui.QFont('Helvatica',17))

            content=qw.QScrollArea()
            content.setMaximumHeight(300)
            scrollwid=qw.QWidget()
            scrollwid.setStyleSheet('''
            QWidget{
                background-color:white;
            }
            QFrame#parent{
                border:1px solid black;
            }
            ''')
            content.setStyleSheet('''
            QScrollArea{
                border:none;
            }
            ''')
            # content.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOn)
            content.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
            content.setWidgetResizable(True)
            content.setWidget(scrollwid)
            scrollwidl=qw.QVBoxLayout()
            scrollwid.setLayout(scrollwidl)
            def Element(text,date,bgcolor):
                widget=qw.QFrame()
                widget.setFixedHeight(100)
                head=qw.QLabel(text)
                head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
                head.setFont(gui.QFont('Helvatica',15))
                content=qw.QLabel(date)
                content.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
                content.setFont(gui.QFont('Helvatica',12))
                widgetLayout=qw.QHBoxLayout()

                textframe=qw.QFrame()
                textlayout=qw.QVBoxLayout()
                textlayout.addWidget(head)
                textlayout.addWidget(content)
                textframe.setLayout(textlayout)
                imagelabel=qw.QLabel()
                image=gui.QPixmap(resource('assets/birthday.png'))
                image=image.scaled(60,60)
                imagelabel=qw.QLabel()
                imagelabel.setPixmap(image)

                widgetLayout.addWidget(imagelabel)
                widgetLayout.addWidget(textframe)
                widget.setLayout(widgetLayout)
                shadow = qw.QGraphicsDropShadowEffect()
                shadow.setBlurRadius(10)
                shadow.setXOffset(0)
                shadow.setYOffset(0)
                widget.setGraphicsEffect(shadow)
                widget.setStyleSheet('''
                QFrame{
                    background-color:'''+bgcolor+''';
                }
                ''')
                return widget


            for i in range(10):
                wid=Element('jeff\'s birthday','12-02-20015','#61ff99')
                wid.setObjectName('parent')
                scrollwidl.addWidget(wid)

            Image=gui.QPixmap(resource('assets/upcoming_events.png'))
            Image=Image.scaled(350,300)
            imagelabel=qw.QLabel()
            imagelabel.setPixmap(Image)
            imagelabel.setFixedHeight(300)
        
            widgetLayout=qw.QVBoxLayout()
            widgetLayout.addWidget(head)
            widgetLayout.addWidget(content)
            widgetLayout.addWidget(imagelabel)
            widgetLayout.setAlignment(imagelabel,PyQt5.QtCore.Qt.AlignHCenter)
            widget.setLayout(widgetLayout)
            shadow = qw.QGraphicsDropShadowEffect()
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setBlurRadius(10)
            widget.setGraphicsEffect(shadow)
            widget.setStyleSheet('''
            QFrame{
                background-color:white;
                
            }
            ''')
            return widget
        def WelcomeBoard(heading,content,image):
            widget=qw.QFrame()
            widget.setFixedHeight(300)
            widget.setFixedWidth(750)
            head=qw.QLabel(heading)
            head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            head.setFont(gui.QFont('Helvatica',20))
            content=qw.QLabel(content)
            content.setFont(gui.QFont('Helvatica',12))
            content.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            widgetLayout=qw.QHBoxLayout()
            rw=qw.QFrame()
            rwl=qw.QVBoxLayout()
            rwl.addWidget(head)
            rwl.addWidget(content)
            rw.setLayout(rwl)

            Image=gui.QPixmap(image)
            # Image=Image.scaled(50,50)
            imagelabel=qw.QLabel()
            imagelabel.setPixmap(Image)

            widgetLayout.addWidget(rw)
            widgetLayout.addWidget(imagelabel)
            shadow = qw.QGraphicsDropShadowEffect()
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setBlurRadius(10)
            widget.setGraphicsEffect(shadow)

            widget.setLayout(widgetLayout)
            widget.setStyleSheet('''
            QFrame{
            background-color:white;
            border-radius:14px;
            }
            ''')
            return widget
        def SimpleInfoBoard(heading,info,width=None,height=130,color='white'):
            widget=qw.QFrame()
            widget.setFixedHeight(height)
            if(width):widget.setFixedWidth(width)
            head=qw.QLabel(heading)
            head.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            head.setFont(gui.QFont('Helvatica',17))
            content=qw.QLabel(info)
            content.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
            content.setFont(gui.QFont('Helvatica',12))
            widgetLayout=qw.QVBoxLayout()
            widgetLayout.addWidget(head)
            widgetLayout.addWidget(content)
            widget.setLayout(widgetLayout)
            shadow = qw.QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            widget.setGraphicsEffect(shadow)
            widget.setStyleSheet('''
            QFrame{
                background-color:'''+color+''';
                border-radius:14px;
            }
            ''')
            return widget
        dashboard=qw.QFrame()
        dashboard.setContentsMargins(0,0,0,0)
      
        content=qw.QScrollArea()
        scrollwid=qw.QWidget()
        scrollwid.setStyleSheet('''
        QWidget{
            background-color:transparent;
        }
        ''')
        # content.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOn)
        content.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        content.setWidgetResizable(True)
        content.setWidget(scrollwid)
        
        scrollwidl=qw.QVBoxLayout()
        scrollwid.setLayout(scrollwidl)
        scrollwidl.setContentsMargins(0,0,0,0)

        
        

        temp=qw.QFrame()
        templ=qw.QHBoxLayout()
        templ.addWidget(SimpleInfoBoard("Employee ","120",240))
        templ.addWidget(SimpleInfoBoard("Abseent","30",240))
        templ.addWidget(SimpleInfoBoard("Leave","6",240))
        templ.setContentsMargins(0,12,0,12)
        temp.setLayout(templ)
        temp.setFixedWidth(750)
       
         
        temp2=qw.QFrame()
        
        temp2.setFixedHeight(250)
        templ2=qw.QHBoxLayout()
        p1=ProgressIndicator()
        p1.value=67

        p1.setText("Present",66)
        templ2.addWidget(p1)
        p=ProgressIndicator()
        p.value=80
        p.setText("leave",70)
        templ2.addWidget(p)
        temp2.setLayout(templ2)
        temp2.setFixedWidth(750)

        temp3=qw.QFrame()
        temp3l=qw.QVBoxLayout()
        temp3l.addWidget(WelcomeBoard('Welcome Husk','welcome to HRMS dashborard',resource("assets/welcome.png")))
        temp3l.addWidget(temp)
        temp3l.addWidget(temp2)
        temp3.setLayout(temp3l)

        temp4=qw.QFrame()
        temp4l=qw.QVBoxLayout()
        temp4l.addWidget(SimpleInfoBoard("Revenue","1420",200,color='#55ff22'))
        temp4l.addWidget(SimpleInfoBoard("New Users","3120",200,color='#61ff99'))
        temp4l.addWidget(SimpleInfoBoard("Income","1720",200,color='#55ff22'))
        temp4l.addWidget(SimpleInfoBoard("Expense","1270",200,color='#55ff22'))
        temp4l.addWidget(SimpleInfoBoard("Profit","1920",200,color='#55ff22'))
        # temp4l.setAlignment(PyQt5.QtCore.Qt.AlignHCenter)
        temp4l.setContentsMargins(6,0,6,0)
        temp4.setLayout(temp4l)
        
        temp5=qw.QFrame()
        temp5l=qw.QHBoxLayout()
        temp5l.addWidget(temp3)
        temp5l.addWidget(temp4)
        temp5l.addWidget(UpcomingEvents())
        temp5.setLayout(temp5l)

        temp6=qw.QFrame()
        temp6l=qw.QHBoxLayout()
        temp6l.addWidget(ProgressIndicatorWidget(color='#7561ff',value=20))
        temp6l.addWidget(ProgressIndicatorWidget(color='#42ee41',value=80))
        temp6l.addWidget(ProgressIndicatorWidget(color='orange',value=56))
        temp6l.addWidget(ProgressIndicatorWidget(color='#9e8606',value=80))
        temp6l.setContentsMargins(0,30,0,30)
       
        temp6.setLayout(temp6l)
         
        scrollwidl.addWidget(temp5)
        scrollwidl.addWidget(temp6)
        
        table=Table(headingsList=['Leader','Project','Tasks','Deadline','Staffs'])
        scrollwidl.addWidget(table)

        for i in range(10): table < ['hello','world','','-----','world']
        

        
        scrollwid.setSizePolicy(qw.QSizePolicy.Expanding,qw.QSizePolicy.Expanding)
        # content.setSizePolicy(qw.QSizePolicy.Expanding,qw.QSizePolicy.Expanding)
        content.setStyleSheet('''
        QScrollArea{
            border:none;
        }
        ''')
        content.setContentsMargins(0,0,0,0)
        # content.setFixedHeight(400)
        
        dashboard.setLayout(qw.QHBoxLayout())
        dashboard.layout().addWidget(content)
        
        
        self.currentHomeWidget=dashboard
        self.homePanel.layout().addWidget(dashboard)
        self.homePanel.layout().setContentsMargins(0,0,0,0)
        
        return dashboard

    def Emp_Attendence(self):
        dashboard=qw.QFrame()
        dashboard.setLayout(qw.QVBoxLayout())
        dashboard.layout().addWidget(qw.QLabel('Emp attendence'))
        self.currentHomeWidget=dashboard
        self.homePanel.layout().addWidget(dashboard)
    

