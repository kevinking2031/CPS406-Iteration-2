# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from TemplateWindow import Ui_TemplateWindow
import time


class Ui_LoginScreen(object):
        
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(811, 466)
        LoginScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(LoginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.header_label = QtWidgets.QLabel(self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setFrameShape(QtWidgets.QFrame.HLine)
        self.header_label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.header_label.setLineWidth(1)
        self.header_label.setMidLineWidth(0)
        self.header_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.header_label.setObjectName("header_label")
        self.faq_button = QtWidgets.QPushButton(self.centralwidget)
        self.faq_button.setGeometry(QtCore.QRect(738, 423, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.faq_button.setFont(font)
        self.faq_button.setFlat(True)
        self.faq_button.setObjectName("faq_button")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(70, 70, 681, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(260, 190, 211, 31))
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(260, 240, 211, 31))
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(150, 240, 81, 21))
        self.password_label.setObjectName("password_label")
        self.email_domain_label = QtWidgets.QLabel(self.centralwidget)
        self.email_domain_label.setGeometry(QtCore.QRect(510, 190, 121, 21))
        self.email_domain_label.setObjectName("email_domain_label")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(140, 310, 89, 25))
        self.login_button.setObjectName("login_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(450, 310, 89, 25))
        self.cancel_button.setObjectName("cancel_button")
        LoginScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        LoginScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginScreen)
        self.statusbar.setObjectName("statusbar")
        LoginScreen.setStatusBar(self.statusbar)

        #self.retranslateUi(LoginScreen)
        #self.login_button.clicked.connect(self.getInfo)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi_english(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Cypress - login"))
        self.header_label.setText(_translate("LoginScreen", "CYPRESS                                                                                  City of Toronto"))
        self.faq_button.setText(_translate("LoginScreen", "FAQ"))
        self.description_label.setText(_translate("LoginScreen", "You are currently at the Cypress Login Page. By logging into this system, you will be able to report a variety of problems as you have witnessed on the streets of Toronto. "))
        self.username_label.setText(_translate("LoginScreen", "Username:"))
        self.password_label.setText(_translate("LoginScreen", "Password:"))
        self.email_domain_label.setText(_translate("LoginScreen", "@cypress.on.ca"))
        self.login_button.setText(_translate("LoginScreen", "Login"))
        self.cancel_button.setText(_translate("LoginScreen", "Cancel"))

    def retranslateUi_french(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Cypress - login"))
        self.header_label.setText(_translate("LoginScreen", "CYPRESS                                                                                  Ville de Toronto"))
        self.faq_button.setText(_translate("LoginScreen", "FAQ"))
        self.description_label.setText(_translate("LoginScreen", "Vous êtes actuellement sur la page de connexion de Cypress. En vous connectant à ce système, vous serez en mesure de signaler une variété de problèmes comme vous en avez été témoins dans les rues de Toronto. "))
        self.username_label.setText(_translate("LoginScreen", "Nom d'Utilisateur:"))
        self.password_label.setText(_translate("LoginScreen", "Mot de Passe:"))
        self.email_domain_label.setText(_translate("LoginScreen", "@cypress.on.ca"))
        self.login_button.setText(_translate("LoginScreen", "Connexion"))
        self.cancel_button.setText(_translate("LoginScreen", "Annuler"))

    # def getInfo(self):
    #     return [self.username.text(), self.password.text()]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginScreen = QtWidgets.QMainWindow()
    ui = Ui_LoginScreen()
    ui.setupUi(LoginScreen)
    LoginScreen.show()
    sys.exit(app.exec_())
