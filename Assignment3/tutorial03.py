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

def del_directory(directory = ".", pwd = pwd()):
	for root, dirs, files in os.walk(directory, topdown=False):
		if(directory == '/'):
			print("Dangerous. Stopping right away!")
			return None
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

# Imported necessary modules captured data from input_file
input_file_path = 'studentinfo_cs384.csv'

headers = []
raw_data = []

with open(input_file_path, 'r') as input_file:
	reader = csv.DictReader(input_file)
	headers = reader.fieldnames
	for row in reader:
		raw_data.append(row)

del_directory("analytics")
open_dir("analytics")

root_folder = pwd()

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
	open_dir(root_folder)
	open_dir("course", pwd())
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

	return(courses, years, degrees)


def country():
	open_dir(root_folder)
	open_dir("country", pwd())
	countries = set()
	for row in raw_data:
		country = row[headers[2]]
		countries.add(country)
		filename = str(country).lower() + ".csv"
		append_row(filename, row.values())

	return countries

def email_domain_extract():
    open_dir(root_folder)
    open_dir("email_domain", pwd())
    domains = set()
    for row in raw_data:
    	email = row[headers[3]]
    	start_pos = email.find('@')
    	start_pos += 1
    	end_pos = email.find('.')
    	domain = email[start_pos:end_pos]
    	domains.add(domain)
    	filename = str(domain).lower() + ".csv"
    	append_row(filename, row.values())

    return domains

def gender():
    open_dir(root_folder)
    open_dir("gender", pwd())
    genders = set()

    for row in raw_data:
    	gender = row[headers[4]]
    	genders.add(gender)
    	filename = str(gender).lower() + ".csv"
    	append_row(filename, row.values())

    return genders


def dob():
    open_dir(root_folder)
    open_dir("dob", pwd())
    dobs = [1995,2000,2005,2010,2015]

    for row in raw_data:
    	dob = row[headers[5]]
    	year = int(dob[-4:])
    	if(year == 2020):
    		year = 2015
    	try:
    		year = dobs[((year%1995)//5)]
    		if(year != 2015):
    			filename = "bday_" + str(year) + "_" + str(year+4) + ".csv"
    		else:
    			filename = "bday_" + str(year) + "_" + str(year+5) + ".csv"
    	except:
    		filename = "misc.csv" 
    	
    	append_row(filename, row.values())

    return dobs


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
country()
email_domain_extract()
gender()
dob()

