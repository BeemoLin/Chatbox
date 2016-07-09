# coding=UTF-8
import socket
from Settings import HOST, PORT, PASS, IDENT, CHANNEL

def openSocket():
	
	s = socket.socket()
	s.connect((HOST, PORT))
	#decode('utf-8').encode('big5')
	s.send(("PASS " + PASS + "\r\n"))
	s.send(("NICK " + IDENT + "\r\n"))
	s.send(("JOIN #" + CHANNEL + "\r\n"))
	return s
	
def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
	s.send((messageTemp + "\r\n"))
	print("Sent: " + messageTemp)