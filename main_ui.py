import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

import FrontScreen #import Ui_FrontScreen
import MainScreen #import Ui_MainScreen
import LoginScreen #import Ui_LoginScreen
import RegisterScreen #import *
import ReportScreen #import Ui_ReportScreen

global language
#This is the array of user information, this array does not include user security questions and answers
userData=[]
userData.append(['John','Landon','1234 SomePlace Crescent','4161234567','johnLandon123','jLandon1234',0]) #For test purposes
userData.append(['Riley', 'Alex', '123 Anywhere Road', '123456789', 'alexRiley', 'pAssword1',0]) #For test purposes
#userData.append(['Briana', 'Alice', '123 Chip', '123456789', 'briChip', 'pass123WORD']) #For testing 

#This array stores security question and answer info about each user (Only needed for register/login purposes)
userQData=[]
userQData.append(["Favourite car?","Honda"]) #For test purposes
userQData.append(["Favourite colour?","Blue"]) #For test purposes
#userQData.append(["Favourite day of the week?","Monday"]) #For testing

#This is the variable that holds the user name of the user currently logged in
#It will be None if no one is logged in
userAccount=None

class MyFrontScreen(QMainWindow):
    def __init__(self):
        global language
        super().__init__()
        self.ui=FrontScreen.Ui_FrontScreen()
        self.ui.setupUi(self)
        language='english'
        self.ui.english_button.clicked.connect(self.eng_clicked)
        self.ui.french_button.clicked.connect(self.fre_clicked)

    def eng_clicked(self):
        self.hide()
        self.next=MyLoginScreen()
        self.next.show()
    
    def fre_clicked(self):
        global language
        language='french'
        self.eng_clicked()

class MyMainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui=MainScreen.Ui_MainScreen()
        self.ui.setupUi(self)
        if language=='french':   self.ui.retranslateUi_french(self)
        else:   self.ui.retranslateUi_english(self)
        self.ui.go_button.clicked.connect(self.go_clicked)

    def go_clicked(self):
        page_btn=[
            self.ui.register_button,
            self.ui.login_button, 
            self.ui.report_button,
            self.ui.contact_button,  
            self.ui.suggest_button, 
            self.ui.vote_button, 
            self.ui.faq_button, 
            self.ui.contact_button ]
        page_obj=[
            MyRegisterScreen(),
            MyLoginScreen(),
            MyReportScreen(),
        ]

        for i in range(len(page_obj)):
            if page_btn[i].isChecked() and i < 3:
                self.hide()
                self.next=page_obj[i]; self.next.show()

class MyLoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui=LoginScreen.Ui_LoginScreen()
        self.ui.setupUi(self)
        if language=='french':   self.ui.retranslateUi_french(self)
        else:   self.ui.retranslateUi_english(self)
        self.ui.login_button.clicked.connect(self.login_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.forgot_button.clicked.connect(self.forgot_clicked)  

    def cancel_clicked(self):
        #if username is not empty =======
        self.hide()
        self.next=MyMainScreen()
        self.next.show()

    def login_clicked(self):
        ## Validate here 
        ## get username and password as strings with - self.username.text() and self.password.text()
        userName=self.ui.username.text()
        password=self.ui.password.text()
        listInfo=[userName,password]

        check=self.isValidLogin(listInfo)
        #if not valid :
        if check!=True:
            #self.notify=LoginScreen.MyNotify(language)
            #self.notify.show()
            msg = QMessageBox()
            if language=="english":
                msg.setWindowTitle("Login Error")
            else:
                msg.setWindowTitle("Erreur d'identification")
            msg.setText(check)
            msg.exec_()
        else:
            self.cancel_clicked()

    def isValidLogin(self,listInfo):
        foundUser=False
        userNum=-1
        
        #Check if the username exists in userData
        for user in userData:
            userNum+=1
            if user[4]==listInfo[0]:
                foundUser=True
                break
            
        if foundUser==False:
            if language=="english":
                return("Username does not currently have an account")
            else:
                return("Le nom d'utilisateur n'a pas de compte actuellement")

        #Check if the user has 3 failed login attemps
        if userData[userNum][6]==3:
            if language=="english":
                return("User is banned due to 3 failed login attempts")
            else:
                return("L'utilisateur est banni en raison de 3 tentatives de connexion infructueuses")

        #Check if the password is correct for the username
        if userData[userNum][5]==listInfo[1]:
            #Put the username as the currently logged in user
            userAccount=listInfo[0]
            return True
        else:
            userData[userNum][6]+=1
            if language=="english":
                return("Incorrect password")
            else:
                return("Mot de passe incorrect")

    def forgot_clicked(self):
        self.SQ=LoginScreen.MyDialog(language)
        #get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
        self.hide()     
        self.SQ.exec_()
        #Check if the question and answer match up to the userName
        username=self.ui.username.text()
        
        #print(self.SQ.ui.security_question.text())
        self.next=MyFrontScreen(); self.next.show()

class MyRegisterScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui=RegisterScreen.Ui_RegisterScreen()
        self.ui.setupUi(self)
        if language=='french':   self.ui.retranslateUi_french(self)
        else:   self.ui.retranslateUi_english(self)
        self.ui.register_button.clicked.connect(self.register_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)  

    def cancel_clicked(self):
        self.hide()
        self.next=MyMainScreen();self.next.show()

    def register_clicked(self):
        ## make new user here. Get user info with
        ## self.ui.first_name.text(), self.ui.last_name.text(), self.ui.address.text(), 
        # for phone number - self.ui.phone_1.text()+self.ui.phone_2.text()+self.ui.phone_3.text() , 
        # self.ui.username.text(), self.ui.password.text()]
        firstName=self.ui.first_name.text()
        lastName=self.ui.last_name.text()
        address=self.ui.address.text()
        phone=self.ui.phone_1.text()+self.ui.phone_2.text()+self.ui.phone_3.text()
        userName=self.ui.username.text()
        password=self.ui.password.text()
        
        #Add the elements to a list that will be added to userData if it is correct
        listInfo=[firstName,lastName,address,phone,userName,password]

        #Send the information into isValidRegister to see if it is valid
        if self.isValidRegister(listInfo)!=True:
            msg = QMessageBox()
            if language=="english":
                msg.setWindowTitle("Registration Error")
            else:
                msg.setWindowTitle("Erreur d'enregistrement")
            msg.setText(self.isValidRegister(listInfo))
            msg.exec_()
        else:
            #self.SQ=RegisterScreen.MyDialog(language)
            #get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
            self.SQ=LoginScreen.MyDialog(language)
            self.hide()
            self.SQ.exec_()
            #Append values to the end of the list
            userQData.append([self.SQ.ui.security_question.text(),self.SQ.ui.security_answer.text()])
            self.cancel_clicked()

    def isValidRegister(self,listInfo):
        foundNum=False  #If a number has been found in the password
        foundUpper=False #If an uppercase letter has been found in password
        foundLower=False #If a lowercase letter has been found in password
        #Make sure no fields are empty, if any are empty return false
        for element in listInfo:
            if len(element)==0:
                if language=="english":
                    return("Not all fields are filled out correctly")
                else:
                    return("Tous les champs ne sont pas remplis correctement")
            
        #If the length of password is less than 8 chars return false
        if len(listInfo[5])<8:
            if language=="english":
                return("Length of password is too short")
            else:
                return("La longueur du mot de passe est trop courte")
            
        #Go through each character in password to check requirements
        for letter in listInfo[5]:
            #Check for a number
            if letter.isnumeric():
                foundNum=True
            #Check for an uppercase letter
            if letter.isupper():
                foundUpper=True
            #Check for an lowercase letter
            if letter.islower():
                foundLower=True

        #Check if the password is valid (field 5)
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

        #If it is not the first element in userData check if the username is free (field 4)
        for user in userData:
            if user[4]==listInfo[4]:
                if language=="english":
                    return("Username is already taken")
                else:
                    return("Le nom d'utilisateur est déjà pris")

        #Since the username is free and the password is valid add it to userData and return true
        userData.append(listInfo)
        return True

class MyReportScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        global language
        self.ui=ReportScreen.Ui_ReportScreen()
        self.ui.setupUi(self)
        if language=='french':   self.ui.retranslateUi_french(self)
        else:   self.ui.retranslateUi_english(self)
        self.ui.report_button.clicked.connect(self.report_clicked)
        self.ui.cancel_button.clicked.connect(self.cancel_clicked)  

    def cancel_clicked(self):
        self.hide()
        self.next=MyMainScreen(); self.next.show()

    def report_clicked(self):
        prblm_str=[
            'Utility Failures',
            'Potholes',
            'City Property Vandalism',
            'Eroded Streets',
            'Tree Collapse',
            'Flooded Streets',
            'Mould and Spore Growth',
            'Garbage or any Other Road Blocking Objects'
        ]
        prblm_btn=[
            self.ui.utilitly_failures_button,
            self.ui.potholes_button,
            self.ui.vandalism_button,
            self.ui.erroded_streets_button,
            self.ui.tree_collapse_button,
            self.ui.flood_button,
            self.ui.mould_button,
            self.ui.road_block_button
        ]
        address=self.ui.address.text()
        for i in range(len(prblm_str)):
            if prblm_btn[i].isChecked():
                promblem=prblm_str[i]
        
        # report problem here with 'address' and 'problem' variables



        self.cancel_clicked()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyFrontScreen()
    w.show()
    sys.exit(app.exec_())
    
