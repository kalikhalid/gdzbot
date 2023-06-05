from config import *
from loader import *
import telebot
import shutil
import os
import sqlite3
from get_img.getdzfunc import *
import sys
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup #States
# States storage
from telebot.storage import StateMemoryStorage
from core.variable_gen import *
from core.gradesfunks import *
from core.gmtscript import *


state_storage = StateMemoryStorage() # you can init here another storage
Thisfiledir = os.path.dirname(os.path.abspath(sys.argv[0]))
bot = telebot.TeleBot(TOKEN,
state_storage=state_storage)
#channel id
chan_id = -1001731808658

# state class
class MyState(StatesGroup):
	grade = State()
	subject = State()
	ex = State()
	choice = State()
	exit = State()

@bot.message_handler(regexp='/start')
def start(message):
	bot.set_state(message.from_user.id, MyState.grade, message.chat.id)
	bot.send_message(message.chat.id, 'Выберите свой класс', reply_markup=grade_markup)

@bot.message_handler(state=MyState.grade)
def grade_get(message):
	if message.text in ['7', '8', '9', '10', '11']:
		bot.send_message(message.chat.id, 'Теперь напишите предмет', reply_markup=sub_murkup)
	elif message.text in ['2', '3', '4', '5', '6', '1']:
		bot.send_message(message.chat.id, 'Теперь напишите предмет', reply_markup=sub1_murkup)
	bot.set_state(message.from_user.id, MyState.subject, message.chat.id)
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['grade'] = message.text
@bot.message_handler(state=MyState.subject)
def ask_age(message):
	bot.set_state(message.from_user.id, MyState.ex, message.chat.id)
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['subject'] = message.text
		if data['subject'] == 'география конт. карты' and data['grade'] in ['7', '8']:
			bot.send_message(message.chat.id, "Bыберите из списка страницу", reply_markup=conmaps_marcup)
		if data['subject'] == 'география конт. карты' and data['grade'] in ['5']:
			bot.send_message(message.chat.id, "Bыберите из списка страницу", reply_markup=contur5maps_marcup)
		else:
			bot.send_message(message.chat.id, "Напишите упражнение", reply_markup=None)

@bot.message_handler(state=MyState.ex)
def ready_for_answer(message):
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['ex'] = message.text
		filesdir7 = Thisfiledir + '/' + '7gradehomedir'
		if data['grade'] == '7':
			getdzfor7(message.chat.id, message.text, filesdir7, data['subject'], message.from_user.username)
			bot.set_state(message.from_user.id, MyState.exit, message.chat.id)
			bot.send_message(message.chat.id, "в начало?", reply_markup=start_murkup)
		elif data['grade'] == '8':
			getdzfor8(message.chat.id, message.text, filesdir7, data['subject'], message.from_user.username)
			bot.set_state(message.from_user.id, MyState.exit, message.chat.id)
			bot.send_message(message.chat.id, "в начало?", reply_markup=start_murkup)
		elif data['grade'] == '5':
			getdzfor5(message.chat.id, message.text, filesdir7, data['subject'], message.from_user.username)
			bot.set_state(message.from_user.id, MyState.exit, message.chat.id)
			bot.send_message(message.chat.id, "в начало?", reply_markup=start_murkup)


@bot.message_handler(state=MyState.exit)
def stop(message):
	bot.set_state(message.from_user.id, MyState.ex, message.chat.id)
	if message.text == 'в начало':
		bot.set_state(message.from_user.id, MyState.grade, message.chat.id)
		bot.send_message(message.chat.id, 'Выберите свой класс', reply_markup=grade_markup)

	else:
		bot.send_message(message.chat.id, "/start")


	

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling() 
