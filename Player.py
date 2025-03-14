from main import color
from Items import items
from Map import map
class Player:
  def __init__(self, pos:list):
    self.hp = 100
    self.max_hp = 100
    self.isAlive = True
    self.damage = 10
    self.defense = 5
    self.level = 1
    self.exp = 0
    self.exp_to_level = 100
    self.inventory = []
    self.equips = {'head': None, 'body': None, 'legs': None, 'feet': None, 'weapon': None, 'shield': None}
    self.money = 0
    self.name = None
    self.pos = pos
  def update(self):
    #check if player has equipped items
    # Reset player's attack and defense to base values
    self.damage = 10
    self.defense = 5

    # Update player's attack and defense based on equipped items
    for equip in self.equips.items():
      if equip:
       if 'defense' in equip:
         self.defense += equip['defense']
         if 'attack' in equip:
          self.damage += equip['attack']

    #check if player is alive
    if self.hp <= 0:
      self.isAlive = False
    
    #check if player leveled up  
    if self.exp >= self.exp_to_level:
      self.level += 1
      self.exp -= self.exp_to_level
      self.exp_to_level = (self.exp_to_level * 1.5)
      self.max_hp += 10
      self.hp = self.max_hp
      self.damage += 5
      self.defense += 5
      print(f"{color.green}You leveled up to level {self.level}!{color.end}")
      print(f"{color.green}Your max hp is now {self.max_hp}!{color.end}")
      print(f"{color.green}Your damage is now {self.damage}!{color.end}")
      print(f"{color.green}Your defense is now {self.defense}!{color.end}")

  
  def add_item(self, item:str):
    if item in items:
      self.inventory.append(items[item])
    else: 
      raise ValueError(f"{color.red}Item {item} not found in items list{color.end}")
    