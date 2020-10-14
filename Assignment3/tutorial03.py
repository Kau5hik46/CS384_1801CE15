import csv
import os
from os import system as terminal

# Imported necessary modules captured data from input_file
input_file_path = 'studentinfo_cs384.csv'

headers = []
raw_data = []

with open(input_file_path, 'r') as input_file:
	reader = csv.DictReader(input_file)
	headers = reader.fieldnames
	for row in reader:
		raw_data.append(row)

pwd = os.getcwd()

def open_dir(directory = ".", pwd = os.getcwd()):
	if(directory == "."):
		return

	try:
		os.chdir(directory)
	except:
		os.mkdir(os.path.join(pwd, str(directory)))
		os.chdir(directory)

	print(os.getcwd())
	return None

def get_ydc(row):
	student_id = row[headers[0]]
	y,d,c = None, None, None
	if(len(student_id) == 8):
   		try:
   			y = int(student_id[0:2])
   			d = student_id[2:4]
   			c = student_id[4:6]
   		except:
   			pass
   		
	return (y,d,c)

def append_row(filename, list_of_elems):
	if(os.path.exists(filename)):
		with open(filename, 'a') as output_file:
			writer = csv.writer(output_file, delimiter = ",")
			writer.writerow(list_of_elems)
	else:
		with open(filename, 'w') as output_file:
			writer = csv.writer(output_file, delimiter = ",")
			writer.writerow(headers)
			writer.writerow(list_of_elems)


def course():
	open_dir("analytics")
	open_dir("course")
	course_dir = os.getcwd()

	courses = set()
	years = set()
	degrees = {"01" : "btech", "11" : 'mtech', "12" : 'msc', "21" : 'phd'}

	for row in raw_data:
		year,degree,course = get_ydc(row)
		years.add(year)
		courses.add(course)

	for row in raw_data:
   		year,degree,course = get_ydc(row)
   		if(year == None or degree == None or course == None):
   			append_row("misc.csv", row.values())
   			continue
   		open_dir(course.lower(), os.getcwd())
   		open_dir(degrees[degree].lower(), os.getcwd())
   		filename = str(year).lower() + "_" + str(course).lower() + "_" + str(degrees[degree]).lower() + ".csv"
   		append_row(filename, row.values())
   		open_dir(course_dir)



def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

course()

