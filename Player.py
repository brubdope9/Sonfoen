from main import color
from Items import items
class Player:
  def __init__(self, pos:list):
    self.hp = 100
    self.max_hp = 100
    self.isAlive = True
    self.damage = 10
    self.defense = 10
    self.level = 1
    self.exp = 0
    self.exp_to_level = 100
    self.inventory = []
    self.equips = {'head': None, 'body': None, 'legs': None, 'feet': None, 'weapon': None, 'shield': None}
    self.money = 0
    self.name = None
    self.pos = pos
  def update(self):
    if self.hp <= 0:
      self.isAlive = False
    if self.exp >= self.exp_to_level:
      self.level += 1
      self.exp -= self.exp_to_level
      self.exp_to_level = (self.exp_to_level * 1.5)
      self.max_hp += 10
      self.hp = self.max_hp
      self.damage += 5
      self.defense += 5
      print(f"{color.green}You leveled up to level {self.level}!{color.end}")
  def use_item(self, item:str:
    