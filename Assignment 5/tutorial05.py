import os
import re

pwd = os.getcwd #function alias
# Opens folder if exists, else creates and opens
def open_dir(directory = ".", pwd = pwd()):
	if directory == ".":
		return

	try:
		os.chdir(directory)
	except:
		os.mkdir(os.path.join(pwd, str(directory)))
		os.chdir(directory)

	return pwd()


def rename_FIR(folder_name = "FIR"):
    # rename Logic 
    

def rename_Game_of_Thrones(folder_name = "Game of Thrones"):
    # rename Logic 
    

def rename_Sherlock(folder_name = "Sherlock"):
    # rename Logic 
    

def rename_Suits(folder_name = "Suits"):
    # rename Logic 
    

def rename_How_I_Met_Your_Mother(folder_name = "How I Met Your Mother"):
    # rename Logic 
    

# Driver Code

root_folder = open_dir("Subtitles")

series = ["FIR" : 1, "Game of Thrones" : 2, "How I Met Your Mother": 3, "Sherlock" : 4, "Suits" : 5]

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
	elif  option == series["FIR"]:
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
