from random import randint, choice
from Items import items
from Color import color
from opensimplex import OpenSimplex
from Player import player



gen = OpenSimplex(seed=randint(1, 1000000))
def octave_noise2(x, y, octaves=1, persistence=0.5, lacunarity=2.0, seed = 0):
          """ Mimics pnoise2 with octaves, persistence, and lacunarity """
          amplitude = 1.0  # Controls how strong each layer of noise is
          frequency = 1.0  # Controls how zoomed in the noise is
          value = 0.0  # Stores the final noise value 
          max_amplitude = 0.0  # Used for normalization
          if seed != 0:
              for _ in range(octaves):
                  value += OpenSimplex(seed=seed).noise2(x * frequency, y * frequency) * amplitude
                  max_amplitude += amplitude
                  amplitude *= persistence  # Reduces amplitude for next octave
                  frequency *= lacunarity  # Increases frequency for next octave

          else:
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
  
  
  
  def __init__(self, width:int, height:int, type:str = 'plains', cgen:bool = False, mplayer:player = None):
    self.width = width
    self.height = height
    self.type = type
    self.tiledata = {}
    self.cseeds = {}
    if not cgen:
      map.generate(self)
    else:
        self.cgen()
        self.loadedChunks = {}
    if mplayer:
        self.player = mplayer
        self.player.setMap(self)


    self.overworld = self.tiledata




  def generate(self):
    x_offset = randint(1, 10000)
    y_offset = x_offset/2

    for x in range(self.width):
      for y in range(self.height):
        # scale = 55.6
        scale = 10
        
        # terrainValue  = perlin(x/scale, y/scale, octaves=2, persistence=0.6, lacunarity=2.5, base=base,)
        terrainValue  = octave_noise2((x+x_offset)/scale, (y+y_offset)/scale, octaves=6, persistence=0.3, lacunarity=3.0)


        if terrainValue >= 0.53:
          self.tiledata[(x, y)] = {'tile':(x, y),'terrain': 'mountain', 'items': [], 'features': []}
        elif terrainValue >= 0.36:
          self.tiledata[(x, y)] = {'tile':(x, y),'terrain': 'forest', 'items': [], 'features': []}
        elif terrainValue >= 0.045:
          self.tiledata[(x, y)] = {'tile':(x, y),'terrain': 'plains', 'items': [],'features': []}
        elif terrainValue  >= -0.1:
           self.tiledata[(x, y)] = {'tile':(x, y),'terrain': 'beach', 'items': [],'features': []}
        else:
          self.tiledata[(x, y)] = {'tile':(x, y),'terrain': 'water', 'items': [],'features': []}
         # add features
        featureChance = randint(1, 100)
        if featureChance <= map.chanceFeatures[self.tiledata[(x, y)]['terrain']]:
          numfeatures = randint(1, 3)
          match numfeatures:
            case 1:
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))
            case 2:
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))

            case 3:
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))
              self.tiledata[(x, y)]['features'].append(choice(map.features[self.tiledata[(x, y)]['terrain']]))

            
            

  def cgen(self): # generate with chunking
      chunk_x, chunk_y = 0, 0  # initialize chunk coordinates
      seed = randint(1, 1000000)  # generate a random seed for this chunk
      self.cseeds[(chunk_x, chunk_y)] = seed  # store the seed for this chunk
      scale = 5
      for x in range(self.width):
          for y in range(self.height):




              # terrainValue  = perlin(x/scale, y/scale, octaves=2, persistence=0.6, lacunarity=2.5, base=base,)
              terrainValue = octave_noise2(x / scale, y/ scale, octaves=6, persistence=0.3, lacunarity=3.0, seed=seed)

              if terrainValue >= 0.53:
                  self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'mountain', 'items': [], 'features': []}
              elif terrainValue >= 0.36:
                  self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'forest', 'items': [], 'features': []}
              elif terrainValue >= 0.045:
                  self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'plains', 'items': [], 'features': []}
              elif terrainValue >= -0.1:
                  self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'beach', 'items': [], 'features': []}
              else:
                  self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'water', 'items': [], 'features': []}
              # add features
              featureChance = randint(1, 100)
              if featureChance <= map.chanceFeatures[self.tiledata[(x, y)]['terrain']]:
                  numfeatures = randint(1, 3)
                  match numfeatures:
                      case 1:
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))
                      case 2:
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))

                      case 3:
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))
                          self.tiledata[(x, y)]['features'].append(
                              choice(map.features[self.tiledata[(x, y)]['terrain']]))

  def loadChunk(self, chunk_x, chunk_y):
    seed = randint(1, 1000000)  # generate a random seed for this chunk
    self.cseeds[(chunk_x, chunk_y)] = seed  # store the seed for this chunk
    scale = 5
    for x in range(chunk_x * self.width, (chunk_x + 1) * self.width):
        for y in range(chunk_y * self.height, (chunk_y + 1) * self.height):
            #global_x = x + chunk_x * self.width
            #global_y = y + chunk_y * self.height

            # terrainValue  = perlin(x/scale, y/scale, octaves=2, persistence=0.6, lacunarity=2.5, base=base,)
            terrainValue = octave_noise2(x / scale, y/ scale, octaves=6, persistence=0.3, lacunarity=3.0, seed=seed)

            if terrainValue >= 0.53:
                self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'mountain', 'items': [], 'features': []}
            elif terrainValue >= 0.36:
                self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'forest', 'items': [], 'features': []}
            elif terrainValue >= 0.045:
                self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'plains', 'items': [], 'features': []}
            elif terrainValue >= -0.1:
                self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'beach', 'items': [], 'features': []}
            else:
                self.tiledata[(x, y)] = {'tile': (x, y), 'terrain': 'water', 'items': [], 'features': []}


  def UnloadChunk(self, chunk_x, chunk_y):
   pass

  def display(self):
    for y in range(self.height):
      row = []
      for x in range(self.width):
        terrain = self.tiledata[(x, y)]['terrain']
        if terrain == 'plains':
            row.append(f"{color.lightgreen}P{color.end}")
        elif terrain == 'forest':
            row.append(f"{color.darkgreen}T{color.end}")
        elif terrain == 'mountain':
            row.append(f"{color.magenta}M{color.end}")
        elif terrain == 'water':
            row.append(f"{color.blue}#{color.end}")
        elif terrain == 'beach':
            row.append(f"{color.tan}#{color.end}")

      print(' '.join(row))

  def displaysolid(self):
   for y in range(self.height):
      row = []
      for x in range(self.width):
        terrain = self.tiledata[(x, y)]['terrain']
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

  def displaysolidAll(self):
      min_x = min(chunk_x for chunk_x, chunk_y in self.cseeds)
      max_x = max(chunk_x for chunk_x, chunk_y in self.cseeds)
      min_y = min(chunk_y for chunk_x, chunk_y in self.cseeds)
      max_y = max(chunk_y for chunk_x, chunk_y in self.cseeds)

      for y in range((max_y + 1) * self.height, (min_y - 1) * self.height - 1, -1):
          row = []
          for x in range((min_x - 1) * self.width, (max_x + 1) * self.width):
              if (x, y) in self.tiledata:

                  terrain = self.tiledata[(x, y)]['terrain']
                  if hasattr(self, 'player') and self.player.pos == [x, y]:
                      row.append(f"{color.red}P{color.end}")

                  elif terrain == 'plains':
                      row.append(f"{color.lightgreen}#{color.end}")
                  elif terrain == 'forest':
                      row.append(f"{color.darkgreen}#{color.end}")
                  elif terrain == 'mountain':
                      row.append(f"{color.magenta}#{color.end}")
                  elif terrain == 'water':
                      row.append(f"{color.blue}#{color.end}")
                  elif terrain == 'beach':
                      row.append(f"{color.tan}#{color.end}")
                  else:
                      row.append(" ")
          print(''.join(row))

  def generateSubMap(self):
    pass
  
      
      
  
  def printfeatures(self):
    for data in self.tiledata:
        print(data)

  def add_item(self, x:int, y:int, item:str):
    self.tiledata[f"{x}, {y}"]['items'].append(item)

    
        
'''
testMap = map(20, 7, cgen=True)
#print(testMap.tiledata)
#testMap.display()
testMap.loadChunk(21, 1)
# testMap.displaysolid()
testMap.displaysolidAll()
#testMap.printfeatures()

'''