import os
import webbrowser
from webbot import Browser
import pyautogui as gui
from python_imagesearch.imagesearch import imagesearch
#from selenium import webdriver 
import time
from datetime import date

login = "yout_login"
password = "your_password"
path_to_photos = "path_to_photos"

today = date.today()
d1 = today.strftime("%d.%m.%Y")

driver = Browser()
driver.go_to('https://www.instagram.com/')
time.sleep(2)
driver.click('Akceptuj') 
time.sleep(4)
driver.click('Zezwól')
time.sleep(2)
driver.click('Zaloguj')  
time.sleep(2)
driver.type(login, into = 'Login')
time.sleep(2)
driver.type(password, into = 'Password')
time.sleep(4)
driver.click('Zaloguj się') 
time.sleep(3)
driver.click('Zapisz') 
time.sleep(4)
driver.click('Zapisz') 
time.sleep(4)
driver.click("add.png")
pos_add = imagesearch("add.png")
while pos_add[0] == -1:
    time.sleep(2)
    if pos_add[0] != -1:
        print("position : ", pos_add[0], pos_add[1])
    else:
        print("add image not found")
time.sleep(2)
gui.doubleClick(pos_add[0]+10, pos_add[1]+10)
gui.click(pos_add[0]+10, pos_add[1]+10)
time.sleep(2)
driver.click('Wybierz') 
time.sleep(1)
pos = imagesearch("lupa.png")
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
else:
    print("lupa image not found")
time.sleep(2)
gui.click(pos[0]-100, pos[1]+10)
time.sleep(2)
gui.typewrite(path_to_photos, interval=0.01)
time.sleep(2)
gui.press('enter')
time.sleep(2)
gui.click(pos[0]+10, pos[1]+10)
time.sleep(2)
gui.typewrite(d1, interval=0.01)
time.sleep(2)
gui.press('enter')
time.sleep(2)
gui.doubleClick(pos[0]+10, pos[1]+80)
time.sleep(2)
gui.keyDown('ctrl')
gui.press('a')
gui.keyUp('ctrl')
time.sleep(2)
gui.doubleClick(pos[0]+10, pos[1]+550)
time.sleep(2)
driver.click("Dalej")
time.sleep(2)
driver.click("Dalej")
time.sleep(2)
#driver.click("Udostępnij")