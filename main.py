from random import randint, choice
import os
# import unicurses as c
import threading
class color:
   purple = '\033[38;5;135m'
   cyan = '\033[38;5;51m'
   darkcyan = '\033[38;5;36m'
   blue = '\033[38;5;27m'
   green = '\033[38;5;46m'
   lightgreen = '\033[38;5;156m'
   yellow = '\033[38;5;226m'
   red = '\033[38;5;196m'
   darkgreen = '\033[38;5;34m'
   magenta = '\033[38;5;201m'
   orange = '\033[38;5;214m'
   tan = '\033[38;5;220m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'
def clear():
  os.system('clear')
# c.initscr()