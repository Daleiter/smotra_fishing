import telebot
import json

token = '6577063318:AAE_T_3KZum81nlKuE4pxpeqOO_5jV_MePI'  # Замените на свой токен
bot = telebot.TeleBot(token)
# while True:
#     with open("update_id.json", "r") as json_file:
#         data = json.load(json_file)
#     updates = bot.get_updates(offset=data['update_id'], limit=1,timeout=1)
#     if updates != []:
#         data['update_id'] = updates[0].update_id + 1
#         with open("update_id.json", "w") as json_file:
#             json.dump(data, json_file, ensure_ascii=False, indent=4)
#         print(data['update_id'], updates[0].message.text)
#     else:
#         break
# # updates = bot.get_updates(offset=196930922, limit=1)
# # if updates != []:
# #     print(updates)
import pyautogui
import keyboard
import time
time.sleep(2) 
while pyautogui.pixel(1685, 1028)[0] != 186:
    print('asd')


        

# last_key = ''
# listfunctions=[]
# def pressQ():
#     print('q')
# def pressE():
#     print('e')
# while True:
#     right_pixel = pyautogui.pixel(1063, 533)
#     left_pixel = pyautogui.pixel(1035, 533)
#     if 170 <= right_pixel[1] <= 200:
#         if last_key != 'Q':
#             listfunctions=[]
#         listfunctions.append(pressQ)
#         for i in listfunctions:
#             i()
#         last_key = "Q"
#     elif left_pixel[1] < 70:
#         if last_key != 'E':
#             listfunctions=[]
#         listfunctions.append(pressE)
#         for i in listfunctions:
#             i()
#         last_key = "E"