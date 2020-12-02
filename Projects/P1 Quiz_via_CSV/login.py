import hashlib
from getpass import getpass
from dbhandler import dbhandler

errors = {"wrong_username" :"Invalid username/roll number. Try again.", "wrong_password" : "Please enter correct password"}

class login_item():
	def __init__(self, db = "project1_quiz_cs384.db"):
		self.prompt()
		self.logged_in = False
		self.database_name = db
		self.table_name = "project1_registration"
		self.index_tuples = index_tuples = [("NAME", "TEXT", "NOT NULL"), ("ROLL","TEXT", "PRIMARY KEY","NOT NULL"), ("PASSWORD", "CHAR(64)", "NOT NULL"), ("WHATSAPP", "VARCHAR(12)", "NOT NULL")]
		while self.logged_in == False:
			if(self.action == 'login'):
				self.username = str(input("Enter username(Roll number): "))
				self.password = self.encrypt_password( getpass("Enter the password: "))
				self.password = self.encrypt_password(self.password)
				data = self.login()
				if(data in errors.values()):
					self.prompt('register')

			elif (self.action == 'register'):
				self.register()

	def encrypt_password(self,password):
		hashed_pw = hashlib.sha256(password.encode()).hexdigest()
		return hashed_pw

	def prompt(self, logintype = 'login'):
		action = int(input("Enter 1 for registration and 2 for login and 0 to quit: "))
		if(logintype == 'forgot'):
			self.forgot_password()
		if(action == 1):
			self.action = 'register'
		elif(action == 2):
			self.action = 'login'
		elif action == 0:
			self.quit()
		else:
			self.action = logintype

	def login(self):
		username = (self.username).upper()
		password = self.password
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = dbhandler(database_name, table_name, index_tuples)
		data = None
		try:
			data = table1.select(table_name, username)
			if data == None:
				print(errors["wrong_username"])
				return errors["wrong_username"]
		except:
			print(errors["wrong_username"])
			return errors["wrong_username"]
		
		if data[2] != password:
			print(errors["wrong_password"])
			return errors["wrong_password"]
			self.prompt('forgot')
		else:
			self.logged()
			return data


	def register(self):
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = dbhandler(database_name, table_name, index_tuples)
		name = input("Please Enter your name: ")
		roll = input("Please Enter your Rollnumber (becomes your username): ")
		roll = roll.upper()
		password = None
		confirm = ""
		while password != confirm:
			password = getpass("Enter a password: ")
			confirm = getpass("Re-enter the password: ")
		password = self.encrypt_password(password)
		whatsapp = input("Enter your whatsapp number: ")
		values = list((name, roll, password, whatsapp))
		inserted = table1.insert(table_name, values)
		self.username = roll
		self.password = password
		print(self.password)
		self.login()

	def forgot_password(self):
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = dbhandler(database_name, table_name, index_tuples)
		name = input("Please Enter your name: ")
		roll = input("Please Enter your Rollnumber (becomes your username): ")
		roll = roll.upper()
		password = None
		confirm = ""
		while password != confirm:
			password = getpass("Enter a password: ")
			confirm = getpass("Re-enter the password: ")
		password = self.encrypt_password(password)
		whatsapp = input("Enter your whatsapp number: ")
		values = list((name, roll, password, whatsapp))
		inserted = table1.insert(table_name, values)
		self.username = roll
		self.password = password
		print(self.password)
		self.login()

	def logged(self):
		self.logged_in = True
		return True

	def quit(self):
		pass

lgn = login_item()
print(lgn.logged_in)

