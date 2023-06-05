from core.gmtscript import *
from get_img.getdzfunc import *
from core.variable_gen import *
import shutil
import os
import telebot
import sys
def include(file):
  globals().update(runpy.run_path(file,globals()))
include("/home/botenter/config.py")

global telbot
telbot = telebot.TeleBot(TOKEN)
def getdzfor7(message_id, message_text, filedir, datasub, username):
	if datasub == 'русский':
		delitearr = ['russkiy-yazyk-7-klass-baranov.jpg', '5f7dbc226dfc3.jpg', '5f7c3b2f0e6b5.jpg']
		print("User with username " + str(username) + " downloading russian")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-7/russkii_yazik/baranova/', '-nom/', delitearr, message_text)
	elif datasub == 'английский':
		delitearr = ['gdz-7-class-angliyskiy-yazyk-komissarov.jpg', 'gdz-7-class-angliyskiy-yazyk-baranova.jpg', 'gdz-7-class-angliyskiy-yazyk-smirnov.jpg', 'crown.svg', 'icon_arrow.png']		
		print("User with username " + str(username) + " downloading english")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-7/english/starlight-baranova/', '-s/', delitearr, message_text)
	elif datasub == 'алгебра':
		delitearr = ['algebra-7-klass-makarychev.jpg', 'gdz-7-class-algebra-makarychev.jpg', 'icon_arrow.png']
		print("User with username " + str(username) + " downloading algebra")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-7/algebra/makarichev-18/', '/', delitearr, message_text)
	elif datasub == 'геометрия':
		gmturls = ['https://gdz.ru/class-7/geometria/atanasyan-7-9/1-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/2-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/3-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/4-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/5-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/6-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/7-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/8-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/9-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/10-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/11-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/12-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/13-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/14-chapter-']
		var = genv()
		print("User with username " + str(username) + " downloading geometry")
		gmthelp(gmturls, message_text, var, filedir)
		os.chdir(filedir + '/' + var)
		filesdir = os.listdir(os.getcwd())
		for a in filesdir:
			telbot.send_photo(message_id, open(a, 'rb'))
	
		os.chdir(filedir)
		
		shutil.rmtree(filedir + '/' + var)
	elif datasub == 'география(к.к.)':
		delitearr = ['60b4b162f2767.jpg', 'gdz-7-class-geografiya-kurbskiy.jpg']
		print("User with username " + str(username) + " downloading geography")
		msg_txt = message_text.split('.')[1].split('-')
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-7/geografiya/konturnie-karti-kurbskij/', '-s/', delitearr, msg_txt[0])



def getdzfor8(message_id, message_text, filedir, datasub, username):
	if datasub == 'русский':
		delitearr = ['russkiy-yazyk-8-klass-barhudarov.jpg', '5f7c4196ad4d1.jpg', 'russian.jpg']
		print("User with username " + str(username) + " downloading russian")
		getdz(message_id, telbot, genv(), filedir, "https://gdz.ru/class-8/russkii_yazik/barhudarov-8/", '-nom/', delitearr, message_text)
	elif datasub == 'английский':
		delitearr = ['gdz-8-class-angliyskiy-yazyk-baranova.jpg', 'gdz-8-class-angliyskiy-yazyk-inyashkin.jpg', 'gdz-8-class-angliyskiy-yazyk-komissarov.jpg']		
		print("User with username " + str(username) + " downloading english")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-8/english/starlight-baranova/', '-s/', delitearr, message_text)
	elif datasub == 'алгебра':
		delitearr = ['622f3629c4920.jpg', 'gdz-8-class-algebra-makarychev.jpg', 'algebra-8-klass-makarychev.jpg']
		print("User with username " + str(username) + " downloading algebra")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-8/algebra/makarychev-8/nomer-', '/', delitearr, message_text)
	elif datasub == 'геометрия':
		gmturls = ['https://gdz.ru/class-7/geometria/atanasyan-7-9/1-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/2-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/3-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/4-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/5-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/6-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/7-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/8-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/9-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/10-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/11-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/12-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/13-chapter-', 'https://gdz.ru/class-7/geometria/atanasyan-7-9/14-chapter-']
		var = genv()
		print("User with username " + str(username) + " downloading geometry")
		gmthelp(gmturls, message_text, var, filedir)
		os.chdir(filedir + '/' + var)
		filesdir = os.listdir(os.getcwd())
		for a in filesdir:
			telbot.send_photo(message_id, open(a, 'rb'))
	
		os.chdir(filedir)
		
		shutil.rmtree(filedir + '/' + var)
def getdzfor5(message_id, message_text, filedir, datasub, username):
	if datasub == 'русский':
		delitearr = ['5f7dba78620da.jpg', '642dbdcdb6b5c.jpg','642dbe1e8b51b.jpg', 'russian.jpg', 'russkiy-yazyk-5-klass-ladyzhenskaya-baranov.jpg']
		print("User with username " + str(username) + " downloading russian")
		getdz(message_id, telbot, genv(), filedir, "https://gdz.ru/class-5/russkii_yazik/ladyzhenskaya-t-a/2019-upr-", '/', delitearr, message_text)
	elif datasub == 'английский':
		delitearr = ['gdz-5-class-angliyskiy-yazyk-baranova.jpg', 'gdz-5-class-angliyskiy-yazyk-komissarov.jpg', 'gdz-5-class-angliyskiy-yazyk-smirnov.jpg']		
		print("User with username " + str(username) + " downloading english")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-5/english/reshebnik-baranova-k-m-starlight-5-zvezdnyy-angliyskiy-5-klass/', '-s/', delitearr, message_text)
	elif datasub == 'математика':
		delitearr = ['gdz-5-class-matematika-bucko.jpg', 'gdz-5-class-matematika-merzlyak.jpg', 'gdz-5-class-matematika-merzlyak.png', 'math.jpg']
		print("User with username " + str(username) + " downloading algebra")
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-5/matematika/merzlyak-polonskiy/', '-nom/', delitearr, message_text)
	elif datasub == 'география конт. карты':
		delitearr = ['gdz-5-6-class-geografiya-alekseev.jpg', 'gdz-5-6-class-geografiya-bondareva.jpg', 'gdz-5-6-class-geografiya-dubinina.jpg', 'gdz-5-6-class-geografiya-nikolina.jpg', 'gdz-5-class-geografiya-nikolina.jpg']
		print("User with username " + str(username) + " downloading geography")
		msg_txt = message_text.split('.')[1].split('-')s
		getdz(message_id, telbot, genv(), filedir, 'https://gdz.ru/class-5/geografiya/konturnie-karti-matveev/', '-s/', delitearr, msg_txt[0])
