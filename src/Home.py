from ctypes import windll
from logging import root
from lib.Assets import  resource
from tkinter import *
from lib.ScreenShot import takeScreenShot


def TopBar(parent):
    Frame(parent)

class TopBar():
    def __init__(self,parent:Tk):
        self.font='Microsoft YaHei UI Light'
        self.root=Frame(parent)
        self.root.pack(padx=4,pady=4)
        global logoimg
        logoimg=PhotoImage(file=resource("./assets/minilogo.png"))
        Label(self.root,image=logoimg).grid(row=0,column=0,ipady=10,padx=15)

        Label(self.root,text='HRMS',font=(self.font,25,'bold')).grid(row=0,column=1)

        Frame(self.root,width=self.root.winfo_screenwidth()-750).grid(column=2,row=0)


        global userimg
        userimg=PhotoImage(file=resource("./assets/userimg.png"))
        Label(self.root,image=userimg).grid(row=0,column=3,padx=30)

        Label(self.root,text='tecktok4u@tech.in',font=(self.font,10)).grid(row=0,column=4)

        self.butt=Button(self.root,text='logout',width=10,pady=1,bg='#57a1f8', fg='white',font=('Microsoft YaHei UI Light',10,'bold'), border=0)
        self.butt.grid(row=0,column=5,padx=25)
        self.butt.bind('<Enter>',lambda e :self.butt.configure(bg='#0765D3'))
        self.butt.bind('<Leave>',lambda e:self.butt.configure(bg='#57a1f8'))

class SideBar():
    def __init__(self,parent:Tk):
        Frame(parent,width=300,height=parent.winfo_screenheight(),bg='blue').pack(anchor='w')

def Button(root):
    button=Frame(root)



class Home():
    def __init__(self,parent:Tk):
        self.parent=parent
        parent.title('Home')
        parent.geometry(f'{parent.winfo_screenwidth()-100}x{parent.winfo_screenheight()-100}+50-25')
        parent.configure(bg="#fff")
        parent.resizable(False,False)

        self.root=Frame(parent)
        self.root.pack(padx=4,pady=4)
        TopBar(self.root)
        SideBar(self.root)