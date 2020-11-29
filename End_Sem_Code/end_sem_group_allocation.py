import math
import os
import csv
import copy
from os import system as terminal
import time

pwd = os.getcwd

def open_dir(directory = ".", pwd = pwd()):
	if(directory == "."):
		return
	try:
		os.chdir(os.path.join(pwd, str(directory)))
	except:
		os.mkdir(os.path.join(pwd, str(directory)))
		os.chdir(directory)

	return None

def del_folder(directory = "Groups", pwd = pwd()):
	for root, dirs, files in os.walk(directory, topdown=False):
		if(directory == '/'):
			print("Dangerous. Stopping right away!")
			return None
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

def padding(original = '', padding_length = 0):
	padded = str(original)
	padded = padded.strip()
	padded = padded.lstrip('0')
	while len(padded) < padding_length:
		padded = '0' + padded

	return padded

class Group():
	def __init__(self, name, headers = ["Roll Number", "Name", "E mail"], input_file = ''):
		self.group_name = name
		self.output_filename = str(name) + ".csv"
		self.group_list = []
		self.headers = headers 
		self.branches = set([])
		if input_file != '':
			self.read_from_file(input_file)
			self.sort(key_index = 0)

	def setdata(self, data):
		setattr(self, "group_list", data)

	def read_from_file(self, filename):
		with open(filename, 'r') as input_file:
			reader = csv.DictReader(input_file)
			self.headers = reader.fieldnames
			for row in reader:
				row = list(row.values())
				self.group_list.append(list(row))
				self.branches.add(self.get_branch(roll = row[0]))

	def add_row(self, row):
		self.group_list.append(row)

	def append_row(self, filename, headers, list_of_elems):
		if(os.path.exists(filename)):
			with open(filename, 'a') as output_file:
				writer = csv.writer(output_file, delimiter = ",")
				writer.writerow(list_of_elems)
		else:
			with open(filename, 'w') as output_file:
				writer = csv.writer(output_file, delimiter = ",")
				writer.writerow(headers)
				writer.writerow(list_of_elems)

	def get_branch(self, position = -1, roll = None, row = None):
		if row == None:
			try:
				row = self.group_list[position]
			except IndexError:
				row = self.group_list[-1]

		if roll == None:
			roll = row[0]
		branch = ""
		for i in roll[4:]:
			if i.isdigit():
				break
			branch += i

		self.branches.add(branch)
		return branch


	def sort(self, key_index = 0, reverse = False): 
		self.group_list = sorted(self.group_list, key = lambda x: x[key_index], reverse = reverse)

	def make_csv(self, attribute = None):
		open_dir("Groups", root_folder)
		if attribute == None:
			attribute = getattr(self, "group_list")
		for row in attribute:
			self.append_row(self.output_filename, self.headers, row)

def make_groups(number_of_groups, branch_groups, branch_strength, total_strength):
	groups = []
	strengths = []
	for strength in branch_strength.group_list:
		init_strength = math.floor(strength[1]/number_of_groups)
		remaining = strength[1]%number_of_groups
		strengths.append((init_strength, remaining))

	for i in range(1, number_of_groups+1):
		name = "Group_G" + padding(str(i), len(str(number_of_groups)))
		temp = Group(name)
		groups.append(temp)
		groups[i-1].strengths = [x[0] for x in strengths]

	strengths = [x[1] for x in strengths]
	branch_groups = sorted(branch_groups, key = lambda x : x.group_name, reverse = False)
	branch_groups = sorted(branch_groups, key = lambda x : x.strength, reverse = True)

	cummulative_strength = [sum(strengths[0:x:1]) for x in range(0, len(strengths)+1)]
	cummulative_strength = cummulative_strength[1:]

	header = ["group", "total"] + [x[0] for x in branch_strength.group_list]

	j = 0
	for i in range(0, sum(strengths)):
		if(i >= cummulative_strength[j]):
			j += 1
		if(strengths[j] == 0):
			j += 1
		strengths[j] -= 1
		groups[i%number_of_groups].strengths[j] += 1

	
	stats = Group("stats_grouping", headers = header)
	for g in groups:
		temp = [g.output_filename] + [sum(g.strengths)] + g.strengths
		stats.group_list.append(temp)
		i = 0
		while i < len(strengths) and g.strengths[i] > 0:
			temp = branch_groups[i].group_list.pop(0)
			g.group_list.append(temp)
			g.strengths[i] -= 1
			if(g.strengths[i] == 0):
				i += 1
		g.sort(key_index = 0)
		g.make_csv()

	stats.make_csv()



def group_allocation(filename, number_of_groups):
	raw_data = Group("raw_data", input_file = filename)
	branch_strength = Group("branch_strength", headers = ["BRANCH_CODE", "STRENGTH"])
	branch_groups = []
	for branch in raw_data.branches:
		data = []
		for row in raw_data.group_list:
			if raw_data.get_branch(row = row) == branch:
				data.append(row)
		individual = Group(branch)
		individual.setdata(data)
		individual.strength = len(data)
		individual.make_csv()
		branch_groups.append(individual)
		branch_strength.group_list.append([branch, len(data)])

	branch_strength.sort(key_index = 0)
	branch_strength.sort(key_index = 1, reverse = True)
	branch_strength.make_csv()
	make_groups(number_of_groups, branch_groups, branch_strength, len(raw_data.group_list))
	



filename = "Btech_2020_master_data.csv"
del_folder()

root_folder = pwd()

number_of_groups = 12
group_allocation(filename, number_of_groups)
