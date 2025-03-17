from Player import Player

class Entity(Player):
    super().updateAll()
    def __init__(self, pos:list,):
        super().__init__(pos)
        self.hp = 100
        self.max_hp = 100
        self.isAlive = True
        self.damage = 10
        self.defense = 5
        self.level = 1
        self.exp = 0
        self.exp_to_level = 100
        self.inventory = []
        self.equips = {'head': None,
                       'body': None, 
                       'legs': None, 
                       'feet': None, 
                       'weapon': None, 
                       'shield': None}
        self.money = 0
class Enemy(Entity):
    pass