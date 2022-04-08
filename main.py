import requests,random,json,os,sys
import flask
import telebot
from telebot import types
from user_agent import generate_user_agent
from config import *
import logging
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

call  = types.InlineKeyboardButton(text = "StArT MaKe HosT", callback_data = 'Suf')
@bot.message_handler(commands=['start'])
def start(message):
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 2
	Keyy.add(call)
	try:
		first = message.chat.first_name
		bot.send_message(message.chat.id,f"*- Hello {first}\n\n- The BoT Make HosT\n\n- BY:- @MMPMMMM*",parse_mode="markdown",reply_markup=Keyy)
		pass
	except:
		print('Error Token')
		exit()
@bot.callback_query_handler(func=lambda call: True)
def bin_mos(call):
	#hotmail
	if call.data =="Suf":
		host(call.message)
	if call.data =="python":
		python1(call.message)
	if call.data =="php":
		php1(call.message)
	if call.data =="pantheon":
		pyth(call.message)
		
def python1(message):
	program = types.InlineKeyboardButton(text='Click Login Host ',url='https://www.pythonanywhere.com/login')
	suf1 = types.InlineKeyboardMarkup()
	suf1.row_width = 2
	suf1.add(program)
	url = "https://mr-abood.herokuapp.com/Create/Python/Hosting"
	req = requests.get(url).json()
	print(req)
	user = str(req['username'])
	password = str(req['password'])
	bot.send_message(message.chat.id,f"- Hi Host Python Done ✅\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nUserName : {user}\nPassWord : {password}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n- By @MMPMMMM",parse_mode="markdown",reply_markup=suf1)	
		
def php1(message):
	url = "https://mr-abood.herokuapp.com/Create/PHP/Hosting"
	req = requests.get(url).json()
	print(req)
	user = str(req['username'])
	password = str(req['password'])
	p = str(req['panel'])
	web = str(req['website'])
	bot.send_message(message.chat.id,f"- Hi Host PhP Done ✅\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nUserName : {user}\nPassWord : {password}\nPanel : {p}\nWebSite : {web}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n- By @MMPMMMM",parse_mode="markdown")
	
def pyth(message):
	program = types.InlineKeyboardButton(text='Click Login Host ',url='https://pantheon.auth0.com/login?state=hKFo2SBFenVGYnNINmVqU19kNUNGSDhpUElia3BuYUptUkg5S6FupWxvZ2luo3RpZNkgLXZOM0M3dW1kT3hTTDdfRkltNWNqN0RJT19BR2tzVDajY2lk2SBxOWZXajl4blB4NE9BQVk5SU5ZZGNmaVlJVGtHdmFIcg&client=q9fWj9xnPx4OAAY9INYdcfiYITkGvaHr&protocol=oauth2&responsetype=code&redirecturi=https%3A%2F%2Fdashboard.pantheon.io%2Fauth%2Fcallback&scope=login%20openid%20pantheon&connection=')
	su = types.InlineKeyboardMarkup()
	su.row_width = 2
	su.add(program)
	url = 'https://mr-abood.herokuapp.com/Create/Pantheon/Account'
	req = requests.get(url).json()
	print(req)
	user = str(req['Email'])
	password = str(req['Password'])
	print(f"Email : {user}\nPassWord : {password}")
	if "'Status': True," in req:
		print("✓")
	else:
		print("Not")
		bot.send_message(message.chat.id,f"- Hi Host PanTHeon Done ✅\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\nEmail : {user}\nPassWord : {password}\n┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉\n- By @MMPMMMM",parse_mode="markdown",reply_markup=su)
	
	

def host(message):
	python  = types.InlineKeyboardButton(text = "Python", callback_data = 'python')
	php  = types.InlineKeyboardButton(text = "php", callback_data = 'php')
	pantheon = types.InlineKeyboardButton(text = "Pantheon", callback_data = 'pantheon')
	
	olo1 = types.InlineKeyboardMarkup()
	olo1.row_width = 2
	olo1.add(python,php,pantheon)
	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="ChoosE PhP or Python",parse_mode='markdown',reply_markup=olo1)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://hostio.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.polling()