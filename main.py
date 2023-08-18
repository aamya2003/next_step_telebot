import telebot
from telebot.types import *

bot = telebot.TeleBot("Your_Bot_Token")


@bot.message_handler(commands=['start'])
def main(message:Message):
    global myid
    myid = message.from_user.id
    bot.send_message(message.chat.id, "ارسل اسمك: ")

def sec(message):
    if myid == message.from_user.id:
        bot.send_message(message.chat.id, "تم تسجيل عضويتك")


bot.infinity_polling()