import win32com.client
import keyboard
import numpy
from time import sleep
from os import system
from os import path
from os import remove

check_file = path.exists("fps_value.dat")

check_win = path.exists("C:\Windows\SysWOW64")
if check_win == True:
  clear = 'cls'
else:
  clear = 'clear'

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

system(clear)
if check_file != True:
    build_fps = int(input("Enter Desired Framerate: "))
    file0 = open('fps_value.dat','x')
    file0.close()

    byte_array = bytearray(build_fps.to_bytes(2, byteorder='big'))
    reversed_array = byte_array[::-1]
    with open('fps_value.dat','rb+') as file1:
        file1.write(reversed_array)
        file1.close()

if check_file == True:
    call_last_value = open('fps_value.dat','rb+')
    fps_value_read = call_last_value.read()
    build_fps = int.from_bytes(fps_value_read[::-1], byteorder='big')


shell = win32com.client.Dispatch("WScript.Shell")
print("Press the 'Enter' Key While Inside of Vampire Slayer.")
keyboard.wait('Enter')
shell.sendkeys('`')
shell.sendkeys('t')
shell.sendkeys('.')
shell.sendkeys('m')
shell.sendkeys('a')
shell.sendkeys('x')
shell.sendkeys('f')
shell.sendkeys('p')
shell.sendkeys('s')
shell.sendkeys(' ')
shell.sendkeys(build_fps)

keyboard.press_and_release('Enter')

shell.sendkeys('`')
shell.sendkeys('s')
shell.sendkeys('t')
shell.sendkeys('a')
shell.sendkeys('t')
shell.sendkeys(' ')
shell.sendkeys('f')
shell.sendkeys('p')
shell.sendkeys('s')
keyboard.press_and_release('Enter')
