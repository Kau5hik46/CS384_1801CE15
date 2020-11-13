import csv
import os
from os import system as terminal

pwd = os.getcwd

def open_dir(directory = ".", pwd = pwd()):
	if(directory == "."):
		return

	try:
		os.chdir(directory)
	except:
		os.mkdir(os.path.join(pwd, str(directory)))
		os.chdir(directory)

	# print(os.getcwd())
	return None

def del_create_grades_folder(directory = "grades", pwd = pwd()):
	for root, dirs, files in os.walk(directory, topdown=False):
		if(directory == '/'):
			print("Dangerous. Stopping right away!")
			return None
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

input_file_path = 'acad_res_stud_grades.csv'

headers = []
raw_data = []
rolls = []
root_folder = pwd()

with open(input_file_path, 'r') as input_file:
	reader = csv.DictReader(input_file)
	headers = reader.fieldnames
	for row in reader:
		raw_data.append(row)

del_create_grades_folder(directory = "grades", pwd = pwd())
open_dir("grades")



def get_rollnumber(row):
	rollnumber = row[headers[1]]
	return rollnumber

def get_row_data(row):
	Roll = row[headers[1]]
	Subject = row[headers[4]]
	Credits = row[headers[5]]
	Type = row[headers[8]]
	Grade = row[headers[6]]
	Sem = row[headers[2]]
	ans = list( (Subject, Credits, Type, Grade, Sem) )
	return ans


def append_row(filename, headers, list_of_elems, individual = True):
	if(os.path.exists(filename)):
		with open(filename, 'a') as output_file:
			writer = csv.writer(output_file, delimiter = ",")
			writer.writerow(list_of_elems)
	else:
		with open(filename, 'w') as output_file:
			writer = csv.writer(output_file, delimiter = ",")
			writer.writerow(headers)
			if(individual == True):
				row1 = ["Semester Wise Details"]
				row2 = ["Subject", "Credits", "Type", "Grade", "Sem"]
				writer.writerow(row1)
				writer.writerow(row2)
			writer.writerow(list_of_elems)

def individual(row):
	rollnumber = get_rollnumber(row)
	roll_head = "Roll: "+ str(rollnumber)
	if(rollnumber not in rolls):
		rolls.append(rollnumber)
	headers = [roll_head]
	filename = str(rollnumber) + "_individual.csv"
	data = get_row_data(row)
	# accepted = ["CORE", "ELECTIVE I", "ELECTIVE II", "ELECTIVE III", "ELECTIVE IV", "HS ELECTIVE", "DEPARTMENTAL ELECTIVE - I", "DEPARTMENTAL ELECTIVE - II","DEPARTMENTAL ELECTIVE - III",]
	try:
		int(data[1])
		int(data[4])
	except:
		filename = "misc.csv"
	if(None in data):
		filename = "misc.csv"
	append_row(filename, headers, data, individual = True)

def grade(alpha):
	dictionary = {"AA": 10, "AB": 9, "BB": 8, "BC": 7, "CC":6, "CD":5, "DD":4, "F": 0,
	"I":0}
	try:
		return dictionary[alpha]
	except:
		return 0

def spi(grades, credits):
	spi = 0
	credits_cleared = 0
	for g, credit in zip(grades, credits):
		spi += grade(g)*credit
		if(grade(g) != 0):
			credits_cleared += credit

	try:
		spi = round(spi/sum(credits), 2)
	except:
		spi = 0 

	return spi, credits_cleared

def cpi(cpi, credits_prev, spi, additional_credits):
	credits_curr = credits_prev + additional_credits
	try:
		cpi = (cpi * credits_prev+ spi * additional_credits)/credits_curr
	except:
		cpi = cpi
	cpi = round(cpi, 2)
	return cpi
   

def semdetails(sem_number, ind_data):
	semester_credits = []
	semester_grades = []
	for row in ind_data:
		if(int(row[4]) == sem_number):
			semester_credits.append(int(row[1]))
			semester_grades.append(row[3])
	SPI, cleared_credits = spi(semester_grades, semester_credits)
	return sem_number, sum(semester_credits), cleared_credits, SPI



def overall(rollnumber):
	open_dir(root_folder)
	open_dir("grades", pwd())
	input_file_path = str(rollnumber) + "_individual.csv"
	grades_dir = os.getcwd()
	ind_data = []
	with open(input_file_path, 'r') as input_file:
		reader = csv.reader(input_file)
		for row in reader:
			ind_data.append(row)
	ind_data.remove(['Semester Wise Details'])
	del ind_data[0]
	ind_data.remove(['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
	# print(ind_data)
	curr_sem = 0
	for row in ind_data:
		row[4] = int(row[4])
		if curr_sem < row[4]:
			curr_sem = row[4]

	overall_data = []
	filename = str(rollnumber) + "_overall.csv"
	header = ["Roll: " + str(rollnumber)]
	new_header = ["Semester", "Semester Credits", "Semester Credits Cleared", "Total Credits", "SPI" "Total Credits Cleared", "CPI"]
	append_row(filename, header, new_header, individual = False)

	for i in range(1,curr_sem+1):
		sem_details = semdetails(i, ind_data)
		sem, total_semester_credits, total_semester_credits_cleared, spi = sem_details
		if(i == 1):
			overall_data = list(sem_details)
			overall_data.append(total_semester_credits)
			overall_data.append(total_semester_credits_cleared)
			overall_data.append(spi)
		else:
			overall_data[0] = i
			overall_data[1] = total_semester_credits
			overall_data[2] = total_semester_credits_cleared
			overall_data[3] = spi
			overall_data[6] = cpi(overall_data[6], overall_data[4], spi, total_semester_credits)
			overall_data[4] += total_semester_credits
			overall_data[5] += total_semester_credits_cleared
		append_row(filename, header, overall_data, individual = False)
			

	# spi_list = []
	# semester_credits = []
	# new_header = ["Semester", "Semester Credits", "Semester Credits Cleared", "Total Credits", "Total Credits Cleared", "CPI"]

	# for row in ind_data:
	# 	course_semester.append(int(row[4]))
	# 	for i in range(1,9):
	# 		if course_semester[-1] == i:
	# 			course_credits.append(int(row[1]))
	# 			course_grade.append(int(row[3]))
				


	
			# course_credits.append(int(row[1]))
			# gr = grade(str(row[3]))
			# grades.append(gr)
			# if(gr > 0):
			# 	credits_cleared.append(int(row[1]))
		

			# SPI, Total_credits_cleared = spi(grades, course_credits)
			# spi_list.append(SPI)
			# credits.append(Total_credits_cleared)
			# CPI = cpi(spi_list, Total_credits_cleared)
			# roll_head = "Roll: "+ str(rollnumber)
			# headers = ["Semester", "Semester Credits", "Semester Credits Cleared", "Total Credits", "Total Credits Cleared", "CPI"]
			# Total_credits = 0
			# for i in credits:
			# 	Total_credits+=i 
			# Total_credits_cleared = 0
			# for i in credits_cleared:
			# 		Total_credits_cleared+=i
			# file_name = str(rollnumber) + "_" + "overall.csv"
			# if(credits_cleared == []):
			# 	credits_cleared.append(0)
			# data = (Semester, course_credits[-1], credits_cleared[-1], Total_credits, Total_credits_cleared, CPI)
			# data = list(data)
			# append_row(file_name, headers, data)
		 

for row in raw_data:
	individual(row)

for rollnumber in rolls:
	overall(rollnumber)


