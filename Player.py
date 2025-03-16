from main import color
from Items import items
from Map import map
from Actions import Actions
class Player:
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
    self.max_mana = 100 
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
    self.actions = Actions()
  
  def checkEquips(self):
      # Reset player's attack, defense, and magic damage to base values
      self.damage = 10
      self.defense = 5
      self.magicDamage = 10

      # Update player's stats based on equipped items
      for equip in self.equips.values():
          if equip:
              if 'defense' in equip:
                  self.defense += equip['defense']
              if 'attack' in equip:
                  self.damage += equip['attack']
              if 'magicDamage' in equip:
                  self.magicDamage += equip['magicDamage']
              if 'magicDefense' in equip:
                  self.magicDefense += equip['magicDefense']
              if 'maxHp' in equip:
                  self.maxHp += equip['maxHp']
              if 'maxMana' in equip:
                  self.max_mana += equip['maxMana']

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
      self.max_mana = self.baseMaxMana
      self.mana = self.max_mana

      print(f"{color.green}You leveled up to level {self.level}!{color.end}")
      print(f"{color.green}Your max hp is now {self.maxHp}!{color.end}")
      print(f"{color.green}Your damage is now {self.damage}!{color.end}")
      print(f"{color.green}Your defense is now {self.defense}!{color.end}")
      
      print(f"{color.green}Your max mana is now {self.max_mana}!{color.end}")
  def checkAlive(self):
    if self.hp <= 0:
      self.isAlive = False
      return False
    else:
      return True

  def updateAll(self):
    # Check if player has equipped items
    self.checkEquips()

    # Check if player is alive
    self.checkAlive()
    
    # Check if player leveled up  
    self.check_level_up()

  def add_item(self, item:str):
    if item in items:
      self.inventory.append(items[item])
    else: 
      raise ValueError(f"{color.red}Item {item} not found in items list{color.end}")
    