from os import getcwd as pwd
from question import Question
from iohandling import csvhandler
from iohandling import open_dir, del_folder

database_name = "project1_quiz_cs384.db"
folder_questions = "quiz_wise_questions"
folder_responses = "quiz_wise_responses"
folder_individual = "individual_responses"

quiz = csvhandler()

