import os
import re

pwd = os.getcwd #function alias

# Opens folder if exists, else creates and opens
def open_dir(directory = ".", cwd = pwd()):
	if directory == ".":
		return

	try:
		os.chdir(directory)
	except:
		os.mkdir(os.path.join(cwd, str(directory)))
		os.chdir(directory)

	return pwd()

root_folder = open_dir("Subtitles") #Setting this as the root folder for further reference


# Padding function
def padding(original = '', padding_length = 0):
	padded = str(original)
	padded = padded.strip()
	padded = padded.lstrip('0')
	while len(padded) < padding_length:
		padded = '0' + padded

	return padded

def newname_check(subtitle):
	print("Checking for new naming convention")
	extracted = re.split('-',subtitle)
	extracted = [x.strip() for x in extracted]
	season_number = (extracted[1].split())[1]
	season_number = padding(season_number, padding_season)
	episode_number = (extracted[1].strip()).split()[3]
	episode_number = padding(episode_number, padding_episode)
	file_extension = extracted[2].split(r'.')[-1]
	try:
		episode_name = extracted[2].split(r'.')[0]
		return episode_number, season_number, episode_name, file_extension
	except:
		return episode_number, season_number, file_extension


def rename_FIR(folder_name = "FIR"):
	open_dir(root_folder)
	open_dir(folder_name)
	Subtitles = os.listdir(pwd())
	for subtitle in Subtitles:
		try:
			extracted = re.findall(r'\d+',subtitle)
			episode_number = extracted[0].strip()
			file_extension = (re.split(r'\.',subtitle)[-1]).strip()
			episode_number = padding(episode_number, padding_episode)
			new_name = "FIR - Episode " + episode_number + "." + file_extension
			os.rename(subtitle, new_name)
		except:
			print(subtitle + " doesn't corespond to the normal subtitle naming convention")
			os.rename(subtitle, subtitle)
	return 

def rename_Game_of_Thrones(folder_name = "Game of Thrones"):
	open_dir(root_folder)
	open_dir(folder_name)
	Subtitles = os.listdir(pwd())
	for subtitle in Subtitles:
		try:
			extracted = re.split('-',subtitle)
			season_x_episode = extracted[1]
			remaining = re.split(r'\.',extracted[2])
			season_number , episode_number = re.split('x',season_x_episode)
			episode_name = remaining[0]
			file_extension = (re.split(r'\.',extracted[2])[-1]).strip()
			episode_number = padding(episode_number, padding_episode)
			season_number = padding(season_number, padding_season)
			new_name = 'Game of Thrones - Season '+ season_number + ' Episode ' + episode_number+ ' - ' + episode_name + '.' + file_extension
			os.rename(subtitle, new_name)
		except:
			try:
				episode_number, season_number, episode_name, file_extension = newname_check(subtitle)
				new_name = 'Game of Thrones - Season '+ season_number + ' Episode ' + episode_number+ ' - ' + episode_name + '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")
				os.rename(subtitle, subtitle)

def rename_Sherlock(folder_name = "Sherlock"):
	open_dir(root_folder)
	open_dir(folder_name)
	Subtitles = os.listdir(pwd())
	for subtitle in Subtitles:
		try:
			extracted = re.findall(r'\d+',subtitle)
			extracted = [x.strip() for x in extracted]
			season_number = extracted[0]
			episode_number = extracted[1]
			file_extension = (re.split(r'\.',subtitle)[-1]).strip()
			episode_number = padding(episode_number, padding_episode)
			season_number = padding(season_number, padding_season)
			new_name = 'Sherlock - Season '+ season_number + ' Episode ' + episode_number+ '.' + file_extension
			os.rename(subtitle, new_name)
		except:
			try:
				episode_number, season_number, file_extension = newname_check(subtitle)
				new_name = 'Sherlock - Season '+ season_number + ' Episode ' + episode_number+ '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")
				os.rename(subtitle, subtitle)

def rename_Suits(folder_name = "Suits"):
	open_dir(root_folder)
	open_dir(folder_name)
	Subtitles = os.listdir(pwd())
	for subtitle in Subtitles:
		try:
			extracted = re.findall(r'\d+',subtitle)
			extracted = [x.strip() for x in extracted]
			episode_number = extracted[1]
			season_number = extracted[0]
			extracted = re.split('-',subtitle)
			episode_name = (re.split(r'\.',extracted[2])[0]).strip()
			file_extension = (re.split(r'\.',subtitle)[-1]).strip()
			episode_number = padding(episode_number, padding_episode)
			season_number = padding(season_number, padding_season)
			new_name = 'Suits - Season '+ season_number + ' Episode ' + episode_number + ' - ' + episode_name + '.' + file_extension
			os.rename(subtitle, new_name)    
		except:
			try:
				episode_number, season_number, episode_name, file_extension = newname_check(subtitle)
				new_name = 'Suits - Season '+ season_number + ' Episode ' + episode_number + ' - ' + episode_name + '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")
				os.rename(subtitle, subtitle)

def rename_How_I_Met_Your_Mother(folder_name = "How I Met Your Mother"):
	open_dir(root_folder)
	open_dir(folder_name)
	Subtitles = os.listdir(pwd())
	for subtitle in Subtitles:
		try:
			extracted = re.findall(r'\d+',subtitle)
			episode_number = (extracted[1]).strip()
			season_number = (extracted[0]).strip()
			extracted = re.split('-',subtitle)
			episode_name = (re.split(r'\.',extracted[2])[0]).strip()
			file_extension = (re.split(r'\.',subtitle)[-1]).strip()
			episode_number = padding(episode_number, padding_episode)
			season_number = padding(season_number, padding_season)
			new_name = 'How I Met Your Mother - Season '+ season_number + ' Episode ' + episode_number + ' - ' + episode_name + '.' + file_extension
			os.rename(subtitle, new_name) 
		except:
			try:
				episode_number, season_number, episode_name, file_extension = newname_check(subtitle)
				new_name = 'How I Met Your Mother - Season '+ season_number + ' Episode ' + episode_number + ' - ' + episode_name + '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")
				os.rename(subtitle, subtitle)

# Driver Code
title_list = [1,2,3,4,5]
series = ["FIR", "Game of Thrones", "How I Met Your Mother", "Sherlock", "Suits"]

def prompt():
	series_input = int(input('''1.FIR
2.Game of Thrones
3.How I Met Your Mother
4.Sherlock
5.Suits
Please enter the title of the Series: '''))
	if series_input not in title_list:
		series_input = prompt()
	return series_input - 1

def rename(option = -1):
	if(option == -1):
		return
	elif option == 0:
		rename_FIR()
	elif option == 1:
		rename_Game_of_Thrones()
	elif option == 2:
		rename_Sherlock()
	elif option	== 3:
		rename_Suits()
	elif option == 4:
		rename_How_I_Met_Your_Mother()
	else:
		rename(series[prompt()])

series_name = prompt()

padding_season = int(input("Please enter season number padding: "))
padding_episode = int(input("Please enter episode number padding: "))

rename(series_name)
