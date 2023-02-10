import pydirectinput
import keyboard
from os import path
from os import system
from time import sleep

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

system(clear)

def Load():
  sleep(1)
  print("Created By:  r       ")
  sleep(0.15)
  system(clear)
  print("Created By:  r c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c     ")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c    8")
  sleep(0.15)
  system(clear)
  print("Created By: Cr c  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac  2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o2 8")
  sleep(0.15)
  system(clear)
  print("Created By: Crac o298")
  sleep(0.15)
  system(clear)
  print("Created By: Cracko298")
  sleep(4)
  system(clear)
Load()

use = int(input("Enter Desired Framerate: "))

system(clear)

print("Press 'Enter' To Set Framerate.")

keyboard.wait('Enter')
pydirectinput.press('left')
pydirectinput.typewrite(f'`t.maxfps {use}')
pydirectinput.press('Enter')
