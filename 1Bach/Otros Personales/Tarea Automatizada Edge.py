import os
import pyautogui
import time
import random

os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

time.sleep(3)
pyautogui.write('Comenzando Tarea Automatizada')

pyautogui.hotkey('enter')

n = 1
while (n <= 36):
    if(n == 35):
    
        break

    time.sleep(2)
    pyautogui.hotkey('ctrl','t')
    pyautogui.write(str(random.randint(0,99999999)))
    pyautogui.hotkey('enter')
    n += 1