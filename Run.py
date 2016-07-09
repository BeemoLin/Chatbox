# coding=UTF-8

import os
import string
import time
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from gtts import gTTS
import subprocess

if not os.path.exists('sound'):
	os.mkdir('sound')
	
def player(say):
	try:
		timeStamp = str(time.time())
		download_mp3(say, timeStamp)
		file_Path = "sound/" + timeStamp + ".mp3";
		child = subprocess.Popen(["python","player_google.py",file_Path])
	except:	
		print("can't play")

def download_mp3(say, file_name):
	try:
		tts = gTTS(text=say, lang='zh-tw')
		tts.save("sound/" + file_name + ".mp3")
	except:
		print("can't download mp3")

def player_Poi(fileName):
	try:
		file_Path = "kancolle/" + fileName;
		child = subprocess.Popen(["python","player.py",file_Path])
	except:	
		print("can't play")
	
s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)

			if "PING" in line:
				s.send((line.replace("PING", "PONG") + "\r\n"))
				print(line.replace("PING", "PONG"))
				break
			user = getUser(line)
			message = getMessage(line)
			print(user + " typed :" + message)
			
			if "sklive_如月" in message:
				player("8 8 3 7歐提 燒!")
				sendMessage(s, "8837歐提 燒!")
				break
			elif "!8837" in message:
				player("8 8 3 7歐提 燒!")
				break
			elif "戳8837" in message:
				player_Poi("KisaragiKai27.mp3")
				sendMessage(s, "如月：司令官ったら・・・ありがとう、好きよ。")
				break
			elif "http" in message:
				player("只是一個網址")
				break
			elif "sklive_田中" in message:
				player("幹你田中 燒!")
				break
			elif "sklive_歐提燒" in message:
				player("歐提燒")
				#sendMessage(s, "歐提 燒!")
				break
			elif "sklive_幫幫幫" in message:
				player_Poi("Atago26.mp3")
				#sendMessage(s, "幫幫嘎幫")
				break
			elif "sklive_哇哇哇" in message:
				player("哇哇哇哇")
				#sendMessage(s, "哇哇哇哇")
				break
			elif "sklive_卡滋卡滋" in message:
				player("卡滋卡滋")
				#sendMessage(s, "卡滋卡滋")
				break
			elif "sklive_北方百烈拳" in message:
				player("北方百烈拳")
				#sendMessage(s, "北方百烈拳")
				break
			elif "sklive_110" in message:
				player("警察叔叔就是他")
				#sendMessage(s, "警察叔叔就是他")
				break
			elif "sklive_潛水" in message:
				player_Poi("I58_11.mp3")
				break
			elif "sklive_決鬥" in message:
				player_Poi("duel.mp3")
				break
			elif "sklive_熊" in message:
				player("變態")
				break
			elif "!決鬥" in message:
				player_Poi("duel.mp3")
				break
			elif "安安" in message:
				player("你好" + user + "歡迎來到U醬漁民協會!")
				sendMessage(s, "你好" + user + "歡迎來到U醬漁民協會!")
				break
			elif "島風衝刺" in message:
				player_Poi("Shimakaze26.mp3")
				sendMessage(s, "島風：おっそーいー！")
				break
			elif "!島風" in message:
				player_Poi("Shimakaze02.mp3")
				sendMessage(s, "島風：ｵｩｯ!?")
				break
			elif "!大鯨" in message:
				player_Poi("Taigei29.mp3")
				sendMessage(s, "大鯨：て・い・と・く、提督！あ、あの…潜水艦作戦は……")
				break
			elif "壓壓鯨" in message:
				player_Poi("Taigei29.mp3")
				sendMessage(s, "大鯨：て・い・と・く、提督！あ、あの…潜水艦作戦は……")
				break
			elif "歐根燒" in message:
				player_Poi("PrinzEugen16.mp3")
				sendMessage(s, "Prinz Eugen：Feuer! Feuer!")
				break
			elif "!歐根" in message:
				player_Poi("PrinzEugen03.mp3")
				sendMessage(s, "Prinz Eugen：Einen schönen Tag.")
				break
			elif "謝謝" in message:
				player_Poi("PrinzEugen09.mp3")
				sendMessage(s, "Prinz Eugen：Danke Danke！")
				break
			elif "!義大利" in message:
				player_Poi("Littorio27.mp3")
				sendMessage(s, "Littorio：美味しいパスタ、食べたいですね。")
				break
			elif "!大淀" in message:
				player_Poi("Oyodo08a.mp3")
				sendMessage(s, "大淀：提督、艦隊の情報。ご覧になります？")
				break
			elif "!霞" in message:
				player_Poi("Kasumi03.mp3")
				sendMessage(s, "霞：だから何よ？")
				break
			elif "!明石" in message:
				player_Poi("Akashi03.mp3")
				sendMessage(s, "明石：提督も修理ですか？どこが壊れてます？")
				break
			elif "!電" in message:
				player_Poi("Inazuma15.mp3")
				sendMessage(s, "電：なのです！")
				break
			elif "!pola醉" in message:
				player_Poi("Pola12.mp3")
				sendMessage(s, "Pola：提督～がぁ～ふたりぃ～♪ヘヘヘヘ♪ちょっとだけ飲んじゃった・・・服が邪魔♪。")
				break
			elif "!pola" in message:
				player_Poi("Pola03.mp3")
				sendMessage(s, "Pola：なんでしょう～。飲み会ですかぁ～？")
				break
			elif "!潮" in message:
				player_Poi("Ushio15natsu2.mp3")
				sendMessage(s, "潮：ひゃあああ！あ、あの…びっくりしますから…")
				break
			elif "!三隈" in message:
				player_Poi("Mikuma17.mp3")
				sendMessage(s, "三隈：くまりんこ！")
				break
			elif "!三熊" in message:
				player_Poi("Mikuma17.mp3")
				sendMessage(s, "三隈：くまりんこ！")
				break
			elif "yee" in message:
				player_Poi("32263730.mp3")
				sendMessage(s, "PT：イ゛イ゛ッ…！イ゛ィーッ……！")
				break
			elif "!小北方" in message:
				player_Poi("HimeNorth06.mp3")
				sendMessage(s, "北方棲姬：カエレ……ッ！")
				break
			elif "!響" in message:
				player_Poi("Bep17.mp3")
				sendMessage(s, "Верный：Хорошо")
				break
			elif "666" in message:
				player_Poi("Bep17.mp3")
				sendMessage(s, "Верный：Хорошо")
				break
			elif "!叢雲" in message:
				player_Poi("Murakumo04.mp3")
				sendMessage(s, "叢雲：アンタ…酸素魚雷を食らわせるわよ！")
				break
			elif "!如月" in message:
				player_Poi("Kisaragi28.mp3")
				sendMessage(s, "如月：な～んちゃって。")
				break
			elif "如月中破" in message:
				player_Poi("Kisaragi21.mp3")
				sendMessage(s, "如月：私を…どうする気?!")
				break
			elif "!那珂" in message:
				player_Poi("Nakakai02.mp3")
				sendMessage(s, "那珂：よぉし、那珂ちゃん今日もかわいい♪")
				break
			elif "!雪風" in message:
				player_Poi("Yukikaze_v15.mp3")
				sendMessage(s, "雪風：雪風は沈みませんっ！")
				break
			elif "!春風" in message:
				player_Poi("Harukaze02.mp3")
				sendMessage(s, "春風：春風をお呼びでございますか？")
				break
			elif "!神風" in message:
				player_Poi("Kamikaze02.mp3")
				sendMessage(s, "神風：司令官、私を呼んだ？準備はできているわ。")
				break
			elif "夜戰" in message:
				player_Poi("Sendai02.mp3")
				sendMessage(s, "川內：何？夜戦？")
				break
			elif "!U" in message:
				player_Poi("U-511-Secretary_1.ogg")
				sendMessage(s, "U-511：Guten Morgen")
				break
			elif "sklive_がるる" in message:
				player_Poi("Ro500_18.mp3")
				break
			else:
				player(message)
			print("wait to message")
