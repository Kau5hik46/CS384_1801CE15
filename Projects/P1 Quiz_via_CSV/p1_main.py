from question import *
from iohandling import csvhandler
from iohandling import *
import multiprocessing as mp

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
for question in quiz_questions:
	terminal("clear")
	timer_thread = mp.Process(target = question.timer, args = (1,))
	question_thread = mp.Process(target = question.display_question, args = ())
	timer_thread.start()
	question_thread.start()
	question_thread.join()
	

