import string
import random



characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def genv():
	length = 6
	random.shuffle(characters)
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	random.shuffle(password)
	variable = "".join(password)
	return variable
