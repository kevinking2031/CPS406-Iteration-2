import sys
import ctypes
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import ContactScreen
import FaqScreen
import FrontScreen
import MainScreen
import LoginScreen
import RegisterScreen
import ReportScreen
import ProfileScreen
import MyReports
import SuggestScreen
import SuggestPopUp
import RankScreen
import VoteScreen
import Share
import SurveyScreen

global language

# This is the array of user information, this array does not include user security questions and answers
global userData
userData = []
userData.append(['John', 'Landon', '1234 SomePlace Crescent', '4161234567', "jLand@gmail.com", \
                 'johnLandon123', 'jLandon1234', 0])  # For test purposes
userData.append(['Riley', 'Alex', '123 Anywhere Road', '123456789', "alexaRiley@hotmail.com", \
                 'alexRiley', 'pAssword1', 0])  # For test purposes
# userData.append(['Briana', 'Alice', '123 Chip', '123456789',briannaMail56@gmail.com,'briChip'\
# , 'pass123WORD',0]) #For testing

# This array stores security question and answer info about each user (Only needed for register/login purposes)
global userQData
userQData = []
userQData.append(["Favourite car?", "Honda"])  # For test purposes
userQData.append(["Favourite colour?", "Blue"])  # For test purposes
# userQData.append(["Favourite day of the week?","Monday"]) #For testing

# This is the variable that holds the user name of the user currently logged in
# It will be None if no one is logged in
global userAccount
userAccount = None

global userReports
userReports = {'johnLandon123': [
    ['Address1', 'Utility Failures'],
    ['Address2', 'Potholes'],
    ['Address3', 'Eroded Streets'],
    ['Address4', 'Tree Collapse'],
    ['Address5', 'Flooded Streets'],
    ['Address6', 'Mould and Spore Growth'],
    ['Address7', 'Garbage or any Other Road Blocking Objects']],

    'PeterPan619': [
        ['Address1', 'Utility Failures'],
        ['Address2', 'Potholes'],
        ['Address3', 'Eroded Streets']]
}  # temporary list for testing please initialise proper list when user logs in where 'johnLandon123' = userAccount(username)

global suggestions
suggestions = {('Address1', 'Utility Failures'): [
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        5],
    [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        3]],

    ('Address2', 'Potholes'): [

        [
            "Urna nunc id cursus metus aliquam eleifend mi in nulla. Scelerisque fermentum dui faucibus in ornare. Venenatis a condimentum vitae sapien pellentesque habitant morbi tristique senectus. Quam adipiscing vitae proin sagittis nisl. Viverra accumsan in nisl nisi scelerisque eu ultrices vitae. Vitae tempus quam pellentesque nec nam aliquam sem et. Mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus. Mauris nunc congue nisi vitae suscipit. Orci dapibus ultrices in iaculis nunc sed augue lacus. Nam at lectus urna duis. Mauris cursus mattis molestie a iaculis at erat pellentesque. Orci eu lobortis elementum nibh tellus molestie. Augue interdum velit euismod in. Praesent elementum facilisis leo vel fringilla est ullamcorper eget. Adipiscing commodo elit at imperdiet dui accumsan. Natoque penatibus et magnis dis parturient montes.",
            20], ["Get a new one", 70]],

    ('Address4', 'Tree Collapse'): [["I don't know", 50], ["Get more Trees", 25]],
    ('Address5', 'Flooded Streets'): [["Not important", 30]],
    ('Address6', 'Mould and Spore Growth'): [],
    ('Address7', 'Garbage or any Other Road Blocking Objects'): [],
    ('Address1', 'Garbage or any Other Road Blocking Objects'): [],
    ('Address2', 'Flooded Streets'): [],
    ('Address3', 'Potholes'): []
}


