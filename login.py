# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from signup import Ui_signupwindow
import sqlite3

conn = sqlite3.connect('ids.db')
c = conn.cursor()


class Ui_loginwindow(QtWidgets.QMainWindow):
    def setupUi(self, loginwindow):
        loginwindow.setObjectName("loginwindow")
        loginwindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(loginwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 721, 521))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 130, 201, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 220, 201, 41))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(360, 130, 301, 41))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(360, 210, 301, 51))
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(self.groupBox)
        self.loginbutton.setGeometry(QtCore.QRect(120, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setItalic(False)
        self.loginbutton.setFont(font)
        self.loginbutton.setObjectName("loginbutton")
        self.signupbutton = QtWidgets.QPushButton(self.groupBox)
        self.signupbutton.setGeometry(QtCore.QRect(390, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setItalic(False)
        self.signupbutton.setFont(font)
        self.signupbutton.setObjectName("signupbutton")
        loginwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(loginwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        loginwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(loginwindow)
        self.statusbar.setObjectName("statusbar")
        loginwindow.setStatusBar(self.statusbar)
        self.signupbutton.clicked.connect(self.signup_window)
        self.loginbutton.clicked.connect(self.login_query)

        self.retranslateUi(loginwindow)
        QtCore.QMetaObject.connectSlotsByName(loginwindow)

    def retranslateUi(self, loginwindow):
        _translate = QtCore.QCoreApplication.translate
        loginwindow.setWindowTitle(_translate("loginwindow", "MainWindow"))
        self.groupBox.setTitle(_translate("loginwindow", "LOGIN"))
        self.label.setText(_translate("loginwindow", "Username"))
        self.label_2.setText(_translate("loginwindow", "Password"))
        self.loginbutton.setText(_translate("loginwindow", "Login"))
        self.signupbutton.setText(_translate("loginwindow", "Signup"))

    def login_query(self):
        username = self.username.text()
        password = self.password.text()
        c.execute("SELECT username, password FROM ids WHERE username = :username AND password = :password", {
                  'username': username, 'password': password})
        ls = c.fetchone()
        if ls != None:
            QMessageBox.about(self, 'Logged in',
                              'You have been succesfully logged in')
        else:
            QMessageBox.about(self, 'Error', 'No such account exists')

    def signup_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_signupwindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginwindow = QtWidgets.QMainWindow()
    ui = Ui_loginwindow()
    ui.setupUi(loginwindow)
    loginwindow.show()
    sys.exit(app.exec_())
