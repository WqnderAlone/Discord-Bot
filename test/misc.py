import random

def gibberish(length):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=~!@#$%^&*()_+[]\;',./{}|:<>?"
	sendme = ""
	for i in range(0, int(length)):
		sendme += random.choice(list(alphabet))
	return sendme
