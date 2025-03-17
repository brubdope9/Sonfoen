from random import randint, choice
from Items import items
from noise import pnoise2 as perlin
from main import color

class map:
  terrain = ['plains', 'forest', 'mountain', 'water']
  features = {'forest': ['tree', 'bush'], 'mountain': ['boulder', 'cave'], 'water': ['seaweed', 'coral']}
  naturalItems = {'forest': ['stick', 'rock', 'mushroom'], 'mountain': ['rock', 'gem', 'fossil'], 'water': ['fish', 'shell', 'seaweed']}
  chanceItems = {'forest': 20, 'mountain': 15, 'water': 45}
  
  
  
  def __init__(self, width:int, height:int, type:str = 'plains'):
    self.width = width
    self.height = height
    self.type = type
    self.tiledata = {}
    map.generate(self)
    
  


  def generate(self):
    for x in range(self.width):
      for y in range(self.height): 
        scale = 55.4

        terrainValue  = perlin(x/scale, y/scale, octaves=2, persistence=0.6, lacunarity=2.5, base= randint(1, 1000000))
        if terrainValue < 0:
          terrainValue *= -1
        if terrainValue >= 0.2:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'mountain', 'items': [], 'features': []}
        elif terrainValue >= 0.145:  
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'forest', 'items': [], 'features': []} 
        elif terrainValue >= 0.1:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'plains', 'items': [],'features': []}
        else:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'water', 'items': [],'features': []}
        # add features
        featureChance = randint(1, 100)
        if featureChance <= 10:
          
          self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
     

  def display(self):
    for y in range(self.height):
      row = []
      for x in range(self.width):
        terrain = self.tiledata[f"{x}, {y}"]['terrain']
        if terrain == 'plains':
            row.append(f"{color.lightgreen}P{color.end}")
        elif terrain == 'forest':
            row.append(f"{color.darkgreen}T{color.end}")
        elif terrain == 'mountain':
            row.append(f"{color.magenta}M{color.end}")
        elif terrain == 'water':
            row.append(f"{color.blue}#{color.end}")
      print(' '.join(row))


  def add_item(self, x:int, y:int, item:str):
    self.tiledata[f"{x}, {y}"]['items'].append(item)

    
        

testMap = map(75, 10)
#print(testMap.tiledata)
testMap.display()