# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from SQ_Dialog import Ui_SQ_Dialog

class Ui_RegisterScreen(object):
    def setupUi(self, RegisterScreen):
        RegisterScreen.setObjectName("RegisterScreen")
        RegisterScreen.resize(811, 466)
        RegisterScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        self.centralwidget = QtWidgets.QWidget(RegisterScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.phone_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_3.sizePolicy().hasHeightForWidth())
        self.phone_3.setSizePolicy(sizePolicy)
        self.phone_3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.phone_3.setObjectName("phone_3")
        self.gridLayout.addWidget(self.phone_3, 8, 6, 1, 1)
        self.email_address = QtWidgets.QLineEdit(self.centralwidget)
        self.email_address.setObjectName("email_address")
        self.gridLayout.addWidget(self.email_address, 9, 2, 1, 3)
        self.faq_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.faq_button.sizePolicy().hasHeightForWidth())
        self.faq_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.faq_button.setFont(font)
        self.faq_button.setFlat(True)
        self.faq_button.setObjectName("faq_button")
        self.gridLayout.addWidget(self.faq_button, 13, 8, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 8, 1, 1)
        self.fn_label = QtWidgets.QLabel(self.centralwidget)
        self.fn_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fn_label.setObjectName("fn_label")
        self.gridLayout.addWidget(self.fn_label, 5, 1, 1, 1)
        self.phone_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_1.sizePolicy().hasHeightForWidth())
        self.phone_1.setSizePolicy(sizePolicy)
        self.phone_1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.phone_1.setObjectName("phone_1")
        self.gridLayout.addWidget(self.phone_1, 8, 2, 1, 1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 11, 2, 1, 3)
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 9, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 10, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 11, 1, 1, 1)
        self.register_button = QtWidgets.QPushButton(self.centralwidget)
        self.register_button.setObjectName("register_button")
        self.gridLayout.addWidget(self.register_button, 13, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 13, 3, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 13, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(3, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 13, 5, 1, 1)
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 7, 2, 1, 5)
        self.dash_label1 = QtWidgets.QLabel(self.centralwidget)
        self.dash_label1.setMaximumSize(QtCore.QSize(10, 16777215))
        self.dash_label1.setObjectName("dash_label1")
        self.gridLayout.addWidget(self.dash_label1, 8, 3, 1, 1)
        self.dash_label2 = QtWidgets.QLabel(self.centralwidget)
        self.dash_label2.setMaximumSize(QtCore.QSize(10, 16777215))
        self.dash_label2.setObjectName("dash_label2")
        self.gridLayout.addWidget(self.dash_label2, 8, 5, 1, 1)
        self.first_name = QtWidgets.QLineEdit(self.centralwidget)
        self.first_name.setObjectName("first_name")
        self.gridLayout.addWidget(self.first_name, 5, 2, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.header_label.setFont(font)
        self.header_label.setObjectName("header_label")
        self.horizontalLayout.addWidget(self.header_label)
        self.header_label2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Gubbi")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.header_label2.setFont(font)
        self.header_label2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.header_label2.setObjectName("header_label2")
        self.horizontalLayout.addWidget(self.header_label2)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 9)
        self.ln_label = QtWidgets.QLabel(self.centralwidget)
        self.ln_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ln_label.setObjectName("ln_label")
        self.gridLayout.addWidget(self.ln_label, 6, 1, 1, 1)
        self.address_label = QtWidgets.QLabel(self.centralwidget)
        self.address_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.address_label.setObjectName("address_label")
        self.gridLayout.addWidget(self.address_label, 7, 1, 1, 1)
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 10, 2, 1, 3)
        self.phone_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_2.sizePolicy().hasHeightForWidth())
        self.phone_2.setSizePolicy(sizePolicy)
        self.phone_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.phone_2.setObjectName("phone_2")
        self.gridLayout.addWidget(self.phone_2, 8, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 12, 2, 1, 1)
        self.email_domain_label = QtWidgets.QLabel(self.centralwidget)
        self.email_domain_label.setObjectName("email_domain_label")
        self.gridLayout.addWidget(self.email_domain_label, 10, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 1, 1, 1)
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.gridLayout.addWidget(self.description_label, 3, 1, 1, 1)
        self.phone_label = QtWidgets.QLabel(self.centralwidget)
        self.phone_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.phone_label.setObjectName("phone_label")
        self.gridLayout.addWidget(self.phone_label, 8, 1, 1, 1)
        self.last_name = QtWidgets.QLineEdit(self.centralwidget)
        self.last_name.setObjectName("last_name")
        self.gridLayout.addWidget(self.last_name, 6, 2, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 13, 7, 1, 1)
        RegisterScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        RegisterScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterScreen)
        self.statusbar.setObjectName("statusbar")
        RegisterScreen.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(RegisterScreen)

    def retranslateUi_english(self, RegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        RegisterScreen.setWindowTitle(_translate("RegisterScreen", "Cypress"))
        self.header_label.setText(_translate("RegisterScreen", "Cypress"))
        self.header_label2.setText(_translate("RegisterScreen", "City of Toronto"))
        self.description_label.setText(_translate("RegisterScreen", "Please enter your information below:"))
        self.fn_label.setText(_translate("RegisterScreen", "First Name:"))
        self.ln_label.setText(_translate("RegisterScreen", "Last Name:"))
        self.address_label.setText(_translate("RegisterScreen", "Address:"))
        self.phone_label.setText(_translate("RegisterScreen", "Phone Number:"))
        self.email_label.setText(_translate("RegisterScreen", "E-mail Address:"))
        self.username_label.setText(_translate("RegisterScreen", "Username:"))
        self.password_label.setText(_translate("RegisterScreen", "Password:"))
        self.register_button.setText(_translate("RegisterScreen", "Register"))
        self.cancel_button.setText(_translate("RegisterScreen", "Cancel"))
        self.dash_label1.setText(_translate("RegisterScreen", "-"))
        self.dash_label2.setText(_translate("RegisterScreen", "-"))
        self.faq_button.setText(_translate("RegisterScreen", "FAQ"))
        self.email_domain_label.setText(_translate("RegisterScreen", "@cypress.on.ca"))
        

    def retranslateUi_french(self, RegisterScreen):
        _translate = QtCore.QCoreApplication.translate
        RegisterScreen.setWindowTitle(_translate("RegisterScreen", "Cypress"))
        self.header_label.setText(_translate("RegisterScreen", "Cypress"))
        self.header_label2.setText(_translate("RegisterScreen", "Ville de Toronto"))
        self.description_label.setText(_translate("RegisterScreen", "S'il vous plaît entrer vos informations ci-dessous:"))
        self.fn_label.setText(_translate("RegisterScreen", "Prénom:"))
        self.ln_label.setText(_translate("RegisterScreen", "Nom de Famille:"))
        self.address_label.setText(_translate("RegisterScreen", "Addresse:"))
        self.phone_label.setText(_translate("RegisterScreen", "Numéro de Téléphone:"))
        self.email_label.setText(_translate("RegisterScreen", "Addresse E-mail:"))
        self.username_label.setText(_translate("RegisterScreen", "Nom d'Utilisateur:"))
        self.password_label.setText(_translate("RegisterScreen", "Mot de Passe:"))
        self.register_button.setText(_translate("RegisterScreen", "S'inscrire"))
        self.cancel_button.setText(_translate("RegisterScreen", "Annuler"))
        self.dash_label1.setText(_translate("RegisterScreen", "-"))
        self.dash_label2.setText(_translate("RegisterScreen", "-"))
        self.faq_button.setText(_translate("RegisterScreen", "FAQ"))
        self.email_domain_label.setText(_translate("RegisterScreen", "@cypress.on.ca"))
   

class MyDialog(QtWidgets.QDialog):
    def __init__(self, language):
        super().__init__()
        self.ui = Ui_SQ_Dialog()
        self.ui.setupUi(self)
        self.retranslateUi_english(self.ui)
        self.ui.security_question = QtWidgets.QLineEdit(self)
        self.ui.security_question.setGeometry(QtCore.QRect(190, 170,  381, 51))
        self.ui.security_question.setObjectName("security_question")
        self.ui.description_label.setStyleSheet("color:rgb(115, 210, 22)")
        self.state=''
        
        if language=='french':   self.retranslateUi_french(self.ui)
        else:   self.retranslateUi_english(self.ui)
        self.ui.OK_Button.clicked.connect(self.close)

    def close(self):
        self.state='OK'
        self.hide()

    def retranslateUi_english(self, ui):
        ui.retranslateUi_english(self)
        _translate = QtCore.QCoreApplication.translate
        ui.description_label.setText(_translate("SQ_Dialog", "Your registration is almost complete! Enter a security question and answer to verify your identity should you forget your password"))

    def retranslateUi_french(self, ui):
        ui.retranslateUi_english(self)
        _translate = QtCore.QCoreApplication.translate
        ui.description_label.setText(_translate("SQ_Dialog", "Votre inscription est presque terminée! Entrez une question de sécurité et une réponse pour vérifier votre identité si vous oubliez votre mot de passe."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterScreen = QtWidgets.QMainWindow()
    ui = Ui_RegisterScreen()
    ui.setupUi(RegisterScreen)
    RegisterScreen.show()
    sys.exit(app.exec_())
