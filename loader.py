from telebot import types
from telebot import callback_data
grade_markup = types.ReplyKeyboardMarkup()
choise = [
#	types.KeyboardButton('1'),
#	types.KeyboardButton('2'),
#	types.KeyboardButton('3'),
#	types.KeyboardButton('4'),
	types.KeyboardButton('5'),
#	types.KeyboardButton('6'),
	types.KeyboardButton('7'),
	types.KeyboardButton('8')
#	types.KeyboardButton('9'),
#	types.KeyboardButton('10'),
#	types.KeyboardButton('11'),
]
grade_markup.add(*choise)
#grade_markup.add(types.KeyboardButton('exit'))
sub_murkup = types.ReplyKeyboardMarkup()
choose_arr = [
		types.KeyboardButton('русский'),
		types.KeyboardButton('английский'),
		types.KeyboardButton('геометрия'),
		types.KeyboardButton('алгебра'),
		# types.KeyboardButton('физика'),
		types.KeyboardButton('география конт. карты')
	]
sub_murkup.add(*choose_arr)

sub1_murkup = types.ReplyKeyboardMarkup()
sub_arr = [
	types.KeyboardButton('русский'),
	types.KeyboardButton('английский'),
	types.KeyboardButton('математика'),
	types.KeyboardButton('география конт. карты')
	
]
sub1_murkup.add(*sub_arr	)

#contur maps markup
conmaps_marcup = types.ReplyKeyboardMarkup()
conmaps_arr = [
	types.KeyboardButton('стр.2'),
	types.KeyboardButton('стр.3'),
	types.KeyboardButton('стр.4'),
	types.KeyboardButton('стр.5'),
	types.KeyboardButton('стр.6'),
	types.KeyboardButton('стр.7'),
	types.KeyboardButton('стр.8'),
	types.KeyboardButton('стр.9'),
	types.KeyboardButton('стр.10-11'),
	types.KeyboardButton('стр.12-13'),
	types.KeyboardButton('стр.14-15'),
	types.KeyboardButton('стр.16')
]
conmaps_marcup.add(*conmaps_arr)

contur5maps_marcup = types.ReplyKeyboardMarkup()
con5maps_arr = [
    types.KeyboardButton('стр.2-3'),
    types.KeyboardButton('стр.4-5'),
    types.KeyboardButton('стр.6-7'),
    types.KeyboardButton('стр.10-11'),
    types.KeyboardButton('стр.14-15')
]
contur5maps_marcup.add(*con5maps_arr)
#start marcup
start_murkup = types.ReplyKeyboardMarkup()
start_murkup.add(types.KeyboardButton('в начало'))

none_marcup = types.ReplyKeyboardMarkup()
none_marcup.add(types.KeyboardButton('-'))

# Keyboard to check subscription
keyboard = types.InlineKeyboardMarkup()
subscribe = types.InlineKeyboardButton(text="Подписаться", url="https://t.me/dunenews")
keyboard.add(subscribe)
