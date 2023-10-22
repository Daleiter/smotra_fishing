import pyautogui
import time
import keyboard
import json
import telebot

token = ('6577063318:AAE_T_3KZum81nlKuE4pxpeqOO_5jV_MePI')
bot = telebot.TeleBot(token)

def update_update():
    while True:
        with open("update_id.json", "r") as json_file:
            data = json.load(json_file)
        updates = bot.get_updates(offset=data['update_id'], limit=1,timeout=1)
        if updates != 0:
            data['update_id'] = updates[0].update_id + 1
            with open("update_id.json", "w") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            print(data['update_id'], updates[0].message.text)
        else:
            break

def dump(info='huevo'):
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    data[info] +=1  
    print(data[info])
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    bot.send_message(1259834978, f"{info, data}")

def recive(info):
    with open("update_id.json", "r") as json_file:
        data = json.load(json_file)
    return data[info]+1
 
def dump_update():
    with open("update_id.json", "r") as json_file:
        data = json.load(json_file)
    data['update_id'] +=1 
    with open("update_id.json", "w") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def podcepit(na4to):
    cordinate=[[0],[699, 597],[1113, 597]]
    time_sleep = 0.5
    pyautogui.keyDown('E')
    time.sleep(time_sleep)
    pyautogui.keyUp('E') 
    print('start')
    time.sleep(time_sleep*2)
    pyautogui.click(cordinate[na4to])
    time.sleep(time_sleep*2.5)
    pyautogui.click(959, 578)
    time.sleep(time_sleep*8)
    while pyautogui.pixel(1654, 1028)[0] == 186:
        time.sleep(time_sleep*2)
    print('kluet')
    pyautogui.keyDown('E')
    time.sleep(time_sleep)
    pyautogui.keyUp('E')
    time.sleep(time_sleep)

def pressQ():
    print('q')
    pyautogui.keyDown('Q')
    # time.sleep(0.1)
    pyautogui.keyUp('Q')

def pressE():
    print('e')
    pyautogui.keyDown('E')
    # time.sleep(0.1)
    pyautogui.keyUp('E')

def lovlia():
    last_key = ''
    print('lovit')
    while pyautogui.pixel(1685, 1028)[0] != 186:
        right_pixel = pyautogui.pixel(1063, 533)
        left_pixel = pyautogui.pixel(1035, 533)
        pimana_pixel_kartinka = pyautogui.pixel(1090, 467)
        if 225 <= pimana_pixel_kartinka[1] <= 240:
            time.sleep(1.5)
            bot.send_photo(1259834978, pyautogui.screenshot(region=(740, 310,440, 480)))
            print('capcha', pimana_pixel_kartinka)
            return 'capcha'
        if 170 <= right_pixel[1] <= 200:
            if last_key == 'Q':
                pressQ()
            pressQ()
            last_key = "Q"
        elif left_pixel[1] < 70:
            if last_key == 'E':
                pressE()
            pressE()
            last_key = "E"
    time.sleep(0.5)
    pyautogui.click(1306, 435)


def slovlia():
    time.sleep(1)
    i=0
    while i<20:
        pimana_pixel_srazu = pyautogui.pixel(930, 235)
        if 200 <= pimana_pixel_srazu[1] <= 205:
            print('srazu',pimana_pixel_srazu)
            return 'gotovo'
        i+=1
    return 'huevo'
        
def walking(napram):
    time.sleep(2)
    if napram == 'l':
        a,d = 'a','d'
        napram = 'r'
    else:
        a,d = 'd','a'
        napram = 'levo'
    keyboard.press('c')
    time.sleep(0.5)
    keyboard.release('c')
    keyboard.press(a)
    time.sleep(1.5)
    keyboard.release(a)
    keyboard.press('w')
    time.sleep(5)
    keyboard.press(d)
    time.sleep(1)
    keyboard.release(d)
    time.sleep(4)
    keyboard.release('w')
    time.sleep(1)
    keyboard.press(d)
    time.sleep(1)
    keyboard.release(d)
    time.sleep(4)
    keyboard.press('c')
    time.sleep(0.5)
    keyboard.release('c')
    return napram 


def priverka():
    while True:
        pimana_pixel_kartinka = pyautogui.pixel(930, 235)
        if 200 <= pimana_pixel_kartinka[1] <= 205 or 210 <= pimana_pixel_kartinka[0] <= 225:
            print(pimana_pixel_kartinka[1])
        
        print('asd',pimana_pixel_kartinka[0])

def vvodcapcha():
    while True:
        try:
            while True:
                updates = bot.get_updates(offset=recive('update_id'), limit=1)
                if updates != []:
                    dump_update()
                    message = updates[0].message.text
                    break
            if message[0] == '0':
                break
            elif message[0] == '1':
                print('vvod', message, updates[0].update_id)
                pyautogui.click(960, 621)
                keyboard.press('backspace')
                keyboard.release('backspace')
                keyboard.press('backspace')
                keyboard.release('backspace')
                keyboard.press('backspace')
                keyboard.release('backspace')
                keyboard.press('backspace')
                keyboard.release('backspace')
                keyboard.write(message[1:])
                keyboard.press_and_release('enter')
            elif message[0] == '2':
                position=[[884, 512],[963, 512],[1042, 512],
                        [884, 588],[963, 588],[1042, 588],
                        [884, 665],[963, 665],[1042, 665]]
                pyautogui.click(position[int(message[1])-1])
            elif message[0] == '3':
                position=[[980, 642],[980, 676],[980, 707]]
                pyautogui.click(position[int(message[1])-1])
            time.sleep(2)
            bot.send_photo(1259834978, pyautogui.screenshot(region=(740, 310,440, 480) ))
        except:
            bot.send_message(1259834978, 'ДОВБОЙОБ')
    
def timewrite(timing):
    with open('time.txt','a')as file:
        file.write(f'{str(int(time.time()- timing))}\n')

keyboard.wait('alt+b')
time.sleep(2 )


prohod = 0
kuda = 'r'
while True:
    timing_na4alo = time.time()
    if prohod == 3:
        kuda = walking(kuda)
        prohod = 0
    print('Prohod:', prohod)
    podcepit(1)
    prohod +=1
    captcha = lovlia()
    if captcha == 'capcha':
        vvodcapcha()
        dump(captcha)
    else:
        captcha = slovlia()
        dump(captcha)
    timewrite(timing_na4alo)
    time.sleep(4)
