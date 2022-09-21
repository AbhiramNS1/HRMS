
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as gui
import PyQt5.QtCore
from lib.Assets import resource

class Main(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HRMS')
        self.setWindowIcon(gui.QIcon(resource('assets/logo.png')))
        self.setLayout(qw.QVBoxLayout())
        self.setMinimumSize(1200,800)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0,0,0,0) #making the default margin to 0
        self.layout().addWidget(Main.CreateTopBar())

        mainFrame=qw.QFrame()
        mainFrame.setLayout(qw.QHBoxLayout())
        mainFrame.layout().setContentsMargins(0,0,0,0)
        mainFrame.layout().setSpacing(0)
        mainFrame.layout().addWidget(Main.SideNavPanel(),1)
        mainFrame.layout().addWidget(Main.HomePanel(),3)

        self.layout().addWidget(mainFrame)



        self.show()
    def CreateTopBar():
        TopBar=qw.QFrame()
        TopBar.setMaximumHeight(100)
        TopBar.setMinimumHeight(100)
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

        layout.addWidget(qw.QPushButton('logout'))
        TopBar.setStyleSheet("""
        QFrame{
            background-color:#D9D9D9;
        }
        """)
        TopBar.setLayout(layout)
        return TopBar
    def SideNavPanel():
        def Element(icon:str,text:str):
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
            return button
        panel=qw.QFrame()
        
        layout=qw.QVBoxLayout()
        layout.setSpacing(0)
        
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(Element('dashboard.png','Dashboard'))
        layout.addWidget(Element('account_box.png','Attendence'))
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
        
        
        panel.setMaximumWidth(380)
        panel.setStyleSheet("""
        QFrame{
            background-color:#0085FF;
        }
        """)
        panel.setLayout(layout)
        return panel

    def HomePanel():
        panel=qw.QFrame()
        layout=qw.QVBoxLayout()
        panel.setStyleSheet("background-color:#CFCFCF")
        panel.setLayout(layout)
        return panel

        


def HomeApp():
    app=qw.QApplication([])
    mv=Main()
    app.exec_()
