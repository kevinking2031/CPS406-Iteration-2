# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RankScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RankScreen(object):
    def setupUi(self, RankScreen):
        RankScreen.setObjectName("RankScreen")
        RankScreen.resize(829, 475)
        RankScreen.setWindowIcon(QtGui.QIcon('images/cypress_logo.png'))
        self.centralwidget = QtWidgets.QWidget(RankScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.problem_tab = QtWidgets.QWidget()
        self.problem_tab.setObjectName("problem_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.problem_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.problem_description = QtWidgets.QLabel(self.problem_tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.problem_description.setFont(font)
        self.problem_description.setWordWrap(True)
        self.problem_description.setObjectName("problem_description")
        self.verticalLayout_2.addWidget(self.problem_description)
        self.scrollArea = QtWidgets.QScrollArea(self.problem_tab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 785, 326))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName("formLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.problem_tab, "")
        self.address_tab = QtWidgets.QWidget()
        self.address_tab.setObjectName("address_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.address_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.address_description = QtWidgets.QLabel(self.address_tab)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.address_description.setFont(font)
        self.address_description.setWordWrap(True)
        self.address_description.setObjectName("address_description")
        self.verticalLayout_3.addWidget(self.address_description)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.address_tab)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scrollArea_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 785, 326))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.address_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.done_button = QtWidgets.QPushButton(self.centralwidget)
        self.done_button.setGeometry(QtCore.QRect(290, 410, 89, 25))
        self.done_button.setObjectName("done_button")
        self.verticalLayout.addWidget(self.done_button)
        RankScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RankScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 22))
        self.menubar.setObjectName("menubar")
        RankScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RankScreen)
        self.statusbar.setObjectName("statusbar")
        RankScreen.setStatusBar(self.statusbar)

        self.retranslateUi(RankScreen)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RankScreen)

    def retranslateUi(self, RankScreen):
        _translate = QtCore.QCoreApplication.translate
        RankScreen.setWindowTitle(_translate("RankScreen", "Cypress"))
        self.problem_description.setText(_translate("RankScreen", "Problem with the most reports ranked in ascending order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.problem_tab), _translate("RankScreen", "Problem Rankings"))
        self.address_description.setText(_translate("RankScreen", "Places with the most reports ranked in ascending order"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.address_tab), _translate("RankScreen", "Address Rankings"))
        self.done_button.setText(_translate("RankScreen", "Done"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RankScreen = QtWidgets.QMainWindow()
    ui = Ui_RankScreen()
    ui.setupUi(RankScreen)
    RankScreen.show()
    sys.exit(app.exec_())
