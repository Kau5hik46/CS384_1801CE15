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

def del_create_analytics_folder(directory = "analytics", pwd = pwd()):
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

del_create_analytics_folder()
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
    open_dir(root_folder)
    open_dir("state", pwd())
    states = set()

    for row in raw_data:
    	state = row[headers[7]]
    	states.add(state)
    	filename = str(state).lower() + ".csv"
    	append_row(filename, row.values())

    return states


def blood_group():
    open_dir(root_folder)
    open_dir("blood_group", pwd())
    blood_groups = set()

    for row in raw_data:
    	blood_group = row[headers[6]]
    	blood_groups.add(blood_group)
    	filename = str(blood_group).lower() + ".csv"
    	append_row(filename, row.values())

    return blood_groups


def Sort(new_data): 
	return(sorted(new_data, key = lambda x: x[1]))  


# Create the new file here and also sort it in this function only.
def new_file_sort():
	open_dir(root_folder)
	new_data = [list(x.values()) for x in raw_data]
	del headers[1]
	headers.insert(1, "first_name")
	headers.insert(2, "last_name")
	filename_1 = "studentinfo_cs384_names_split.csv"
	for row in new_data:
		full_name = row[1]
		names = full_name.split(" ", 1)
		first_name = names[0]
		last_name = names[1]
		del row[1]
		row.insert(1, first_name)
		row.insert(2, last_name)
		append_row(filename_1, row)

	sorted_data = Sort(new_data)
	filename_2 = "studentinfo_cs384_names_split_sorted_first_name.csv"
	for row in sorted_data:
		append_row(filename_2, row)

