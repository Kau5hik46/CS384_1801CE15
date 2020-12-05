import tkinter as tk
import time
import os
from functools import partial
from tkinter import ttk
from question import *
from iohandling import csvhandler
from iohandling import *
from login import *
from timer import *

def set_quiz(i):
	var.set(i)
	global quiz_number
	quiz_number = i

def select_quiz(main_window):
	global quiz_number
	quiz_number = 1
	open_dir(folder_questions)
	global var
	var = tk.IntVar()
	button_quiz = None
	for i in range(1,len(os.listdir())+1):
		button_quiz = tk.Button(
			main_window,
			text = "quiz " + str(i),
			bg = "#541388",
			activebackground = "#2e294e",
			font = ("helvetica", 20),
			justify = "left",
			command = partial(set_quiz, i))
		button_quiz.pack(pady = 5, expand = 'True')
	
	button_quiz.wait_variable(var)
	for widget in main_window.winfo_children():
			widget.destroy()

	quiz_number_name = 'q' + str(quiz_number) + '.csv'

	raw_data = csvhandler(quiz_number_name)
	raw_data.read_from_file()
	open_dir(root_folder)

	global time
	quiz_questions, time, multiplier = quiz(raw_data)
	time *= multiplier

	return quiz_questions

def individual_response(user_data, quiz_number, quiz_questions):
	open_dir(folder_individual)
	filename = 'q' + str(quiz_number) + '_' + user_data[0] + ".csv"
	output = csvhandler()
	output.headers = ["ques_no","question","option1","option2","option3","option4","correct_option","marks_correct_ans","marks_wrong_ans","compulsory","marked_choice","Total","Legend"]
	for question in quiz_questions:
		row = []
		row.append(question.qnum)
		row.append(question.question)
		for x in question.options:
			row.append(x)
		row.append(question.correct)
		for x in question.marks:
			row.append(x)
		row.append(question.compulsory)
		row.append(question.answer)
		output.output_data.append(row)

	legends = ["Correct Choices", "Wrong Choices", "Unattempted", "Marks Obtained", "Total Quiz Marks"]
	Total = [0,0,0,0,0]
	for q in quiz_questions:
		if(q.answer_correct == True):
			Total[0] += 1
		elif(q.answer_correct == False):
			Total[1] += 1
		elif(q.answer_correct == 'skipped'):
			Total[2] += 1
		Total[3] += int(q.obtained_marks)
		Total[4] += int(q.marks[0])

	print(Total)
	i = 0
	for row in zip(Total, legends):
		try:
			output.output_data[i].append(row[0], row[1])
		except:
			new = tuple(('','','','','','','','','','','', row[0], row[1]))
			output.output_data.append(list(new))
		i += 1

	# print(output.output_data)
	output.make_csv(filename)

def display(main_window, background_color, user_data):
	frame_timer = tk.Frame(main_window, background = background_color)
	frame_timer.pack()
	label_timer = tk.Label(
		frame_timer,
		text = "timer",
		font = ("helvetica", 20),
		background = background_color,
		justify = "center"
		)
	label_timer.pack()

	timer(label_timer, time, lambda: end_page(main_window))

	label_roll = label_timer = tk.Label(
		frame_timer,
		text = "Roll: " + str(user_data[1]),
		font = ("helvetica", 20),
		background = background_color,
		justify = "center"
		)
	label_roll.pack(pady = 5)

	label_user = label_timer = tk.Label(
		frame_timer,
		text = "Name: " + str(user_data[0]),
		font = ("helvetica", 20),
		background = background_color,
		justify = "center"
		)
	label_user.pack(pady = 5)

	label_unattempted = tk.Label(
		frame_timer,
		text = "Unattempted Questions: " + str(0),
		font = ("helvetica", 20),
		background = background_color,
		justify = "center"
		)
	label_unattempted.pack()

	return frame_timer, label_unattempted

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
		user_data = lgn.data
		start_quiz(button_start, main_window, background_color, user_data)
	# return lgn.data

def end_page(main_window, quiz_questions, user_data):
	individual_response(user_data, quiz_number, quiz_questions)
	marks_list = [int(x.obtained_marks) for x in quiz_questions]
	total_marks = sum(marks_list)
	try:
		main_window.destroy()
	except:
		pass

def start_quiz(start_button, main_window, background_color, user_data):
	start_button.destroy()
	quiz_questions = select_quiz(main_window)

	i = 0
	unattempted_qs = 0

	frame_timer, label_unattempted = display(main_window, background_color, user_data)
	
	q_list = []
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
		q_list.append(q)
		if not question.answered:
			unattempted_qs += 1
			label_unattempted.config(text = "Unattempted Questions: " + str(unattempted_qs))
		try:
			q.pack_forget()
		except:
			pass
		i += 1
	
	end_page(main_window, quiz_questions, user_data)

def destroy(tkobj):
	tkobj.destroy()
	return None

if __name__ == "__main__":
	database_name = "project1_quiz_cs384.db"
	folder_questions = "quiz_wise_questions"
	folder_responses = "quiz_wise_responses"
	folder_individual = "individual_responses"
	global root_folder
	root_folder = pwd()
	
	main_window = tk.Tk()
	main_window.title("Quiz Portal")
	main_window.geometry("800x600")
	background_color = "#E8C547"
	main_window.config(background = background_color)

	button_start = tk.Button(main_window, text ="Start", bg = "#541388",font = ("Helvetica", 20),command = lambda: login_page(button_start, main_window, background_color))
	button_start.pack(expand = 'True')

	main_window.mainloop()
	try:
		main_window.wait_window(main_window)
		end_page(main_window)
	except:
		pass
