import time
import tkinter as tk
from functools import partial
from os import system as terminal
current = time.time

class Question():
	def __init__(self, number, q, options, correct, marks, comp = 'n'):
		self.qnum = number

		self.question = str(q)
		if(self.question[-1] != '?'):
			self.question += '?'

		self.options = list(options)
		self.marks = tuple(marks)
		self.obtained_marks = 0
		self.correct = correct
		self.answered = False
		self.answer_correct = 'unattempted'
		self.obtained_marks = 0
		self.answer = 0

		if comp.upper() == 'Y':
			self.compulsory = "Yes"
			self.comp = True
		else:
			self.compulsory = "No"
			self.comp = False

	def display_question(self):
		print("Question ", self.qnum, ") ", self.question)
		i = 1
		for opt in self.options:
			print("Option ", i, ") ", opt)
			i += 1
		print()
		print("Credits if correct option: ", self.marks[0])
		print("Negative Marking: ", self.marks[1])
		print("Is compulsory: ", self.compulsory)
		self.marking()

	def display_question_gui(self, main_window, background_color,del_label):
		label_question = tk.Label(
			main_window,
			text = str(self.qnum) + ")" + self.question + "\nCompulsory Question?: " + self.compulsory,
			font = ("helvetica", 25),
			background = background_color,
			width = 500,
			justify = "center",
			wraplength = 400)

		buttons_options = []

		for opt in self.options:
			option = tk.Button(
				main_window,
				text = opt,
				bg = "#541388",
				activebackground = "#2e294e",
				font = ("helvetica", 20),
				justify = "left",
				command = partial(self.marking_gui, opt, del_label))
			buttons_options.append(option)

		skip_option = tk.Button(
			main_window,
			text = "Skip this question",
			font = ("helvetica", 20),
			bg = "#541388",
			activebackground = "#d90368",
			justify = "left",
			command = partial(self.marking_gui, "Skip this question", del_label))
		buttons_options.append(skip_option)

		return label_question, buttons_options

	def marking(self):
		self.answer = input("Enter Choice: 1,2,3,4,S : S is to skip question: ")
		try:
			self.answer = int(self.answer)
		except:
			self.answer = str(self.answer)
		acceptable = [1,2,3,4,'S']
		while self.answer not in acceptable:
			self.answer = input("Enter Choice: 1,2,3,4,S : S is to skip question: ")

		if(self.answer == self.correct):
			self.obtained_marks = self.marks[0]
		elif self.answer == 'S' and not self.comp :
			self.obtained_marks = 0
		else:
			self.obtained_marks = self.marks[1]

		return self.obtained_marks

	def marking_gui(self, option, del_label):
		self.answered = True
		self.answer = option
		if(self.options[int(self.correct)-1] == option):
			self.answer_correct = True
			self.obtained_marks = self.marks[0]
		elif option == "Skip this question" and not self.comp :
			self.answer_correct = 'skipped'
			self.obtained_marks = 0
			self.answered = False
		elif option == "Skip this question" and self.comp :
			self.answer_correct = 'skipped'
			self.obtained_marks = self.marks[1]
			self.answered = False
		else:
			self.answer_correct = False
			self.obtained_marks = self.marks[1]
		del_label()
		return self.obtained_marks

	def decrement(self):
		time.sleep(1)
		self.time_remaining -= 1

	def timer(self, total_minutes = None):
		if total_minutes != None:
			self.time_remaining  = total_minutes * 60
		while self.time_remaining > 0:
			self.decrement()
			self.minutes = self.time_remaining // 60
			self.seconds = self.time_remaining % 60
		return self.minutes, self.seconds

	def timer_gui(self, details_frame, background_color = 'white',total_minutes = None):
		if total_minutes != None:
			self.time_remaining  = total_minutes * 60
		# while self.time_remaining > 0:
			# self.decrement()
		self.minutes = self.time_remaining // 60
		self.seconds = self.time_remaining % 60
		self.label_minutes = tk.Label(
			details_frame,
			text = "Timer: " + str(self.minutes),
			font = ("helvetica", 20),
			background = background_color,
			justify = "center"
			)
		self.label_seconds = tk.Label(
			details_frame,
			text = ":" + str(self.seconds),
			font = ("helvetica", 20),
			background = background_color,
			justify = "center"
			)
		return self.time_remaining, self.label_minutes, self.label_seconds

def total_marks(current_marks, obtained_marks):
	return current_marks + obtained_marks

def marking(quiz_questions):
	pass

def quiz(raw_data):
	quiz_questions = []
	for quest in raw_data.input_data:
		quest.pop(-1)
		number = quest[0]
		q = quest[1]
		options = quest[2:6]
		correct = quest[6]
		marks = tuple(quest[7:9])
		comp = quest[-1]
		question = Question(number, q, options, correct, marks, comp)
		quiz_questions.append(question)
	time = raw_data.headers[-1]
	time = time.split("=")[-1]
	time = time.strip()
	unit = time[-1]
	time = time.strip(unit)
	time = int(time)
	if(unit == 'h'):
		multiplier = 3600
	elif(unit == 'm'):
		multiplier = 60
	elif(unit == 's'):
		multiplier = 1
	return quiz_questions, time, multiplier
