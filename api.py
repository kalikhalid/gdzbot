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

#bot
state_storage = StateMemoryStorage() # you can init here another storage
Thisfiledir = os.path.dirname(os.path.abspath(sys.argv[0]))
bot = telebot.TeleBot(TOKEN,
state_storage=state_storage)
#channel id
chan_id ="-1001731808658"

# state class
class MyState(StatesGroup):
	grade = State()
	subject = State()
	ex = State()
	previous_step = State()

class PhysicsState(StatesGroup):
	paragraph = State()
	questions = State()
	num = State()

# Keyboard to check subscription
keyboard = telebot.types.InlineKeyboardMarkup()
subscribe = telebot.types.InlineKeyboardButton(text="Subscribe", url="https://t.me/dunenews")
keyboard.add(subscribe)


@bot.message_handler(regexp='/start')
def start(message):
	member = bot.get_chat_member(chat_id=chan_id, user_id=message.from_user.id)
	statuses = ('creator', 'administrator', 'member')
	if member.status not in statuses:
		bot.send_message(message.chat.id, "Please subscribe to the channel with news about the bot and send /start command", reply_markup=keyboard)
	else:
		bot.set_state(message.from_user.id, MyState.grade, message.chat.id)
		bot.send_message(message.chat.id, 'Choose your grade.', reply_markup=grade_markup)

@bot.message_handler(state=MyState.grade)
def grade_get(message):
	bot.send_message(message.chat.id, 'Now write subject', reply_markup=sub_murkup)
	bot.set_state(message.from_user.id, MyState.subject, message.chat.id)
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['grade'] = message.text

@bot.message_handler(state=MyState.subject)
def ask_age(message):
    bot.send_message(message.chat.id, "Write ex or page")
    bot.set_state(message.from_user.id, MyState.ex, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['subject'] = message.text


@bot.message_handler(state=MyState.ex, is_digit=True)
def ready_for_answer(message):
	bot.set_state(message.from_user.id, MyState.previous_step, message.chat.id)
	with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
		data['ex'] = message.text
		if data['grade'] == '7':
			filesdir7 = Thisfiledir + '/' + '7gradehomedir'
			getdzfor7(message.chat.id, message.text, filesdir7, data['subject'])
				
	bot.delete_state(message.from_user.id, message.chat.id)
@bot.message_handler(state=MyState.ex, is_digit=False)
def not_true(message):
	bot.send_message(message.chat.id, 'Looks like you are submitting a string in the field age. Please enter a number')


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())

bot.infinity_polling() 
