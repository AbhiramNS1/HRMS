
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as gui
import PyQt5.QtCore
from src.Home import Main
from libs.Assets import resource
from libs.Auth import AuthenticateUser

WINDOW=None
class Login(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HRMS - Login')
        self.setWindowIcon(gui.QIcon(resource('assets/logo.png')))
        self.setLayout(qw.QVBoxLayout())
        self.setMinimumSize(1000,600)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(0,0,0,0) #making the default margin to 0
       
        mainFrame=qw.QFrame()
        mainFrame.setLayout(qw.QHBoxLayout())
        mainFrame.setStyleSheet('''QFrame{background-color:white}''')
   
        Image=gui.QPixmap(resource('assets/logo.png'))
        imagelabel=qw.QLabel()
        imagelabel.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        
        spacer1=qw.QFrame()
        spacer1.setSizePolicy(qw.QSizePolicy.Expanding,qw.QSizePolicy.Expanding)
        spacer2=qw.QFrame()
        spacer2.setSizePolicy(qw.QSizePolicy.Expanding,qw.QSizePolicy.Expanding)
        spacer3=qw.QFrame()
        spacer3.setSizePolicy(qw.QSizePolicy.Expanding,qw.QSizePolicy.Expanding)
        spacer3.setMaximumWidth(200)

        imagelabel.setPixmap(Image)
        
        mainFrame.layout().addWidget(spacer1)
        mainFrame.layout().addWidget(imagelabel)


        loginFrame=qw.QFrame()
        loginlayout=qw.QVBoxLayout()
        
        signinLabel=qw.QLabel('Sign In')
        signinLabel.setFont(gui.QFont("Helvatica",30))
        
        unameLabel=qw.QLabel('Username :')
        unameLabel.setFont(gui.QFont("Helvatica",12))
        self.uname=qw.QLineEdit()
        passwordLabel=qw.QLabel('password :')
        passwordLabel.setFont(gui.QFont("Helvatica",12))
        self.password=qw.QLineEdit()
        loginlayout.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        loginFrame.setFixedWidth(400)
        
        dummy1=qw.QFrame()
        dummy1.setLayout(qw.QHBoxLayout())
        submit=qw.QPushButton(text='Submit')
        submit.setMaximumWidth(100)
        submit.setStyleSheet(
            '''
            QPushButton{
                background-color:#49a1ff;
                border:none;
                border-radius:5px;
                padding:7px;
                font-size:17px;
            }
            QPushButton:hover{
                background-color:#007bff;
            }
            QPushButton:pressed{
                background-color:#166ecc;
            }
            '''
        )
        submit.clicked.connect(self.SignIn)
        dummy1.layout().addWidget(submit)
        
        basicstyle='''
               QLineEdit{
                padding:4px;
                font-size:16px;
                margin:10px
               }
        '''
        loginFrame.setStyleSheet(basicstyle)
        loginlayout.addWidget(signinLabel)
        loginlayout.addWidget(unameLabel)
        loginlayout.addWidget(self.uname)
        loginlayout.addWidget(passwordLabel)
        loginlayout.addWidget(self.password)
        loginlayout.addWidget(dummy1)
        loginFrame.setLayout(loginlayout)

        

      
     
        mainFrame.layout().addWidget(spacer3)
        mainFrame.layout().addWidget(loginFrame)
       
        self.layout().addWidget(mainFrame)
        mainFrame.layout().addWidget(spacer2)


        self.show()
    def SignIn(self):
        username=self.uname.text()
        password=self.password.text()
        #implement basic email and password validation here
        def Show(status):
            global WINDOW
            self.close()
            WINDOW=Main()
        AuthenticateUser(username,password,Show)

