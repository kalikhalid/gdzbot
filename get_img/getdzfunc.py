#imports ##############
import os
import telebot
from time import sleep
import shutil
from get_img.get_img_test import *
import runpy
def include(file):
  globals().update(runpy.run_path(file,globals()))
include("/home/botenter/config.py")
########################


def getdz(message_id, bot_tok, patharr, filedir, url_beg, url_end, delite_imgs, msgtext):
	get_images(url_beg + msgtext + url_end, patharr, filedir=filedir)
	try:
		for i in delite_imgs:
			os.remove(i)
	except FileNotFoundError:
		pass

	os.chdir(filedir + '/' + patharr)
			
	filesdir = os.listdir(os.getcwd())
	for a in filesdir:
		path = filedir + '/' + patharr + '/' + a
		bot_tok.send_photo(int(message_id), (open(path, "rb")))
		sleep(0.5)
	os.chdir(filedir)
	
	shutil.rmtree(filedir + '/' + patharr)

def getdzphysics(message_id, bot_tok, patharr, filedir, urls, delite_imgs, msgtext):
	for i in urls:
		get_images(i, patharr, filedir=filedir)
		
		for i in delite_imgs:
			os.remove(i)
		os.chdir(filedir)
		try:
			os.chdir(filedir + '/' + patharr)
			
			filesdir = os.listdir(os.getcwd())
			for a in filesdir:
				bot_tok.send_photo(int(message_id), open(a, 'rb'))
		except:
			pass
		os.chdir(filedir)
	
		shutil.rmtree(filedir + '/' + patharr)


	
