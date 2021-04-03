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
		self.next=MyMainScreen(); self.next.show()

	def login_clicked(self):
		## Validate here 
		## get username and password as strings with - self.username.text() and self.password.text()
		
		#if not valid :
		self.notify=LoginScreen.MyNotify(language)
		self.notify.show()
		#else:
		#self.cancel_clicked()

	def forgot_clicked(self):
		self.SQ=LoginScreen.MyDialog(language)
		#get info with : self.SQ.ui.security_answer.text() and self.SQ.ui.security_question.text()
		self.hide()		
		self.SQ.exec_()
		print(self.SQ.ui.security_question.text())
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

		self.SQ=RegisterScreen.MyDialog(language)
		self.hide()
		self.SQ.exec_()

		self.cancel_clicked()

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
	
