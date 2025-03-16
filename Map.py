from random import randint, choice
from Items import items
from noise import pnoise2 as perlin

class map:
  areaTypes = ['plains', 'desert']
  plainsTerrain = ["grass", 'dirt', 'flowerbed', 'cave']
  
  
  
  def __init__(self, width:int, height:int, type:str = 'plains'):
    self.width = width
    self.height = height
    self.type = type
    self.tiledata = {}
    map.generate(self)
    
  


  def generate(self):
    for x in range(self.width):
      for y in range(self.height): 
        
        self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': choice(map.plainsTerrain), 'items': []} 


  def add_item(self, x:int, y:int, item:str):
    self.tiledata[f"{x}, {y}"]['items'].append(item)

    
        

testMap = map(10, 10)
print(testMap.tiledata)


