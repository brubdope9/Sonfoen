from random import randint
class Entity:
    baseEnts= {
        'pig':{'hp': 30, 'dmg': 6, 'df' : 2, 'mana':0, 'mdmg': 0, 'mdf': 0, 'canEquip': False, 'expGiven': 100, 'loot': ['carrot'], 'lootChance': 100},
        'orc':{'hp': 130, 'dmg':17, 'df': 5, "mana": 1, 'mdmg': 0, 'mdf': 1, 'canEquip': False, 'expGiven': 30}, 
        'goblin':{'hp': 50, 'dmg': 10, 'df': 5, "mana": 1, 'mdmg': 0, 'mdf': 1, 'canEquip': False, 'expGiven': 10},
        'panda':{'hp': 75, 'dmg': 15, 'df': 10, "mana": 1, 'mdmg': 0, 'mdf': 1, 'canEquip': False, 'expGiven': 20},
        }
    activeEnts = []
    def __init__(self, pos: list,entType: str, lvl:int = 1):
        self.entType = entType
        self.pos =  pos
        self.hp = int(Entity.baseEnts[entType]['hp'] + randint(- int(Entity.baseEnts[entType]['hp']/10),int( Entity.baseEnts[entType]['hp']/10))*(1+(0.5*lvl) ))  
        self.maxHp = self.hp 
        self.isAlive = True
        self.damage = int(Entity.baseEnts[entType]['dmg'] + randint(- int(Entity.baseEnts[entType]['dmg']/10),int( Entity.baseEnts[entType]['dmg']/10))*(1+(0.5*lvl) ))
        self.defense = int(Entity.baseEnts[entType]['df'] + randint(- int(Entity.baseEnts[entType]['df']/10),int( Entity.baseEnts[entType]['df']/10))*(1+(0.5*lvl) ))
        self.level = lvl
        expGiven = Entity.baseEnts[entType]['expGiven']*(1+(0.5*lvl))
        if Entity.baseEnts[entType]['canEquip']:
            self.equips = {'head': None,
                           'body': None, 
                           'legs': None, 
                           'feet': None, 
                           'weapon': None, 
                           'shield': None
                           }
        self.money = 0
        self.loot = Entity.baseEnts[entType]['loot']
        self.lootChance = Entity.baseEnts[entType]['lootChance']
        
        self.expGiven = int(Entity.baseEnts[entType]['expGiven']*(1+(0.5*lvl)))
        Entity.activeEnts.append(self)


    
    def erase(self):
        Entity.activeEnts.remove(self)
        del self 
    def __str__(self):
        return f'type: {self.entType} \nhp: {self.hp}/{self.maxHp} \nAttack: {self.damage} \nDefense: {self.defense}'
    def hit(self, target):
        damageDealt = self.damage - target.defense
        if damageDealt > 0:
            target.hp -= damageDealt
    def defend(self):
        self.defense += self.defense / 20
    def undefend(self):
        self.defense -= self.defense / 20
    def checkAlive(self):
        if self.hp <= 0:
          self.isAlive = False
          return False
        else:
         return True


'''
from os import system, name 
system('cls' if name == 'nt' else 'clear')
a =  Entity([1, 2], 'panda', 1)
print('\n', Entity.activeEnts, '\n')
a.erase()
print(Entity.activeEnts)
print(a)'''