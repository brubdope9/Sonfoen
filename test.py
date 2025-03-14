from random import randint
from main import color
from time import sleep as wait
from os import system as syst
def ranBinary(num:int):
  for i in range(num):
    print(randint(0,1), end='')


print(color.green, end= '')

while True:
 print("> ", end='')
 a = input()
 match a:
  
  case "decode":
    for i in range(100):
      ranBinary(15)
    
  case 'clear':
    syst('clear')
    
  case 'exit':
    exit()
  case "game":
    syst("python main.py")
  
  case _:
    print(f"{color.red}\nInvalid command.{color.green}")

 print()