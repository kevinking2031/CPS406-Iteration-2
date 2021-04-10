from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class UI_ContactScreen(object):

    def setupUi(self, ContactScreen):
        ContactScreen.setObjectName("ContactScreen")
        ContactScreen.resize(811, 468)
        ContactScreen.setWindowTitle("Cypress")
        ContactScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        ContactScreen.setWindowOpacity(2.0)
        ContactScreen.setAutoFillBackground(False)
        ContactScreen.setStyleSheet("")
        ContactScreen.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.centralwidget = QtWidgets.QWidget(ContactScreen)
        self.centralwidget.setObjectName("centralwidget")

        header_font = QtGui.QFont()
        header_font.setFamily("FreeSans")
        header_font.setPointSize(15)
        header_font.setBold(True)
        header_font.setWeight(12)

        contact_font = QtGui.QFont()
        contact_font.setFamily("FreeSans")
        contact_font.setPointSize(13)

        info_font = QtGui.QFont()
        info_font.setFamily("FreeSans")
        info_font.setPointSize(11)

        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(10, 5, 800, 50))
        self.Header.setFont(header_font)
        self.Header.setObjectName("Header")

        self.c1 = QtWidgets.QLabel(self.centralwidget)
        self.c1.setGeometry(10, 45, 800, 50)
        self.c1.setFont(contact_font)
        self.c1.setObjectName("q1")

        self.i1 = QtWidgets.QLabel(self.centralwidget)
        self.i1.setGeometry(10, 70, 800, 50)
        self.i1.setFont(info_font)
        self.i1.setObjectName("a1")

        self.c2 = QtWidgets.QLabel(self.centralwidget)
        self.c2.setGeometry(10, 110, 800, 50)
        self.c2.setFont(contact_font)
        self.c2.setObjectName("q2")

        self.i2 = QtWidgets.QLabel(self.centralwidget)
        self.i2.setGeometry(10, 145, 800, 50)
        self.i2.setFont(info_font)
        self.i2.setObjectName("a2")

        self.c3 = QtWidgets.QLabel(self.centralwidget)
        self.c3.setGeometry(10, 195, 800, 50)
        self.c3.setFont(contact_font)
        self.c3.setObjectName("q3")

        self.i3 = QtWidgets.QLabel(self.centralwidget)
        self.i3.setGeometry(10, 220, 800, 50)
        self.i3.setFont(info_font)
        self.i3.setObjectName("a3")

        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(702, 423, 89, 25))
        self.ok_button.setObjectName("ok_button")

        ContactScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi_french(ContactScreen)
        QtCore.QMetaObject.connectSlotsByName(ContactScreen)

    def retranslateUi_english(self, ContactScreen):
        _translate = QtCore.QCoreApplication.translate
        ContactScreen.setWindowTitle(_translate("ContactScreen", "Cypress"))
        self.Header.setText(_translate("ContactScreen", "Contact Information"))

        self.c1.setText(_translate("ContactScreen", "Submit a Report"))
        self.i1.setText(_translate("ContactScreen", "Phone: (123)456-7890"))

        self.c2.setText(_translate("ContactScreen", "General Support"))
        self.i2.setText(_translate("ContactScreen", "Phone: (456)789-0123"
                                   "\nEmail: support@cypress.on.ca"))

        self.c3.setText(_translate("ContactScreen", "Have a suggestion?"))
        self.i3.setText(_translate("ContactScreen", "Email: suggest@cypress.on.ca"))

        self.ok_button.setText(_translate("ContactScreen", "OK"))

    def retranslateUi_french(self, ContactScreen):
        _translate = QtCore.QCoreApplication.translate
        ContactScreen.setWindowTitle(_translate("ContactScreen", "Cypress"))
        self.Header.setText(_translate("ContactScreen", "Coordonnées"))

        self.c1.setText(_translate("ContactScreen", "envoyer un rapport"))
        self.i1.setText(_translate("ContactScreen", "Téléphoner: (123)456-7890"))

        self.c2.setText(_translate("ContactScreen", "Support général"))
        self.i2.setText(_translate("ContactScreen", "Téléphoner: (456)789-0123"
                                                    "\nE-mail: support@cypress.on.ca"))

        self.c3.setText(_translate("ContactScreen", "Avez-vous une suggestion?"))
        self.i3.setText(_translate("ContactScreen", "E-mail: suggest@cypress.on.ca"))

        self.ok_button.setText(_translate("ContactScreen", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactScreen = QtWidgets.QMainWindow()
    ui = UI_ContactScreen()
    ui.setupUi(ContactScreen)
    ContactScreen.show()
    sys.exit(app.exec_())
