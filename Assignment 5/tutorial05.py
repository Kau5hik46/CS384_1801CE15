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
	extracted = re.split('-',subtitle)
	extracted = [x.strip() for x in extracted]
	season_number = (extracted[1].split())[1]
	season_number = padding(season_number, padding_season)
	episode_number = (extracted[1].strip()).split()[3]
	episode_number = padding(episode_number, padding_episode)
	file_extension = extracted[2].split(r'.')[-1]
	episode_name = extracted[2].split(r'.')[0]
	return episode_number, season_number,  file_extension


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
				season_number, episode_number, file_extension = newname_check(subtitle)
				new_name = 'Game of Thrones - Season '+ season_number + ' Episode ' + episode_number+ ' - ' + episode_name + '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")

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
				season_number, episode_number, file_extension = newname_check(subtitle)
				new_name = 'Sherlock - Season '+ season_number + ' Episode ' + episode_number+ '.' + file_extension
				if(new_name != subtitle):
					os.rename(subtitle, new_name)
			except:
				print(subtitle + " doesn't corespond to the normal subtitle naming convention")

def rename_Suits(folder_name = "Suits"):
	pass

def rename_How_I_Met_Your_Mother(folder_name = "How I Met Your Mother"):
	pass

# Driver Code

series = {"FIR" : 1, "Game of Thrones" : 2, "How I Met Your Mother": 3, "Sherlock" : 4, "Suits" : 5}

def prompt():
	series_input = str(input('''1.FIR
2.Game of Thrones
3.How I Met Your Mother
4.Sherlock
5.Suits
Please enter the title of the Series: '''))
	if series_input not in series.keys():
		series_input = prompt()
	return series_input

def rename(option = 0):
	if(option == 0):
		return
	elif option == series["FIR"]:
		rename_FIR()
	elif option == series["Game of Thrones"]:
		rename_Game_of_Thrones()
	elif option == series["Sherlock"]:
		rename_Sherlock()
	elif option	== series["Suits"]:
		rename_Suits()
	else:
		rename(series[prompt()])

series_name = prompt()

padding_season = int(input("Please enter season number padding: "))
padding_episode = int(input("Please enter episode number padding: "))

rename(series[series_name])
