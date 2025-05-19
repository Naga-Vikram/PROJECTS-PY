import winsound
import os
import time
from datetime import datetime

# def notify(message, sound):
#     print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
#     if sound == 'default':
#         winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
#     elif sound == 'asterisk':
#         winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
#     elif sound == 'exclamation':
#         winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
#     elif sound == 'hand':
#         winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
#     elif sound == 'question':
#         winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
#     elif sound:
#         if os.path.exists(sound):
#             winsound.PlaySound(sound, winsound.SND_FILENAME)
#         else:
#             print(f"Warning: Sound file '{sound}' not found.")

# # Example usage:


while True:
    
    from win10toast import ToastNotifier
    time.sleep(6)
    toaster = ToastNotifier()
    toaster.show_toast("Drink Water!", "It's time to hydrate.", duration=10)
    


    