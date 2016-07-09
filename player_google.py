# coding=UTF-8

import sys
#import time
import pygame  # Load the required library

#from gtts import gTTS

filePath = sys.argv[1].encode('utf-8')
#tts = gTTS(text=say, lang='zh-tw')

#timeStamp = str(time.time())
#tts.save("sound/" + timeStamp + ".mp3")

pygame.mixer.init()
pygame.mixer.music.load(filePath)
pygame.mixer.music.set_volume(0.5)
try:
	clock = pygame.time.Clock()
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		#print "Playing..."
		clock.tick(1000)
except:	
		print("can't play")
