import tkinter as tk
import time
from functools import partial
from tkinter import ttk
from question import *
from iohandling import csvhandler
from iohandling import *
from login import *
from timer import *

def display(main_window, background_color):
	frame_timer = tk.Frame(main_window, background = background_color)
	frame_timer.pack()
	label_timer = tk.Label(
		frame_timer,
		text = "timer",
		font = ("helvetica", 40),
		background = background_color,
		justify = "center"
		)
	label_timer.pack()
	timer(label_timer, 10, lambda: end_page(main_window))
	return frame_timer

def login_page(start_button,main_window, background_color):
	destroy(start_button)
	lgn = login_item()
	lgn.main_window = main_window
	lgn.background_color = background_color
	login_window = tk.Frame(main_window, background = background_color)
	login_window.pack(expand = 'True')
	lgn.login_window = login_window
	x = lgn.get_info_gui(login_window, background_color)
	try:
		main_window.wait_window(lgn.login_window)
	except:
		pass
	if(lgn.logged_in == True):
		login_window.pack_forget()
		start_quiz(button_start, quiz_questions, main_window, background_color)
	# return lgn.data

def end_page(main_window):
	try:
		main_window.destroy()
	except:
		pass

def start_quiz(start_button, quiz_questions, main_window, background_color):
	start_button.destroy()
	i = 0

	frame_timer = display(main_window, background_color)

	for question in quiz_questions:
		try:
			q = tk.Frame(main_window, background = background_color)
			q.pack(side = "top", expand = 'True')
		except:
			pass
		
		label_question, buttons_options = question.display_question_gui(q, background_color,lambda: destroy(label_question))
		label_question.pack()
		for option in buttons_options:
			option.pack(expand = 'True', padx = 50, pady = (10,10))
		q.wait_window(label_question)
		try:
			q.pack_forget()
		except:
			pass
		i += 1
	
	end_page(main_window)

def destroy(tkobj):
	tkobj.destroy()
	return None

database_name = "project1_quiz_cs384.db"
folder_questions = "quiz_wise_questions"
folder_responses = "quiz_wise_responses"
folder_individual = "individual_responses"
quiz_number = "q1.csv"

root_folder = pwd()
open_dir(folder_questions)
raw_data = csvhandler(quiz_number)
raw_data.read_from_file()
open_dir(root_folder)

quiz_questions = quiz(raw_data)

# global main_window
main_window = tk.Tk()
main_window.geometry("800x600")
background_color = "#E8C547"
main_window.config(background = background_color)

button_start = tk.Button(main_window, text ="Start", bg = "#541388",font = ("Helvetica", 20),command = lambda: login_page(button_start, main_window, background_color))
button_start.pack(expand = 'True')

main_window.mainloop()
try:
	main_window.wait_window(main_window)
except:
	pass

end_page(main_window)


