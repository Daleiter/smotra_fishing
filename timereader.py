import pyautogui
import keyboard
import time
s = 0
with open('time.txt','r') as file:
    lines= file.readlines()
for i in lines:
    s += int(i)
output = s/len(lines)
print(output/60,'min/one lovlia\n', s/3600,'/',len(lines),'hour/all lovlia')