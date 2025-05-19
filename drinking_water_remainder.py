"""This Python script uses the win10toast library to display a "Drink Water!" notification every 2 hours on Windows 10"""
import winsound
import os
import time
from datetime import datetime

while True:
    
    from win10toast import ToastNotifier
    time.sleep(7200)
    toaster = ToastNotifier()
    toaster.show_toast("Drink Water!", "It's time to hydrate.", duration=10)
    


    
