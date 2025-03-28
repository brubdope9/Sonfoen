from Color import color
from Items import items

# from Actions import Actions
class player:
  def __init__(self, pos:list):
    self.pos = pos
    self.hp = 100
    self.baseMaxHp = 100
    self.maxHp = 100

    self.isAlive = True

    self.baseDamage = 10
    self.damage = 10
    
    self.baseDefense = 5
    self.defense = 5

    self.mana = 100
    self.baseMaxMana = 100
    self.maxMana = 100 
    self.baseMagicDamage = 10
    self.magicDamage = 10
    self.magicDefense = 5

    self.level = 1
    self.exp = 0
    self.exp_to_level = 100

    self.inventory = []
    self.equips = {
        'head': None,
        'body': None,
        'legs': None, 
        'feet': None, 
        'weapon': None, 
        'shield': None
        }
    
    self.money = 0
    self.name = None
  
  def checkEquips(self):
      # Reset player's attack, defense, and magic damage to base values
      self.damage = self.baseDamage
      self.defense = self.baseDefense
      self.magicDamage =  self.baseMagicDamage

      # Update player's stats based on equipped items
      for equip in self.equips.values():
          if equip is not None:
              if 'defense' in equip:
                  self.defense += equip['defense']
              if 'damage' in equip:
                  self.damage += equip['damage']
              if 'magicDamage' in equip:
                  self.magicDamage += equip['magicDamage']
              if 'magicDefense' in equip:
                  self.magicDefense += equip['magicDefense']
              if 'maxHp' in equip:
                  self.maxHp += equip['maxHp']
              if 'maxMana' in equip:
                  self.maxMana += equip['maxMana']
  def printStats(self):
     print(f'health: {self.hp}/{self.maxHp} \ndamage: {self.damage} \nmana: {self.mana}/{self.maxMana} \ndefense:{self.defense}')
  

    
  def check_level_up(self):
    # Check if player leveled up  
    if self.exp >= self.exp_to_level:
      self.level += 1
      self.exp -= self.exp_to_level
      self.exp_to_level = (self.exp_to_level * 1.5)
      
      self.baseMaxHp += 10
      self.maxHp = self.baseMaxHp
      self.hp = self.maxHp

      self.baseDamage += 5
      self.damage += 5

      self.baseDefense += 5
      self.defense += 5

      self.baseMaxMana += 10
      self.maxMana = self.baseMaxMana
      self.mana = self.maxMana

      print(f"{color.green}You leveled up to level {self.level}!{color.end}")
      print(f"{color.green}Your max hp is now {self.maxHp}!{color.end}")
      print(f"{color.green}Your damage is now {self.damage}!{color.end}")
      print(f"{color.green}Your defense is now {self.defense}!{color.end}")
      
      print(f"{color.green}Your max mana is now {self.maxMana}!{color.end}")
  def checkAlive(self):
    if self.hp <= 0:
      self.isAlive = False
      return False
    else:
      return True


  def updateAll(self):
    self.checkEquips()
    self.checkAlive()
    self.check_level_up()

  def add_item(self, item:str):
    if item in items:
      self.inventory.append(items[item])
  def equipItem(self, item:str):
    if item in items:
      self.equips[items[item]['slot']] = items[item]
  def setMap(self, map):
    self.map = map

  def move(self,direction, tilenum = 1):
    # could do this with one statement
    if direction == 'up':
     try:
      self.pos[1] += tilenum
     except KeyError:
         print ("out of bounds")
    elif direction == 'down':
     try:
      self.pos[1] -= tilenum
     except KeyError:
        print("out of bounds")
    elif direction == 'left':
      try:
       self.pos[0] -= tilenum
      except KeyError:
          print("out of bounds")
    elif direction == 'right':
      try:
       self.pos[0] += tilenum
      except KeyError:
          print("out of bounds")

