I have done a sizeable amount of the login and register screens, I have also started other pages but thought it was best to finish
these two first as may need them to start. I will continue to update the code in the coming week.

I ended up using pyqt5 for the gui so if you want to run the gui, you can use either of the following commands to install pyqt5:

	pip install PyQt5 or pip3 install PyQt5

At this point, I haven't connected the windows so to view each one, you should run them:
	
	python LoginScreen.py or python3 LoginScreen.py

At this point, to get the information from the UI, you should use the following code:

	from LoginScreen import Ui_LoginScreen
	from RegisterScreen import Ui_RegisterScreen

	Ui_RegisterScreen.getInfo() - This returns a list containing the user info when they are registering in the form:

		[First name, Last name, Address, Phone number, Username, password], Example:
			
			['John', 'Landon', '1234 SomePlace Crescent', '4161234567', 'johnLandon123', 'jLandon1234']

		I don't think this is the best practice, I suggest that we create a new object of let's say user class each time we click the register button and store the 			object somewhere. But that is just my suggestion and as I don't know how we are storing/representing data yet, I thought this should do for now.

	Ui_LoginScreen.getInfo() - This returns a list containing the user info when they login in the form:

		[Username, password], Example:
			
			['johnLandon123', 'jLandon1234']

		Again, I don't think this is the best practice, I suggest that we validate the information when we click the login button and go from there. But this should do 		for now.

