from random import randint, choice
from Items import items
from main import color
from opensimplex import OpenSimplex

gen = OpenSimplex(seed=randint(1, 1000000))
def octave_noise2(x, y, octaves=1, persistence=0.5, lacunarity=2.0):
          """ Mimics pnoise2 with octaves, persistence, and lacunarity """
          amplitude = 1.0  # Controls how strong each layer of noise is
          frequency = 1.0  # Controls how zoomed in the noise is
          value = 0.0  # Stores the final noise value 
          max_amplitude = 0.0  # Used for normalization
          for _ in range(octaves):
            value += gen.noise2(x * frequency, y * frequency) * amplitude
            max_amplitude += amplitude
            amplitude *= persistence  # Reduces amplitude for next octave
            frequency *= lacunarity  # Increases frequency for next octave

          return value / max_amplitude  # Normalize to keep values between -1 and 1 t
  

class map:
  terrain = ['plains', 'forest', 'mountain', 'water', 'beach']
  features = {'plains':['bush', 'tree' ],'forest': ['tree', 'bush'], 'mountain': ['boulder', 'cave'], 'water': ['seaweed', 'coral'], 'beach': ['palm tree', ]}
  naturalItems = {'plains':[],'forest': ['stick', 'rock', 'mushroom'], 'mountain': ['rock', 'gem', 'fossil'], 'water': ['fish', 'shell', 'seaweed'], 'beach': ['shell', 'seaweed', 'rock']}
  chanceItems = {'plains': 10,'forest': 20, 'mountain': 15, 'water': 45}
  chanceFeatures = {'plains': 15,'forest': 45, 'mountain': 25, 'water': 30, 'beach': 1}
  structures = {'plains': ['farm', 'village'], 'forest': ['cabin', 'camp'], 'mountain': ['mine', 'cabin'], 'water': ['dock', 'shipwreck'], 'beach': ['dock', 'cabin']}
  chanceStructures = {'plains': 3,'forest': 7, 'mountain': 8, 'water': 2, 'beach': 2}

  
  
  
  def __init__(self, width:int, height:int, type:str = 'plains'):
    self.width = width
    self.height = height
    self.type = type
    self.tiledata = {}
    map.generate(self)
    self.overworld = self.tiledata


    
  # chunking not yet imple


  def generate(self):
    x_offset = randint(1, 10000)
    y_offset = x_offset/2
    col = 0
    for x in range(self.width):
      l = 0
      for y in range(self.height): 
        scale = 55.6
        scale = 3 # 10
        
        # terrainValue  = perlin(x/scale, y/scale, octaves=2, persistence=0.6, lacunarity=2.5, base=base,)
        terrainValue  = octave_noise2((x+x_offset)/scale, (y+y_offset)/scale, octaves=6, persistence=0.3, lacunarity=3.0)
        '''if terrainValue < 0:
          terrainValue *= -1'''
        
        if terrainValue >= 0.53:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'mountain', 'items': [], 'features': []}
        elif terrainValue >= 0.36:  
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'forest', 'items': [], 'features': []} 
        elif terrainValue >= 0.045:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'plains', 'items': [],'features': []}
        elif terrainValue  >= -0.1:
           self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'beach', 'items': [],'features': []}
        else:
          self.tiledata[f"{x}, {y}"] = {'tile':[x, y],'terrain': 'water', 'items': [],'features': []}
         # add features
        featureChance = randint(1, 100)
        if featureChance <= map.chanceFeatures[self.tiledata[f"{x}, {y}"]['terrain']]:
          numfeatures = randint(1, 3)
          match numfeatures:
            case 1:
              self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
            case 2:
              self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
              self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
              
            case 3:
              self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
              self.tiledata[f"{x}, {y}"]['features'].append(choice(map.features[self.tiledata[f'{x}, {y}']['terrain']]))
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

  def displaysolid(self):
   for y in range(self.height):
      row = []
      for x in range(self.width):
        terrain = self.tiledata[f"{x}, {y}"]['terrain']
        if terrain == 'plains':
            row.append(f"{color.lightgreen}#{color.end}")
        elif terrain == 'forest':
            row.append(f"{color.darkgreen}#{color.end}")
        elif terrain == 'mountain':
            row.append(f"{color.magenta}#{color.end}")
        elif terrain == 'water':
            row.append(f"{color.blue}#{color.end}")
        elif terrain == 'beach':
            row.append(f"{color.tan}#{color.end}")    
      print(''.join(row))
  def generateSubMap(self):
    pass
  
      
      
  
  def printfeatures(self):
    for x in range( self.width):
      for y in range(self.height):
        print(f"{x}, {y}: {self.tiledata[f'{x}, {y}']['features']}")

  def add_item(self, x:int, y:int, item:str):
    self.tiledata[f"{x}, {y}"]['items'].append(item)

    
        

testMap = map(145, 20 )
#print(testMap.tiledata)
#testMap.display()
testMap.displaysolid()
# testMap.printfeatures()

  