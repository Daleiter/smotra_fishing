import telebot
import time
import os

token = ('6577063318:AAE_T_3KZum81nlKuE4pxpeqOO_5jV_MePI')
bot = telebot.TeleBot(token)


updates = bot.get_updates(offset=196931267, limit=1)
if updates != 0:
    message = updates[0].message.text
    print(message)