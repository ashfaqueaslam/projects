# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

conn = sqlite3.connect('ids.db')
c = conn.cursor()


class Ui_signupwindow(QtWidgets.QMainWindow):
    def setupUi(self, signupwindow):
        signupwindow.setObjectName("signupwindow")
        signupwindow.resize(972, 735)
        self.centralwidget = QtWidgets.QWidget(signupwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 40, 891, 591))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(20)
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 90, 211, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 211, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 230, 211, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 211, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 370, 211, 41))
        self.label_5.setObjectName("label_5")
        self.firstname = QtWidgets.QLineEdit(self.groupBox)
        self.firstname.setGeometry(QtCore.QRect(360, 90, 371, 41))
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.groupBox)
        self.lastname.setGeometry(QtCore.QRect(360, 160, 371, 41))
        self.lastname.setObjectName("lastname")
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(360, 230, 371, 41))
        self.username.setObjectName("username")
        self.email = QtWidgets.QLineEdit(self.groupBox)
        self.email.setGeometry(QtCore.QRect(360, 300, 371, 41))
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(360, 370, 371, 41))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.submitbutton = QtWidgets.QPushButton(self.groupBox)
        self.submitbutton.setGeometry(QtCore.QRect(320, 460, 151, 51))
        self.submitbutton.setObjectName("submitbutton")
        signupwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(signupwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 26))
        self.menubar.setObjectName("menubar")
        signupwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(signupwindow)
        self.statusbar.setObjectName("statusbar")
        signupwindow.setStatusBar(self.statusbar)
        self.submitbutton.clicked.connect(self.signup_query)

        self.retranslateUi(signupwindow)
        QtCore.QMetaObject.connectSlotsByName(signupwindow)

    def retranslateUi(self, signupwindow):
        _translate = QtCore.QCoreApplication.translate
        signupwindow.setWindowTitle(_translate("signupwindow", "MainWindow"))
        self.groupBox.setTitle(_translate("signupwindow", "Signup"))
        self.label.setText(_translate("signupwindow", "First Name"))
        self.label_2.setText(_translate("signupwindow", "Last Name"))
        self.label_3.setText(_translate("signupwindow", "Username"))
        self.label_4.setText(_translate("signupwindow", "Email"))
        self.label_5.setText(_translate("signupwindow", "Password"))
        self.submitbutton.setText(_translate("signupwindow", "Submit"))

    def signup_query(self):
        firstname = self.firstname.text()
        lastname = self.lastname.text()
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()

        ls = [firstname, lastname, username, email, password]
        switch = True

        for i in ls:
            if i == "":
                QMessageBox.about(self, 'Missing field',
                                  'One or more fields are empty')
                switch = False
                break

        c.execute("SELECT username FROM ids WHERE username = :username", {
                  'username': username})
        un = c.fetchone()
        c.execute("SELECT password FROM ids WHERE password = :password", {
                  'password': password})
        pw = c.fetchone()
        if un != None:
            QMessageBox.about(self, 'Invalid username',
                              'Username is not available')
            switch = False

        elif pw != None:
            QMessageBox.about(self, 'Invalid password',
                              'Password is not available')
            switch = False

        if switch:
            c.execute("INSERT INTO ids VALUES (?, ?, ?, ?, ?)",
                      (firstname, lastname, username, email, password))
            conn.commit()
            QMessageBox.about(self, 'Succesful signup',
                              'You are succesfully signed in')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    signupwindow = QtWidgets.QMainWindow()
    ui = Ui_signupwindow()
    ui.setupUi(signupwindow)
    signupwindow.show()
    sys.exit(app.exec_())
