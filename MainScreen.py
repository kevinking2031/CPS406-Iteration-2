# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.setFixedSize(811, 466)
        MainScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainScreen)
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
        self.go_button = QtWidgets.QPushButton(self.centralwidget)
        self.go_button.setGeometry(QtCore.QRect(220, 380, 71, 21))
        self.go_button.setObjectName("go_button")
        self.pic2_label = QtWidgets.QLabel(self.centralwidget)
        self.pic2_label.setGeometry(QtCore.QRect(560, 120, 201, 181))
        self.pic2_label.setText("")
        self.pic2_label.setPixmap(QtGui.QPixmap("images/london_streets.jpg"))
        self.pic2_label.setObjectName("pic2_label")
        self.pic1_label = QtWidgets.QLabel(self.centralwidget)
        self.pic1_label.setGeometry(QtCore.QRect(355, 90, 201, 221))
        self.pic1_label.setText("")
        self.pic1_label.setPixmap(QtGui.QPixmap("images/cn_tower_pic.jpg"))
        self.pic1_label.setObjectName("pic1_label")
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setGeometry(QtCore.QRect(350, 350, 450, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.description_label.setFont(font)
        self.description_label.setObjectName("description_label")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 271, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -99, 257, 384))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.report_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.report_button.setObjectName("report_button")
        self.verticalLayout.addWidget(self.report_button)
        self.suggest_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.suggest_button.setObjectName("suggest_button")
        self.verticalLayout.addWidget(self.suggest_button)
        self.vote_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.vote_button.setObjectName("vote_button")
        self.verticalLayout.addWidget(self.vote_button)
        self.profile_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.profile_button.setObjectName("profile_button")
        self.verticalLayout.addWidget(self.profile_button)
        self.myReports_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.myReports_button.setObjectName("myReports_button")
        self.verticalLayout.addWidget(self.myReports_button)
        self.rank_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.rank_button.setObjectName("rank_button")
        self.verticalLayout.addWidget(self.rank_button)
        self.friend_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.friend_button.setObjectName("friend_button")
        self.verticalLayout.addWidget(self.friend_button)
        self.faq_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.faq_button.setObjectName("faq_button")
        self.verticalLayout.addWidget(self.faq_button)
        self.contact_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.contact_button.setObjectName("contact_button")
        self.verticalLayout.addWidget(self.contact_button)
        self.logout_button = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout.addWidget(self.logout_button)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.links_label = QtWidgets.QLabel(self.centralwidget)
        self.links_label.setGeometry(QtCore.QRect(10, 40, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.links_label.setFont(font)
        self.links_label.setObjectName("links_label")
        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 22))
        self.menubar.setObjectName("menubar")
        MainScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        self.statusbar.setObjectName("statusbar")
        MainScreen.setStatusBar(self.statusbar)

        self.retranslateUi_french(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi_english(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Cypress"))
        self.header_label.setText(_translate("TemplateWindow", "CYPRESS                                                                                           City of Toronto"))
        self.go_button.setText(_translate("MainScreen", "Go"))
        self.description_label.setText(_translate("MainScreen", "Keeping Our City Streets Clean and Safe..."))
        self.report_button.setText(_translate("MainScreen", "Report a Problem"))
        self.suggest_button.setText(_translate("MainScreen", "Suggest"))
        self.vote_button.setText(_translate("MainScreen", "Vote"))
        self.rank_button.setText(_translate("MainScreen", "Rankings"))
        self.faq_button.setText(_translate("MainScreen", "FAQ"))
        self.contact_button.setText(_translate("MainScreen", "Contact Us"))
        self.profile_button.setText(_translate("MainScreen", "My Profile"))
        self.myReports_button.setText(_translate("MainScreen", "My Reports"))
        self.friend_button.setText(_translate("MainScreen", "Tell a friend"))
        self.logout_button.setText(_translate("MainScreen", "Logout"))
        self.links_label.setText(_translate("MainScreen", "QUICK LINKS >>"))

    def retranslateUi_french(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Cypress"))
        self.header_label.setText(_translate("TemplateWindow", "CYPRESS                                                                                          Ville de Toronto"))
        self.go_button.setText(_translate("MainScreen", "Aller"))
        self.description_label.setText(_translate("MainScreen", "Garder nos rues de la ville propres et sûres ..."))
        self.report_button.setText(_translate("MainScreen", "Signaler un problème"))
        self.suggest_button.setText(_translate("MainScreen", "Suggérer"))
        self.vote_button.setText(_translate("MainScreen", "Voter"))
        self.rank_button.setText(_translate("MainScreen", "Rankings"))
        self.faq_button.setText(_translate("MainScreen", "FAQ"))
        self.contact_button.setText(_translate("MainScreen", "Nous Contacter"))
        self.profile_button.setText(_translate("MainScreen", "Mon Profil"))
        self.myReports_button.setText(_translate("MainScreen", "Mes Rapports"))
        self.friend_button.setText(_translate("MainScreen", "Dire à un ami"))
        self.logout_button.setText(_translate("MainScreen", "Se Déconnecter"))
        self.links_label.setText(_translate("MainScreen", "LIENS RAPIDES >>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainScreen()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
