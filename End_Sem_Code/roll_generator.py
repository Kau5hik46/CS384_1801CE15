import random
import os
import csv
import itertools

def padding(original = '', padding_length = 0):
	padded = str(original)
	padded = padded.strip()
	padded = padded.lstrip('0')
	while len(padded) < padding_length:
		padded = '0' + padded

	return padded

course_codes = ['AI', 'AE', 'CC', 'DR']
course_rolls = []
max_seats = 150

for code in course_codes:
	rolls = []
	branch_strength = random.randint(15, max_seats)
	for i in range(0, branch_strength):
		try:
			roll = "2001" + str(code) + padding(str(i), len(str(branch_strength)))
			rolls.append(roll)
		except:
			pass
	course_rolls.append(rolls)

header = course_codes

def append_row(filename, headers, list_of_elems):
		if(os.path.exists(filename)):
			with open(filename, 'a') as output_file:
				writer = csv.writer(output_file, delimiter = ",")
				writer.writerow(list_of_elems)
		else:
			with open(filename, 'w') as output_file:
				writer = csv.writer(output_file, delimiter = ",")
				writer.writerow(headers)
				writer.writerow(list_of_elems)

write_to_csv = input("write to csv file (writes by default) ?: (Y/N)")
filename = "Random Roll Numbers.csv"
for root, dirs, files in os.walk(".", topdown=False):
	if filename in files:
		os.remove(os.path.join(os.getcwd(), filename))
if(write_to_csv.upper() != 'N'):
	transpose = itertools.zip_longest(*course_rolls, fillvalue = None)
	for row in transpose:
		append_row(filename, header, row)





