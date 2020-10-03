# Bot made by Maple

from keyboard import *
from time import sleep
import pyautogui as p, pyperclip
import os

# ready
os.system('echo Ready!')
p.failSafeCheck()
# open google
p.moveTo(600, 900)
p.moveTo(123, 750)
p.leftClick()
p.moveTo(180, 50)
p.leftClick()
# go to biglike
def paste(text001: str):
    pyperclip.copy(text001)
    press_and_release('ctrl + v')

p.hotkey('ctrl + z')
paste('https://biglike.org/ytlikes')
p.press('Enter')

p.moveTo(350, 500)
sleep(3)
p.leftClick()
sleep(8)
p.moveTo(1070, 100)
p.leftClick()
sleep(4)
p.moveTo(485, 375)
p.leftClick()
sleep(1)
p.moveTo(480, 765)
p.leftClick()
p.moveTo(488, 718)
p.leftClick()
p.moveTo(430, 715)
p.leftClick()
sleep(1)
p.moveTo(1250, 10)
p.leftClick()
sleep(2)
p.moveTo(325, 575)
p.leftClick()
# close window
sleep(4)
p.moveTo(600, 900)
p.moveTo(123, 750)
p.leftClick()
p.moveTo(320, 666)
p.leftClick()
p.moveTo(1350, 5)
p.leftClick()
# restart
sleep(5)
p.moveTo(600, 900)
p.moveTo(170, 750)
p.leftClick()
p.moveTo(1240, 50)
p.leftClick()
p.moveTo(750, 420)
p.leftClick()

#