import ctypes
import sys
import PyQt5.QtWidgets as qw
from tkinter import *
from src.Home import Main
from src.Login import Login
from libs.Auth import getToken


def GetAdministratorPermission():ctypes.windll.shell32.ShellExecuteW(None,'runas',sys.executable," ".join(sys.argv),None,1)
def isAdmin(): return ctypes.windll.shell32.IsUserAnAdmin()

class App():
    def __init__(self):
        app=qw.QApplication([])
        WINDOW=Main() if (token:=getToken()) and len(token)==32 else Login() 
        app.exec_()

if __name__=='__main__':
        App()
  


