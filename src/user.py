


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from datetime import date
from datetime import time
from lib.ScreenShot import takeScreenShot
#from workhour import workhours

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 70, 181, 481))
        self.frame.setStyleSheet("#frame{\n"
"background-color:#0033cc;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 181, 31))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00008B;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("HRMS/grid_view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 30, 181, 31))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00008B;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("HRMS/speaker_notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 60, 181, 31))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00008B;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("HRMS/settings_suggest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 90, 181, 31))
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00008B;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("HRMS (1)/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 120, 181, 31))
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"text-align: left;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #00008B;\n"
"}")
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(180, 70, 561, 471))
        self.frame_3.setStyleSheet("background-color:#e6f0ff;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 400, 211, 31))
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(193, 69, 255);\n"
"}")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, 0, 751, 71))
        self.frame_2.setStyleSheet("QFrame\n"
"{\n"
"background-color:#e6f0ff;\n"
"border-radius: 50%;\n"
"box-shadow: 5px 10px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 20, 81, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(630, 20, 75, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(193, 69, 255);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(26, 0, 71, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("minilogo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(480, 20, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(430, 10, 47, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("HRMS (1)/account_circle.png"))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actiongrid = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("HRMS/grid_view.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiongrid.setIcon(icon4)
        self.actiongrid.setObjectName("actiongrid")
        self.actionmessage = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("HRMS/speaker_notes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionmessage.setIcon(icon5)
        self.actionmessage.setObjectName("actionmessage")
        self.actionsettings = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("HRMS/settings_suggest.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsettings.setIcon(icon6)
        self.actionsettings.setObjectName("actionsettings")
        self.actionattendance = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("HRMS/account_box.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionattendance.setIcon(icon7)
        self.actionattendance.setObjectName("actionattendance")
        self.actionattendance1 = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("HRMS (1)/group.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionattendance1.setIcon(icon8)
        self.actionattendance1.setObjectName("actionattendance1")
        self.actiontimetracking = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("HRMS (1)/hourglass_bottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontimetracking.setIcon(icon9)
        self.actiontimetracking.setObjectName("actiontimetracking")
        self.actionscreenshot = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("HRMS (1)/screenshot_monitor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionscreenshot.setIcon(icon10)
        self.actionscreenshot.setObjectName("actionscreenshot")
        self.actionteam = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("HRMS (1)/diversity_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionteam.setIcon(icon11)
        self.actionteam.setObjectName("actionteam")
        self.actionemployee = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("HRMS (1)/account_circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionemployee.setIcon(icon12)
        self.actionemployee.setObjectName("actionemployee")
        self.actionfeedback = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("HRMS (1)/chat_bubble.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfeedback.setIcon(icon13)
        self.actionfeedback.setObjectName("actionfeedback")
        self.actionchat = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("HRMS (1)/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionchat.setIcon(icon14)
        self.actionchat.setObjectName("actionchat")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "DASH BOARD"))
        self.pushButton_3.setText(_translate("MainWindow", "MESSAGES"))
        self.pushButton_4.setText(_translate("MainWindow", "SETTINGS"))
        self.pushButton_5.setText(_translate("MainWindow", "NOTIFICATIONS"))
        self.pushButton_6.setText(_translate("MainWindow", "VIEW SALARY"))
        self.pushButton_7.setText(_translate("MainWindow", "START WORK"))
        self.pushButton_7.clicked.connect(self.startwork)
        self.pushButton_7.clicked.connect(self.pushButton_7.deleteLater)
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">HRMS</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "LOGOUT"))
        self.pushButton.hide()
        self.pushButton.clicked.connect(self.logout)
        self.label_3.setText(_translate("MainWindow", "Employee@001"))
        self.actiongrid.setText(_translate("MainWindow", "grid"))
        self.actionmessage.setText(_translate("MainWindow", "message"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))
        self.actionattendance.setText(_translate("MainWindow", "attendance"))
        self.actionattendance1.setText(_translate("MainWindow", "attendance1"))
        self.actiontimetracking.setText(_translate("MainWindow", "timetracking"))
        self.actionscreenshot.setText(_translate("MainWindow", "screenshot"))
        self.actionteam.setText(_translate("MainWindow", "team"))
        self.actionemployee.setText(_translate("MainWindow", "employee"))
        self.actionfeedback.setText(_translate("MainWindow", "feedback"))
        self.actionchat.setText(_translate("MainWindow", "chat"))

    def startwork(self):
        msg = QMessageBox()
        msg.setWindowTitle("You are Logged In")
        msg.setText("Your Attendance is been marked. Kindly Logout after you finish work")
        x = msg.exec_()  
        self.pushButton.show()
        datetime = QDate.currentDate()
        print("login time")
        global login_time
        login_time = QTime.currentTime()
        print(login_time.toString())
        print(datetime.toString())
        takeScreenShot(10)
        
    def logout(self):
        datetime = QDate.currentDate()
        print("logout time")
        logout_time = QTime.currentTime()
        print(logout_time.toString())
        print(datetime.toString())
        MainWindow.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
