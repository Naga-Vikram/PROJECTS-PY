import win32com.client

def speak(text):
    """Speaks the given text using the Windows SAPI."""
    
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
    


while True:
    command = input("Enter text to speak (or type 'quit' to exit): ")
    if command.lower() == 'quit':
        break
