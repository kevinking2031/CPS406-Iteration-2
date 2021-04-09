from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel


class UI_FaqScreen(object):

    def setupUi(self, FaqScreen):
        FaqScreen.setObjectName("FaqScreen")
        FaqScreen.resize(811, 468)
        FaqScreen.setWindowTitle("Cypress")
        FaqScreen.setWindowOpacity(2.0)
        FaqScreen.setAutoFillBackground(False)
        FaqScreen.setStyleSheet("")
        FaqScreen.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.centralwidget = QtWidgets.QWidget(FaqScreen)
        self.centralwidget.setObjectName("centralwidget")

        header_font = QtGui.QFont()
        header_font.setFamily("FreeSans")
        header_font.setPointSize(15)
        header_font.setBold(True)
        header_font.setWeight(12)

        question_font = QtGui.QFont()
        question_font.setFamily("FreeSans")
        question_font.setPointSize(13)

        answer_font = QtGui.QFont()
        answer_font.setFamily("FreeSans")
        answer_font.setPointSize(11)

        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(10, 5, 800, 50))
        self.Header.setFont(header_font)
        self.Header.setObjectName("Header")

        self.q1 = QtWidgets.QLabel(self.centralwidget)
        self.q1.setGeometry(10, 45, 800, 50)
        self.q1.setFont(question_font)
        self.q1.setObjectName("q1")

        self.a1 = QtWidgets.QLabel(self.centralwidget)
        self.a1.setGeometry(10, 75, 800, 50)
        self.a1.setFont(answer_font)
        self.a1.setObjectName("a1")

        self.q2 = QtWidgets.QLabel(self.centralwidget)
        self.q2.setGeometry(10, 110, 800, 50)
        self.q2.setFont(question_font)
        self.q2.setObjectName("q2")

        self.a2 = QtWidgets.QLabel(self.centralwidget)
        self.a2.setGeometry(10, 140, 800, 50)
        self.a2.setFont(answer_font)
        self.a2.setObjectName("a2")

        self.q3 = QtWidgets.QLabel(self.centralwidget)
        self.q3.setGeometry(10, 175, 800, 50)
        self.q3.setFont(question_font)
        self.q3.setObjectName("q3")

        self.a3 = QtWidgets.QLabel(self.centralwidget)
        self.a3.setGeometry(10, 215, 800, 50)
        self.a3.setFont(answer_font)
        self.a3.setObjectName("a3")

        self.q4 = QtWidgets.QLabel(self.centralwidget)
        self.q4.setGeometry(10, 260, 800, 50)
        self.q4.setFont(question_font)
        self.q4.setObjectName("q4")

        self.a4 = QtWidgets.QLabel(self.centralwidget)
        self.a4.setGeometry(10, 285, 800, 50)
        self.a4.setFont(answer_font)
        self.a4.setObjectName("a4")

        self.q5 = QtWidgets.QLabel(self.centralwidget)
        self.q5.setGeometry(10, 325, 800, 50)
        self.q5.setFont(question_font)
        self.q5.setObjectName("q5")

        self.a5 = QtWidgets.QLabel(self.centralwidget)
        self.a5.setGeometry(10, 350, 800, 50)
        self.a5.setFont(answer_font)
        self.a5.setObjectName("a5")

        self.ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button.setGeometry(QtCore.QRect(702, 423, 89, 25))
        self.ok_button.setObjectName("ok_button")

        FaqScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi_english(FaqScreen)
        QtCore.QMetaObject.connectSlotsByName(FaqScreen)

    def retranslateUi_english(self, FaqScreen):
        _translate = QtCore.QCoreApplication.translate
        FaqScreen.setWindowTitle(_translate("FaqScreen", "Cypress"))
        self.Header.setText(_translate("FaqScreen", "Frequently Asked Questions"))

        self.q1.setText(_translate("FaqScreen", "I've made a mistake on a report, how can I edit it?"))
        self.a1.setText(_translate("FaqScreen", "> After logging into the account you made the report on, you can "
                                                "access the edit report section from the menu."))

        self.q2.setText(_translate("FaqScreen", "My report has been resolved, where can I delete it?"))
        self.a2.setText(_translate("FaqScreen", "> After logging into the account you made the report on, you can "
                                                "access the delete report section from the menu."))

        self.q3.setText(_translate("FaqScreen", "Is there any way to increase the priority on my report?"))
        self.a3.setText(_translate("FaqScreen", "> Our system takes into account various things when prioritizing "
                                                "reports.\n   Please do not submit multiple reports of the same item as"
                                                " we take all reports into account when prioritizing a fix."))

        self.q4.setText(_translate("FaqScreen", "I'd like to change my account credentials, where can I do that?"))
        self.a4.setText(_translate("FaqScreen", "> Once you've logged into your account, you can edit your information "
                                                "using the edit information menu."))

        self.q5.setText(_translate("FaqScreen", "I'd like to speak to someone from support, where can I contact them?"))
        self.a5.setText(_translate("FaqScreen", "> All contact information for support and personnel can be found on "
                                                "the contact page."))

        self.ok_button.setText(_translate("FaqScreen", "OK"))

    def retranslateUi_french(self, FaqScreen):
        _translate = QtCore.QCoreApplication.translate
        FaqScreen.setWindowTitle(_translate("FaqScreen", "Cypress"))
        self.Header.setText(_translate("FaqScreen", "Questions fréquemment posées"))

        self.q1.setText(_translate("FaqScreen", "J'ai fait une erreur sur un rapport, comment puis-je le modifier?"))
        self.a1.setText(_translate("FaqScreen", "> Après vous être connecté au compte sur lequel vous avez rédigé le "
                                                "rapport, vous pouvez accéder à la section \nd'édition du rapport à "
                                                "partir du menu."))

        self.q2.setText(_translate("FaqScreen", "Mon rapport a été résolu, où puis-je le supprimer?"))
        self.a2.setText(_translate("FaqScreen", "> Après vous être connecté au compte sur lequel vous avez effectué le "
                                                "rapport, vous pouvez accéder à la section Supprimer \nle rapport à "
                                                "partir du menu"))

        self.q3.setText(_translate("FaqScreen", "Existe-t-il un moyen d'augmenter la priorité de mon rapport?"))
        self.a3.setText(_translate("FaqScreen", "> Notre système prend en compte diverses choses lors de la "
                                                "priorisation rapports. \nVeuillez ne pas soumettre plusieurs rapports "
                                                "du même élément que nous prenons en compte tous \nles rapports "
                                                "lors de la priorisation d'un correctif."))

        self.q4.setText(_translate("FaqScreen", "Je souhaite modifier les informations d'identification de mon compte, "
                                                "où puis-je faire cela?"))
        self.a4.setText(_translate("FaqScreen", "> Une fois connecté à votre compte, vous pouvez modifier vos "
                                                "informations à l'aide du menu d'édition des informations."))

        self.q5.setText(_translate("FaqScreen", "J'aimerais parler à une personne de l'assistance, où puis-je "
                                                "la contacter?"))
        self.a5.setText(_translate("FaqScreen", "> Toutes les informations de contact pour l'assistance et le personnel"
                                                " sont disponibles sur la page de contact."))

        self.ok_button.setText(_translate("FaqScreen", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FaqScreen = QtWidgets.QMainWindow()
    ui = UI_FaqScreen()
    ui.setupUi(FaqScreen)
    FaqScreen.show()
    sys.exit(app.exec_())
