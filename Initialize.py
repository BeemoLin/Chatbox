# coding=UTF-8

import string
from Socket import sendMessage
import subprocess

def player_Poi(fileName):
	try:
		file_Path = "kancolle/" + fileName
		child = subprocess.Popen(["python","player.py",file_Path])
	except:	
		print("can't play")
		
def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = loadingComplete(line)
	#sendMessage(s, "您的好友google小姐已上線")
	sendMessage(s, "大鯨：て・い・と・く、提督！")
	
	player_Poi("Taigei29.mp3")
	
def loadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True