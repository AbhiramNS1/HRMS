
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 511, 71))
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
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(26, 0, 71, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Downloads/minilogo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(400, 10, 47, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../../Downloads/HRMS1/account_circle.png"))
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 70, 321, 351))
        self.frame.setStyleSheet("background-color: #a6a6a6")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 161, 22))
        self.comboBox.setStyleSheet("background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"box-shadow: 5px 10px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.listView = QtWidgets.QListView(self.frame)
        self.listView.setGeometry(QtCore.QRect(10, 40, 291, 241))
        self.listView.setStyleSheet("background-color:#ffffff;\n"
"  border-radius: 25px;\n"
"  border: 2px solid #0033cc;")
        self.listView.setObjectName("listView")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 290, 241, 31))
        self.textEdit.setStyleSheet("background-color:#ffffff;\n"
"  border-radius: 15px;\n"
"  border: 2px solid #0033cc;\n"
"  \n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 290, 71, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color:#0033cc;\n"
"color: white;\n"
"font-weight: bold;\n"
"border-radius: 15px;\n"
"border: 2px solid #0033cc;\n"
"box-shadow: 5px 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(193, 69, 255);\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(320, 70, 181, 351))
        self.frame_3.setStyleSheet("background-color:#D9D9D9")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 47, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../Downloads/HRMS1/account_circle.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(60, 16, 91, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 141, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 141, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 130, 151, 31))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">HRMS</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "ADMIN@TECHTOK4U"))
        self.comboBox.setItemText(0, _translate("MainWindow", "SELECT USER"))
        self.pushButton.setText(_translate("MainWindow", "SEND"))
        self.label_6.setText(_translate("MainWindow", "Employee ID"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_8.setText(_translate("MainWindow", "Team:"))
        self.label_9.setText(_translate("MainWindow", " Role:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
