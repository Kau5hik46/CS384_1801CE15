import hashlib
from getpass import getpass
from dbhandler import dbhandler
from functools import partial
import tkinter as tk

errors = {"wrong_username" :"Invalid username/roll number. Try again.", "wrong_password" : "Please enter correct password"}

class login_item():
	def __init__(self, db = "project1_quiz_cs384.db"):
		self.logged_in = False
		self.database_name = db
		self.table_name = "project1_registration"
		self.index_tuples = index_tuples = [("NAME", "TEXT", "NOT NULL"), ("ROLL","TEXT", "PRIMARY KEY","NOT NULL"), ("PASSWORD", "CHAR(64)", "NOT NULL"), ("WHATSAPP", "VARCHAR(12)", "NOT NULL")]
		self.table = dbhandler(self.database_name, self.table_name, self.index_tuples)
		
	def get_info(self):
		self.prompt()
		while self.logged_in == False:
			if(self.action == 'login'):
				self.username = str(input("Enter username(Roll number): ")).upper()
				self.password = self.encrypt_password( getpass("Enter the password: "))
				data = self.login()
				if(data in errors.values()):
					self.prompt('register')
			elif (self.action == 'register'):
				self.register()

	def get_info_gui(self, main_window, background_color = 'white'):
		self.label_username = tk.Label(
			main_window,
			text = "Username",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_username = tk.Entry(main_window, width=15)
		self.label_password = tk.Label(
			main_window,
			text = "Password",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_password = tk.Entry(main_window, show="*", width=15)

		self.button_login = tk.Button(
			main_window,
			text = "login",
			bg = "#541388",
			activebackground = "#2e294e",
			font = ("helvetica", 14),
			justify = "left",
			command = self.login_button_function)
		self.button_register = tk.Button(
			main_window,
			text = "register",
			bg = "#541388",
			activebackground = "#2e294e",
			font = ("helvetica", 14),
			justify = "left",
			command = partial(self.register_button_function, main_window, background_color))
		self.label_username.pack()
		self.field_username.pack()
		self.label_password.pack()
		self.field_password.pack()
		self.button_login.pack()
		self.button_register.pack()

		main_window.wait_window(self.button_login)

		return self.logged_in
		
	def login_button_function(self):
		self.username = self.field_username.get()
		self.password = self.encrypt_password(self.field_password.get())
		return self.login()

	def register_button_function(self, main_window, background_color = 'white'):
		self.button_login.destroy()
		main_window.destroy()
		main_window = tk.Frame(self.main_window, background = self.background_color)
		main_window.pack()
		self.label_register_username = tk.Label(
			main_window,
			text = "Enter your username",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_register_username = tk.Entry(main_window, width=15)
		self.label_register_name = tk.Label(
			main_window,
			text = "Enter your name",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_register_name = tk.Entry(main_window, width=15)
		self.label_register_whatsapp = tk.Label(
			main_window,
			text = "Enter your whatsapp number",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_register_whatsapp = tk.Entry(main_window, width=15)
	
		self.label_register_password = tk.Label(
			main_window,
			text = "Enter your Password",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_register_password = tk.Entry(main_window, show="*", width=15)
		self.label_register_confirm = tk.Label(
			main_window,
			text = "Enter your Password",
			font = ("helvetica", 20),
			background = background_color,
			justify = "center")
		self.field_register_confirm = tk.Entry(main_window, show="*", width=15)

		self.button_register_details = tk.Button(
			main_window,
			text = "complete registration",
			bg = "#541388",
			activebackground = "#2e294e",
			font = ("helvetica", 14),
			justify = "left",
			command = partial(self.register_gui, main_window, background_color))

		self.label_register_username.pack()
		self.field_register_username.pack()
		self.label_register_name.pack()
		self.field_register_name.pack()
		self.label_register_whatsapp.pack()
		self.field_register_whatsapp.pack()
		self.label_register_password.pack()
		self.field_register_password.pack()
		self.label_register_confirm.pack()
		self.field_register_confirm.pack()
		self.button_register_details.pack()
		main_window.wait_window(self.button_register_details)

	def register_gui(self,main_window, background_color = 'white'):
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = self.table
		roll = self.field_register_username.get()
		roll = roll.upper()
		name = self.field_register_name.get()
		password = self.field_register_password.get()
		confirm = self.field_register_confirm.get()
		if(password != confirm):
			return False
		password = self.encrypt_password(password)
		whatsapp = self.field_register_whatsapp.get()
		values = list((name, roll, password, whatsapp))
		inserted = table1.insert(table_name, values)
		self.username = roll
		self.password = password
		result = self.login()

		if self.logged_in == True:
			self.button_register_details.destroy()
			main_window.destroy()
		else:
			print("changing details")
			self.change_details(main_window, roll, name, whatsapp, password, confirm)

		try:
			main_window.wait_window(self.button_register_details)
		except:
			pass
		return result

	def encrypt_password(self,password):
		hashed_pw = hashlib.sha256(password.encode()).hexdigest()
		return hashed_pw

	def prompt(self, logintype = 'login'):
		action = int(input("Enter 1 for registration, 2 for login, 3 for changing personal details and 0 to quit: "))
		if(action == 3):
			self.action = 'forgot'
			self.change_details()
		elif(action == 1):
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
		table1 = self.table
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
			self.data = data
			return data

	def register(self):
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = self.table
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

	def change_details(self, main_window,roll = None, name = None, whatsapp = None, password = None, confirm = None): #provides with an option to update the current details
		database_name = self.database_name
		table_name = self.table_name
		index_tuples = self.index_tuples
		table1 = self.table
		if(roll == None):
			print("Type new value for the field you want to update(Roll number is fixed)")
			roll = input("Please Enter your username/Rollnumber: ")
			self.table.select(table_name, roll)
			name = input("Please Enter new/old name: ")
			whatsapp = input("Enter your new/old whatsapp number: ")
			roll = roll.upper()
			password = None
			confirm = ""
			while password != confirm:
				password = getpass("Enter new/old password: ")
				confirm = getpass("Re-enter the new/old password: ")
			password = self.encrypt_password(password)

		old_values = list((name, roll, password, whatsapp))
		i = 0
		for ans in old_values:
			column = index_tuples[i][0]
			updated = table1.update(table_name, column, old_values[i], old_values[1], "ROLL")
			if updated == None:
				print(errors["wrong_username"])
				self.__init__()
			i += 1

		self.username = roll
		self.password = password
		result = self.login()

		if self.logged_in == True:
			self.button_register_details.destroy()
			main_window.destroy()
		else:
			print("changing details")
			self.change_details(roll, name, whatsapp, password, confirm)

		try:
			main_window.wait_window(main_window)
		except:
			pass
		return result
		# return self.login()
		# self.data = updated

	def logged(self): # Changes state to logged in
		self.logged_in = True
		self.login_window.destroy()
		return True

	def quit(self): #complete using shortcuts
		pass

if __name__ == "__main__":
	lgn = login_item()
	lgn.get_info()
	print(lgn.logged_in)