class MyFrontScreen(QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.ui = FrontScreen.Ui_FrontScreen()
        self.ui.setupUi(self)
        language = 'english'
        self.ui.english_button.clicked.connect(self.eng_clicked)
        self.ui.french_button.clicked.connect(self.fre_clicked)
        # self.ui.faq_button.clicked.connect(self.faq_clicked)

    def eng_clicked(self):
        self.hide()
        self.next = MyLoginScreen()
        self.next.show()

    def fre_clicked(self):
        global language
        language = 'french'
        self.eng_clicked()

class MyMainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui = MainScreen.Ui_MainScreen()
        self.ui.setupUi(self)
        if language == 'french':
            self.ui.retranslateUi_french(self)
        else:
            self.ui.retranslateUi_english(self)
        self.ui.go_button.clicked.connect(self.go_clicked)

    def go_clicked(self):
        global userAccount
        page_btn = [
            self.ui.report_button,
            self.ui.suggest_button,
            self.ui.vote_button,
            self.ui.rank_button,
            self.ui.faq_button,
            self.ui.contact_button,
            self.ui.profile_button,
            self.ui.myReports_button,
            self.ui.friend_button,
            self.ui.survey_button,
            self.ui.logout_button
        ]
        page_obj = [
            MyReportScreen(),
            MySuggestScreen(),
            MyVoteScreen(),
            MyRankScreen(),
            MyFaqScreen(),
            MyContactScreen(),
            MyProfileScreen(),
            None,
            MyShare(),
            MySurveyScreen(),
            MyLoginScreen()
        ]
        if userAccount in userReports:
            page_obj[7] = MyUserReports()

        for i in range(len(page_obj)):
            if page_btn[i].isChecked():
                # if i == 10 logout (do it before netx statements i.e. "self.hide...")
                if i==8:
                    self.hide()
                    self.next=page_obj[8]
                    self.next.exec_()
                    self.show();break
                if i == 10:
                    userAccount = None
                if i == 7 and page_obj[7] is None:
                    msg = QMessageBox()
                    if language == "english":
                        msg.setWindowTitle("Reports List Empty")
                        msg.setText("You must add a report before you can access your reports.")
                    else:
                        msg.setWindowTitle("Liste des rapports vide")
                        msg.setText("Vous devez ajouter un rapport avant de pouvoir accéder à vos rapports.")

                    msg.exec_()
                else:
                    self.hide()
                    self.next = page_obj[i]
                    self.next.show()


class MyLoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        userAccount=None
        self.ui = LoginScreen.Ui_LoginScreen()
        self.ui.setupUi(self)
        if language == 'french':
            self.ui.retranslateUi_french(self)
        else:
            self.ui.retranslateUi_english(self)
        self.ui.login_button.clicked.connect(self.login_clicked)
        self.ui.register_button.clicked.connect(self.register_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.forgot_button.clicked.connect(self.forgot_clicked)
        self.ui.faq_button.clicked.connect(self.faq_clicked)
        self.ui.register_button.clicked.connect(self.register_clicked)

    def cancel_clicked(self):
        self.hide()
        self.next=MyFrontScreen()
        self.next.show()

    def register_clicked(self):
        self.hide()
        self.next = MyRegisterScreen()
        self.next.show()

    def login_clicked(self):
        ## Validate here 
        ## get username and password as strings with - self.username.text() and self.password.text()
        userName = self.ui.username.text()
        password = self.ui.password.text()
        listInfo = [userName, password]
        global userAccount

        check = self.isValidLogin(listInfo)
        # if not valid :
        if check != True:
            # self.notify=LoginScreen.MyNotify(language)
            # self.notify.show()
            msg = QMessageBox()
            if language == "english":
                msg.setWindowTitle("Login Error")
            else:
                msg.setWindowTitle("Erreur d'identification")
            msg.setText(check)
            msg.exec_()
        else:
            userAccount = userName
            self.hide()
            self.next=MyMainScreen()
            self.next.show()

    def register_clicked(self):
        self.hide()
        self.next = MyRegisterScreen();
        self.next.show()

    def isValidLogin(self, listInfo):
        foundUser = False
        userNum = -1

        # Check if the username exists in userData
        for user in userData:
            userNum += 1
            if user[5] == listInfo[0]:
                foundUser = True
                break

        if foundUser == False:
            if language == "english":
                return ("Username does not currently have an account")
            else:
                return ("Le nom d'utilisateur n'a pas de compte actuellement")

        # Check if the user has 3 failed login attemps
        if userData[userNum][7] == 3:
            if language == "english":
                return ("User is banned due to 3 failed login attempts")
            else:
                return ("L'utilisateur est banni en raison de 3 tentatives de connexion infructueuses")

        # Check if the password is correct for the username
        if userData[userNum][6] == listInfo[1]:
            # Put the username as the currently logged in user
            userAccount = listInfo[0]
            return True
        else:
            userData[userNum][7] += 1
            if language == "english":
                return ("Incorrect password")
            else:
                return ("Mot de passe incorrect")

    def forgot_clicked(self):
        userName = self.ui.username.text()
        foundUser = False
        userNum = -1

        # if there is no userName entered, prompt the user to enter a username
        if userName == "":
            msg = QMessageBox()
            if language == "english":
                msg.setWindowTitle("Missing username")
                msg.setText("Please enter a username in the login page to answer a secret question")
            else:
                msg.setWindowTitle("Nom d'utilisateur manquant")
                msg.setText(
                    "Veuillez entrer un nom d'utilisateur dans la page de connexion pour répondre à une question secrète")
            msg.exec_()
        else:
            # Check if the username exists in userData
            for user in userData:
                userNum += 1
                if user[5] == userName:
                    foundUser = True
                    break
            # If it does not exist close this window
            if foundUser == False:
                msg = QMessageBox()
                if language == "english":
                    msg.setWindowTitle("Login Error")
                    msg.setText("Username does not currently have an account")
                else:
                    msg.setWindowTitle("Erreur d'identification")
                    msg.setText("Le nom d'utilisateur n'a pas de compte actuellement")
                msg.exec_()
            # If it does exist find the user question that corresponds
            else:
                # Get the user question
                question = userQData[userNum][0]
                # Display the user question
                self.SQ = LoginScreen.MyDialog(question, language)
                self.SQ.exec_()
                answer = self.SQ.ui.security_answer.text()
                # get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
                # Check to see if answer is correct
                if userQData[userNum][1] == answer:
                    msg = QMessageBox()
                    if language == "english":
                        msg.setWindowTitle("Valid Security Response")
                        msg.setText("Answer is correct. Please check your email for a message with your password.")
                    else:
                        msg.setWindowTitle("Erreur d'identification")
                        msg.setText("Le nom d'utilisateur n'a pas de compte actuellement")
                    msg.exec_()
                    self.hide()
                else:
                    msg = QMessageBox()
                    if language == "english":
                        msg.setWindowTitle("Incorrect Security Response")
                        msg.setText("Security answer is incorrect.")
                    else:
                        msg.setWindowTitle("Erreur d'identification")
                        msg.setText("Le nom d'utilisateur n'a pas de compte actuellement")
                    msg.exec_()
                    self.hide()
                    # Check if the question and answer match up to the userName
                    # username=self.ui.username.text()

                self.next = MyFrontScreen();
                self.next.show()

    def faq_clicked(self):
        self.hide()
        self.next = MyFaqScreen()
        self.next.show()


class MyRegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        userAccount=None
        self.ui = RegisterScreen.Ui_RegisterScreen()
        self.ui.setupUi(self)
        if language == 'french':
            self.ui.retranslateUi_french(self)
        else:
            self.ui.retranslateUi_english(self)
        self.ui.register_button.clicked.connect(self.register_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.faq_button.clicked.connect(self.faq_clicked)

    def cancel_clicked(self):
        if userAccount is not None:
            self.hide()
            self.next = MyMainScreen()
            self.next.show()
        else:
            self.hide()
            self.next = MyFrontScreen()
            self.next.show()

    def register_clicked(self):
        ## make new user here. Get user info with
        ## self.ui.first_name.text(), self.ui.last_name.text(), self.ui.address.text(), 
        # for phone number - self.ui.phone_1.text()+self.ui.phone_2.text()+self.ui.phone_3.text() , 
        # self.ui.username.text(), self.ui.password.text()]
        firstName = self.ui.first_name.text()
        lastName = self.ui.last_name.text()
        address = self.ui.address.text()
        phone = self.ui.phone_1.text() + self.ui.phone_2.text() + self.ui.phone_3.text()
        email = self.ui.email_address.text()
        userName = self.ui.username.text()
        password = self.ui.password.text()

        # Add the elements to a list that will be added to userData if it is correct
        listInfo = [firstName, lastName, address, phone, email, userName, password, 0]

        # Send the information into isValidRegister to see if it is valid
        if self.isValidRegister(listInfo) != True:
            msg = QMessageBox()
            if language == "english":
                msg.setWindowTitle("Registration Error")
            else:
                msg.setWindowTitle("Erreur d'enregistrement")
            msg.setText(self.isValidRegister(listInfo))
            msg.exec_()
        else:
            # self.SQ=RegisterScreen.MyDialog(language)
            # get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
            self.SQ = RegisterScreen.MyDialog(language)
            self.hide()
            self.SQ.exec_()
            # Append values to the end of the list
            sq_lis = [self.SQ.ui.security_question.text(), self.SQ.ui.security_answer.text()]
            if len(sq_lis[0]) > 0 < len(sq_lis[1]):
                userQData.append(sq_lis)
                userAccount = userName
                print(userQData)
                self.cancel_clicked()
            else:
                self.show()
                msg = QMessageBox()
                if language == "english":
                    msg.setWindowTitle("Registration Error")
                    msg.setText("Provide a security question and answer")
                else:
                    msg.setWindowTitle("Erreur d'enregistrement")
                    msg.setText("Fournissez une question de sécurité et une réponse")
                msg.exec_()

    def isValidRegister(self, listInfo):
        foundNum = False  # If a number has been found in the password
        foundUpper = False  # If an uppercase letter has been found in password
        foundLower = False  # If a lowercase letter has been found in password
        # Make sure no fields are empty, if any are empty return false

        for i in range(0, len(listInfo) - 1):
            element = listInfo[i]
            if len(element) == 0:
                if language == "english":
                    return ("Not all fields are filled out correctly")
                else:
                    return ("Tous les champs ne sont pas remplis correctement")

        # for element in listInfo:
        # if len(element)==0:
        # if language=="english":
        # return("Not all fields are filled out correctly")
        # else:
        # return("Tous les champs ne sont pas remplis correctement")

        # If the length of password is less than 8 chars return false
        if len(listInfo[6]) < 8:
            if language == "english":
                return ("Length of password is too short")
            else:
                return ("La longueur du mot de passe est trop courte")

        # Go through each character in password to check requirements
        for letter in listInfo[6]:
            # Check for a number
            if letter.isnumeric():
                foundNum = True
            # Check for an uppercase letter
            if letter.isupper():
                foundUpper = True
            # Check for an lowercase letter
            if letter.islower():
                foundLower = True

        # Check if the password is valid (field 6)
        if (foundNum == False or foundUpper == False or foundLower == False):
            if language == "english":
                return ("Password is missing at least one of the following:\n - 1 number \n - 1 uppercase letter\
                        \n - 1 lowercase letter")
            else:
                return ("Le mot de passe manque au moins l'un des éléments suivants:\n - 1 chiffre \n - 1 lettre majuscule\
                        \n - 1  lettre minuscule")

        # If userData is empty add this as the first element
        if len(userData) == 0:
            userData.append(listInfo)
            return True

        # If it is not the first element in userData check if the username is free (field 5)
        for user in userData:
            if user[5] == listInfo[5]:
                if language == "english":
                    return ("Username is already taken")
                else:
                    return ("Le nom d'utilisateur est déjà pris")

        # Since the username is free and the password is valid add it to userData and return true
        userData.append(listInfo)
        return True

    def faq_clicked(self):
        self.hide()
        self.next = MyFaqScreen()
        self.next.show()


class MyReportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui = ReportScreen.Ui_ReportScreen()
        self.ui.setupUi(self)
        if language == 'french':
            self.ui.retranslateUi_french(self)
        else:
            self.ui.retranslateUi_english(self)
        self.ui.report_button.clicked.connect(self.report_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.hide()
        self.next = MyMainScreen();
        self.next.show()

    def report_clicked(self):
        prblm_str = [
            'Utility Failures',
            'Potholes',
            'City Property Vandalism',
            'Eroded Streets',
            'Tree Collapse',
            'Flooded Streets',
            'Mould and Spore Growth',
            'Garbage or any Other Road Blocking Objects'
        ]
        prblm_btn = [
            self.ui.utilitly_failures_button,
            self.ui.potholes_button,
            self.ui.vandalism_button,
            self.ui.erroded_streets_button,
            self.ui.tree_collapse_button,
            self.ui.flood_button,
            self.ui.mould_button,
            self.ui.road_block_button
        ]
        address = self.ui.address.text()
        for i in range(len(prblm_str)):
            if prblm_btn[i].isChecked() and len(address) != 0:
                promblem = prblm_str[i]

            # Msg Box when all field are not filled for report creation.
            # 			else:
            # 				msg = QMessageBox()
            #                    		if language == "english":
            #                         		msg.setWindowTitle("Report Creation Error")
            #                     		else:
            # 					msg.setWindowTitle("Erreur de création de rapport")
            #                     		msg.exec_()

            if userAccount not in userReports:
                userReports[userAccount] = [[address, promblem]]
        # 			msg = QMessageBox()
        #                    	if language == "english":
        #                         	msg.setWindowTitle("Report Creation")
        #                     	else:
        # 				msg.setWindowTitle("Création de rapports")
        #                     	msg.exec_()

        else:
            userReports[userAccount].append([address, promblem])
        # 			msg = QMessageBox()
        #                    	if language == "english":
        #                         	msg.setWindowTitle("Report Creation")
        #                     	else:
        # 				msg.setWindowTitle("Création de rapports")
        #                     	msg.exec_()

        self.cancel_clicked()


class MyProfileScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        global userData
        global userAccount
        self.userInfo=[]
        for i in range(len(userData)):
            if userData[i][5] == userAccount:	self.userInfo=userData[i]+userQData[i]; break;
        self.ui=ProfileScreen.Ui_ProfileScreen()
        self.ui.setupUi(self)
        #if language=='french':   self.ui.retranslateUi_french(self,self.userInfo)
        #else:   self.ui.retranslateUi_english(self,self.userInfo)
        self.ui.retranslateUi(self,self.userInfo)
        self.ui.edit_button.clicked.connect(self.resetUpUi)
        self.ui.delete_button.clicked.connect(self.delete_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.hide()
        self.next=MyMainScreen(); self.next.show()

    def delete_clicked(self):
        #Make user answer security question from logout page
        #Get the userNum from userData
        userNum=-1
        for user in userData:
            userNum+=1
            if user[5]==userAccount:
                break
        #Get the user question
        question=userQData[userNum][0]
        #Display the user question
        self.SQ=LoginScreen.MyDialog(question, language)
        self.SQ.exec_()
        answer=self.SQ.ui.security_answer.text()
        #get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
        #Check to see if answer is correct
        if userQData[userNum][1]==answer:
            #Then you can ask the user if they want to delete the report
            warn=QMessageBox()
            warn.setIcon(QMessageBox.Warning)
            if language=='french': warn.setText("Voulez-vous vraiment supprimer votre profil?")
            else: warn.setText("Are you sure you want to delete your profile?")
            warn.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            warn.buttonClicked.connect(self.popup_button)
            warn.exec_()
            #userAccount=None
        else:
            msg = QMessageBox()
            if language=="english":
                msg.setWindowTitle("Incorrect Security Response")
                msg.setText("Security answer is incorrect. You may not delete your account at this time.")
            else:
                msg.setWindowTitle("Erreur d'identification")
                msg.setText("La réponse de sécurité est incorrecte. Vous ne pouvez pas supprimer votre compte pour le moment.")
            msg.exec_()
            
    def popup_button(self, btn):
        #Delete profile here if the user clicks yes
        if btn.text()=="&Yes":
            #Get the userNum from userData
            userNum=-1
            for user in userData:
                userNum+=1
                if user[5]==userAccount:
                    break
            #Delete userData with userNum
            del userData[userNum]
            #Delete userQData with userNum
            del userQData[userNum]
            #Return to the main page where userAccount will be equal to 0
            self.hide()
            self.next=MyFrontScreen(); self.next.show()
            

    def resetUpUi(self):
        print("done")
        #print(self.ui.edit_button.text())
        if self.ui.state=='edit':
            self.ui.state='save'
            #self.ui.edit_button.setText("SAVE PROFILE")
            #Prompt the user
            msg = QMessageBox()
            if language=="english":
                msg.setText("All information may be changed except for the following:\n - Username \
                        \n - Security question \n - Security answer")
            else:
                msg.setText("Toutes les informations peuvent être modifiées à l'exception de ce qui suit: \
                            \ n - Nom d'utilisateur \ n - Question de sécurité \n - Réponse de sécurité")
            msg.exec_()
            self.ui.first_name.setReadOnly(False)
            self.ui.last_name.setReadOnly(False)
            self.ui.address.setReadOnly(False)
            self.ui.phone.setReadOnly(False)
            self.ui.email_address.setReadOnly(False)
            self.ui.username.setReadOnly(True)
            self.ui.password.setReadOnly(False)
            self.ui.security_question.setReadOnly(True)
            self.ui.security_answer.setReadOnly(True)
            #Disable the delete button
            self.ui.delete_button.setDisabled(True)
            #if language=='french':   self.ui.retranslateUi_french(self,self.userInfo)
            #else:   self.ui.retranslateUi_english(self,self.userInfo)
            self.ui.retranslateUi(self, self.userInfo)
        else:
            #Save by updating user information
            firstName=self.ui.first_name.text()
            lastName=self.ui.last_name.text()
            address=self.ui.address.text()
            phone=self.ui.phone.text()
            email=self.ui.email_address.text()
            userName=self.ui.username.text()
            password=self.ui.password.text()
            #securQuestion=self.ui.security_question.toPlainText()
            #securAnswer=self.ui.security_answer.toPlainText()
            
            listInfo=[firstName,lastName,address,phone,email,userName,password,0]
            
            check=self.checkReset(listInfo)
            if isinstance(check, str)==True:
                msg = QMessageBox()
                msg.setText(self.checkReset(listInfo))
                msg.exec_()
            else:
                self.ui.state='edit'
                #Tell user changes have been made
                msg = QMessageBox()
                if language=="english":
                    msg.setWindowTitle(" ")
                    msg.setText("Information changed successfully.")
                else:
                    msg.setWindowTitle(" ")
                    msg.setText("Les informations ont été modifiées avec succès.")
                msg.exec_()
                #Go back to the main page
                print(userdata[1])
                #self.cancel_clicked()
            
    def checkReset(self,listInfo):
        foundNum=False  #If a number has been found in the password
        foundUpper=False #If an uppercase letter has been found in password
        foundLower=False #If a lowercase letter has been found in password

        #Make sure no fields are empty, if any are empty return false
        for i in range(0,len(listInfo)-1):
            element=listInfo[i]
            if len(element)==0:
                if language=="english":
                    return("Not all fields are filled out correctly")
                else:
                    return("Tous les champs ne sont pas remplis correctement")
            
        #If the length of password is less than 8 chars return false
        if len(listInfo[6])<8:
            if language=="english":
                return("Length of password is too short")
            else:
                return("La longueur du mot de passe est trop courte")
            
        #Go through each character in password to check requirements
        for letter in listInfo[6]:
            #Check for a number
            if letter.isnumeric():
                foundNum=True
            #Check for an uppercase letter
            if letter.isupper():
                foundUpper=True
            #Check for an lowercase letter
            if letter.islower():
                foundLower=True

        #Check if the password is valid (field 6)
        if (foundNum==False or foundUpper==False or foundLower==False):
            if language=="english":
                return("Password is missing at least one of the following:\n - 1 number \n - 1 uppercase letter\
                        \n - 1 lowercase letter")
            else:
                return("Le mot de passe manque au moins l'un des éléments suivants:\n - 1 chiffre \n - 1 lettre majuscule\
                        \n - 1  lettre minuscule")
            
        #If userData is empty add this as the first element
        if len(userData)==0:
            userData.append(listInfo)
            return True

        #If it is not the first element in userData check if the username is free (field 5)
        for user in userData:
            if user[5]==listInfo[5] and listInfo[5]!=userAccount:
                if language=="english":
                    return("Username is already taken")
                else:
                    return("Le nom d'utilisateur est déjà pris")

        #Get the userNum from userData
        userNum=-1
        for user in userData:
            userNum+=1
            if user[5]==userAccount:
                break
            
        #Since the username is free and the password is valid modify the current userData profile
        for i in range(len(userData)):
            if i==userNum:
                for j in range(7):
                    userData[i][j]=listInfo[j]

        return userNum



    def resetUpUi(self):
        if self.ui.state == 'edit':
            self.ui.first_name.setReadOnly(False)
            self.ui.last_name.setReadOnly(False)
            self.ui.address.setReadOnly(False)
            self.ui.phone.setReadOnly(False)
            self.ui.username.setReadOnly(False)
            self.ui.password.setReadOnly(False)
            self.ui.security_question.setReadOnly(False)
            self.ui.security_answer.setReadOnly(False)
            self.ui.state = 'save'
            self.ui.retranslateUi(self, self.userInfo)
            self.ui.delete_button.setDisabled(True)
        else:
            # save by updating user information
            self.cancel_clicked()


class MyUserReports(QMainWindow):
    def __init__(self):
        super().__init__()
        global userReports
        global userAccount
        self.ui = MyReports.Ui_MyReports()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)
        self.prblm_lis = userReports[userAccount]
        self.clicked_prblm = -1
        buttons = []
        for i in range(len(self.prblm_lis)):
            button = QRadioButton()
            buttons.append(button)
            self.ui.gridLayout.addWidget(buttons[i], i, 0)
            buttons[i].clicked.connect(lambda: self.prblm_clicked(buttons))
            label = QLabel(self.prblm_lis[i][0]);
            label.setWordWrap(True)
            self.ui.gridLayout.addWidget(label, i, 1)
            label = QLabel(self.prblm_lis[i][1]);
            label.setWordWrap(True)
            self.ui.gridLayout.addWidget(label, i, 2)
        self.ui.edit_button.clicked.connect(self.edit_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.delete_button.clicked.connect(self.delete_clicked)

    def prblm_clicked(self, buttons):
        for j in range(len(userReports[userAccount])):
            if buttons[j].isChecked():
                self.clicked_prblm = j

    def edit_clicked(self):
        if self.clicked_prblm >= 0:
            self.hide()
            self.next = MyReportScreen();
            self.next.ui.address.setText(self.prblm_lis[self.clicked_prblm][0])
            self.next.show()

        # check to see if report is in userReports for current user
        if self.prblm_lis[self.clicked_prblm] in userReports[userAccount]:
            userReports[userAccount].remove(self.prblm_lis[self.clicked_prblm])

    def delete_clicked(self):
        if self.clicked_prblm >= 0:
            warn = QMessageBox()
            warn.setIcon(QMessageBox.Warning)
            if language == 'french':
                warn.setText("Voulez-vous vraiment supprimer votre rapport")
            else:
                warn.setText("Are you sure you want to delete your report?")
            warn.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reply = warn.exec_()
            if reply == QMessageBox.Ok:
                if self.prblm_lis[self.clicked_prblm] in userReports[userAccount]:
                    userReports[userAccount].remove(self.prblm_lis[self.clicked_prblm])
        self.hide()
        self.next = MyUserReports()
        self.next.show()

    def cancel_clicked(self):
        self.hide()
        self.next = MyMainScreen();
        self.next.show()


class MyFaqScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        global userAccount
        self.ui = FaqScreen.UI_FaqScreen()
        self.ui.setupUi(self)
        if language == 'french':   self.ui.retranslateUi_french(self)
        self.ui.ok_button.clicked.connect(self.ok_clicked)

    def ok_clicked(self):
        if userAccount is not None:
            self.hide()
            self.next = MyMainScreen()
            self.next.show()
        else:
            self.hide()
            self.next = MyFrontScreen()
            self.next.show()


class MyContactScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui = ContactScreen.UI_ContactScreen()
        self.ui.setupUi(self)
        if language == 'french':   self.ui.retranslateUi_french(self)
        self.ui.ok_button.clicked.connect(self.ok_clicked)

    def ok_clicked(self):
        self.hide()
        self.next = MyMainScreen()
        self.next.show()


class MySuggestPopUp(QDialog):
    def __init__(self, prblm):
        super().__init__()
        global userReports
        global suggestions
        self.ui = SuggestPopUp.Ui_SuggestPopUp()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)
        self.prblm = prblm
        self.ui.problem_label.setText(prblm[1] + " in " + prblm[0])
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.submit_button.clicked.connect(self.submit_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.res = 'CANCEL'
        self.close()

    def back_clicked(self):
        self.res = 'DEL'
        self.close()

    def submit_clicked(self):
        self.res = 'SUB'
        if self.ui.textEdit.toPlainText() != '':
            suggestions[self.prblm].append([self.ui.textEdit.toPlainText(), 0])
            self.close()


class MySuggestScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global userReports
        global suggestions

        self.ui = SuggestScreen.Ui_SuggestScreen()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)

        for i in suggestions:
            frame = QFrame(self.ui.scrollAreaWidgetContents)
            frame.setFrameShape(QFrame.NoFrame)
            gridLayout = QGridLayout(frame)
            suggest_button = QPushButton(frame)

            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0);
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(suggest_button.sizePolicy().hasHeightForWidth())
            suggest_button.setSizePolicy(sizePolicy)
            suggest_button.setMaximumSize(QSize(10000000, 70))

            gridLayout.addWidget(suggest_button, 1, 1, 1, 1)

            label = QLabel(frame)
            font = QFont();
            font.setPointSize(17);
            label.setFont(font)
            label.setFrameShape(QFrame.Panel)
            gridLayout.addWidget(label, 0, 0, 1, 2)
            checkBox = QCheckBox(frame)
            gridLayout.addWidget(checkBox, 1, 0, 1, 1)
            suggest_button.setText("Suggest solution")
            label.setText(i[1] + " in " + i[0])
            label.setWordWrap(True)
            checkBox.setText("Prioritize this problem")

            suggest_button.clicked.connect(partial(self.suggest_clicked, i))
            self.ui.verticalLayout_2.addWidget(frame)

        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.submit_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.close()
        self.next = MyMainScreen();
        self.next.show()

    def suggest_clicked(self, prblm):
        self.hide()
        self.next = MySuggestPopUp(prblm)
        self.next.exec_()
        if self.next.res == 'DEL' or 'SUB':
            self.show()
        else:
            self.cancel_clicked


class MyRankScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global userReports
        global suggestions

        self.ui = RankScreen.Ui_RankScreen()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)
        self.reportsdb = userReports
        self.rankingbd = {}
        self.rankings()
        self.display()
        self.ui.done_button.clicked.connect(self.done_clicked)

    def done_clicked(self):
        self.hide()
        self.next = MyMainScreen();
        self.next.show()

    def rankings(self):
        user_keys = self.reportsdb.keys()
        adrs_count = {}
        prblm_count = {}

        for name in user_keys:
            for num in range(len(self.reportsdb[name])):
                adrs = self.reportsdb[name][num][0]
                prblm = self.reportsdb[name][num][1]

                if adrs not in adrs_count:
                    adrs_count[adrs] = 1

                elif adrs in adrs_count:
                    adrs_count[adrs] += 1

                if prblm not in prblm_count:
                    prblm_count[prblm] = 1

                elif prblm in prblm_count:
                    prblm_count[prblm] += 1

        # sorted from lest to most
        self.adrs_count_sorted = sorted(adrs_count.items(), key=lambda x: x[1])
        self.prblm_count_sorted = sorted(prblm_count.items(), key=lambda x: x[1])

    def display(self):
        for i in range(len(self.prblm_count_sorted)):
            label = QLabel(self.ui.scrollAreaWidgetContents)
            font = QFont()
            font.setPointSize(18)
            label.setFont(font)
            label.setFrameShape(QFrame.WinPanel)
            label.setFrameShadow(QFrame.Raised)
            label.setWordWrap(True)
            self.ui.formLayout.setWidget(i, QFormLayout.LabelRole, label)
            label_2 = QLabel(self.ui.scrollAreaWidgetContents)
            self.ui.formLayout.setWidget(i, QFormLayout.FieldRole, label_2)
            label.setText(self.prblm_count_sorted[i][0])
            label_2.setText('have ' + str(self.prblm_count_sorted[i][1]) + ' total report(s)')

        for i in range(len(self.adrs_count_sorted)):
            label = QLabel(self.ui.scrollAreaWidgetContents_2)
            font = QFont()
            font.setPointSize(18)
            label.setFont(font)
            label.setFrameShape(QFrame.WinPanel)
            label.setFrameShadow(QFrame.Raised)
            label.setWordWrap(True)
            self.ui.formLayout_2.setWidget(i, QFormLayout.LabelRole, label)
            label_2 = QLabel(self.ui.scrollAreaWidgetContents_2)
            self.ui.formLayout_2.setWidget(i, QFormLayout.FieldRole, label_2)
            label.setText(self.adrs_count_sorted[i][0])
            label_2.setText('has' + str(self.adrs_count_sorted[i][1]) + 'total problem(s)')


class MyVoteScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global userReports
        global suggestions

        self.ui = VoteScreen.Ui_VoteScreen()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)
        self.votes = []
        for i in suggestions:
            if suggestions[i] == []: continue;
            # else: print(suggestions[i])
            frame = QFrame(self.ui.scrollAreaWidgetContents)
            frame.setFrameShape(QFrame.StyledPanel);
            frame.setFrameShadow(QFrame.Raised)

            gridLayout = QGridLayout(frame)
            label = QLabel(frame)
            font = QFont();
            font.setPointSize(22)
            label.setFont(font)
            label.setFrameShape(QFrame.WinPanel)
            label.setFrameShadow(QFrame.Raised)
            gridLayout.addWidget(label, 0, 0, 1, 2)
            label.setText(i[1] + " in " + i[0])
            spacerItem = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
            gridLayout.addItem(spacerItem, 1, 0, 1, 1)

            for j in range(len(suggestions[i])):
                frame_2 = QFrame(frame)
                frame_2.setFrameShape(QFrame.NoFrame)
                frame_2.setFrameShadow(QFrame.Plain)
                verticalLayout_2 = QVBoxLayout(frame_2)
                suggest_label = QLabel(frame_2)
                sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0);
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(suggest_label.sizePolicy().hasHeightForWidth())
                suggest_label.setSizePolicy(sizePolicy)
                suggest_label.setMaximumSize(QSize(600, 16777215))
                font = QFont();
                font.setPointSize(12)
                suggest_label.setFont(font)
                suggest_label.setFrameShadow(QFrame.Raised)
                suggest_label.setWordWrap(True)
                suggest_label.setObjectName("suggest_label")
                verticalLayout_2.addWidget(suggest_label)
                checkBox = QCheckBox(frame_2)
                verticalLayout_2.addWidget(checkBox)
                gridLayout.addWidget(frame_2, j + 1, 1, 1, 1)
                self.ui.verticalLayout_6.addWidget(frame)
                checkBox.setText("Like this suggestion")
                suggest_label.setText(suggestions[i][j][0])
                self.votes.append([checkBox, i, j])
        # if submit is clicked and checkbox is checked increase vote by 1
        self.ui.submit_button.clicked.connect(self.submit_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)

    def cancel_clicked(self):
        self.hide()
        self.next = MyMainScreen();
        self.next.show()

    def submit_clicked(self):
        for i, j, k in self.votes:
            if i.isChecked():
                suggestions[j][k][1] += 1
        self.cancel_clicked()
        # print(suggestions)


class MyShare(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Share.Ui_Share()
        self.ui.setupUi(self)
        if language == 'french':   self.ui.retranslateUi_french(self)
        else:   self.ui.retranslateUi_english(self)

        self.ui.pushButton.clicked.connect(self.send_clicked)


    def send_clicked(self):
        self.close()


class MySurveyScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = SurveyScreen.Ui_SurveyScreen()
        self.ui.setupUi(self)
        # if language=='french':   self.ui.retranslateUi_french(self)
        # else:   self.ui.retranslateUi_english(self)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def reject(self):
        self.hide()
        self.next = MyMainScreen()
        self.next.show()

    def accept(self):
        warn = QMessageBox()
        warn.setIcon(QMessageBox.Warning)
        if language == 'french':
            warn.setText("Merci pour votre avis")
        else:
            warn.setText("Thanks for the feedback!")
        warn.exec_()
        self.reject()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyFrontScreen()
    myappid = 'cypress'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    w.show()
    sys.exit(app.exec_())
