import winsound
import os
import time
from datetime import datetime

while True:
    
    from win10toast import ToastNotifier
    time.sleep(6)
    toaster = ToastNotifier()
    toaster.show_toast("Drink Water!", "It's time to hydrate.", duration=10)
    


    
