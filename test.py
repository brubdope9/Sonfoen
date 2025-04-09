
from Map import map, randint, choice
from Player import player, color
from Entities import Entity
from math import floor
from os import system
player = player([0,0])
m = map(10, 5, cgen=True, mplayer=player)
#screenLengthY = 1
#screenLengthX = 1

player.inventory.append('carrot')



# renderDistance = 1
moved = False
while True:
    

    system('clear')
    m.displaysolidAll()

    print("pos: ", player.pos)
    currentChunk = (floor(player.pos[0]/m.width), floor(player.pos[1]/m.height))
    print("currentChunk: ", currentChunk)
    try:
        print(m.tiledata[(player.pos[0], player.pos[1])])
    except KeyError:
        pass
    a = input('')
    if a == 'w':

        if (player.pos[0], player.pos[1]+1) not in m.tiledata:
            player.move('up')
            m.loadChunk(floor(player.pos[0]/m.width), floor(player.pos[1]/m.height))
            m.UnloadChunk(currentChunk[0], currentChunk[1])
        else:  
            player.move('up')
        moved=True
    elif a == 's':
        if (player.pos[0], player.pos[1]-1) not in m.tiledata:
            player.move('down')
            m.loadChunk(floor(player.pos[0]/m.width), floor(player.pos[1]/m.height))
            m.UnloadChunk(currentChunk[0], currentChunk[1])
        else:
            player.move('down')
        moved=True


    elif a == 'a':
        if (player.pos[0]-1, player.pos[1]) not in m.tiledata:
            player.move('left')
            m.loadChunk(floor(player.pos[0]/m.width), floor(player.pos[1]/m.height))
            m.UnloadChunk(currentChunk[0], currentChunk[1])
        else:
            player.move('left')
        moved=True
    


    elif a == 'd':
        if (player.pos[0]+1, player.pos[1]) not in m.tiledata:
            player.move('right')
            m.loadChunk(floor(player.pos[0]/m.width), floor(player.pos[1]/m.height))
            m.UnloadChunk(currentChunk[0], currentChunk[1])
        else:
            player.move('right')
        moved=True

    elif a == 'q':
        while True:
            system('clear')
            print('**allocating skill points**')
            print(f'You have {player.skillPoints} skill points to allocate!')
            print(f'Your stats (including equip bonuses) are:\nMax Health: {player.maxHp} \nDamage: {player.damage} \nDefense: {player.defense} \nMagic Damage: {player.magicDamage} \nMagic Defense: {player.baseDefense} \nMana: {player.maxMana}')
            print('What stat would you like to allocate points to?')
            allocChoice = input('Max health (hp), damage (dmg), defense (df), magic damage (mdmg), magic defense (mdf), mana (m), or exit (x)\n').lower()

            if allocChoice == 'hp':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('hp', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        a = input('enter to continue')
                        if a == '':
                            continue 
                        
            elif allocChoice == 'dmg':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('damage', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        a = input('enter to continue')
                        if a == '':
                            continue
            elif allocChoice == 'df':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('defense', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        a = input('enter to continue')
                        if a == '':
                            continue
                        continue
            elif allocChoice == 'mdf':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('magicDefense', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        continue
            elif allocChoice == 'm':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('mana', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        continue
            elif allocChoice == 'mdmg':
                try:
                    points = int(input('How many skill points would you like to allocate?'))
                    player.allocSkillPoints('magicDamage', points)
                except ValueError:
                        print('Invalid input. Please enter a number.')
                        continue
            elif allocChoice == 'x':
                break
            else:
                while True:
                    system('clear')
                    print('Invalid input. Please enter a valid stat.')
                    a = input('enter to continue')
                    if a == '':
                        break
    elif a == 'e':
        invT = []
        while True:
        
            system('clear')
            print('**Inventory**')
            for i in player.equips:
                if player.equips[i] != None:
                    print(f'{i}: {player.equips[i]['name']}')
                else:
                    print(f'{i}: empty')
            print('\n')
            
            print('Your items are:')
            for i in player.inventory:
                if i not in invT:
                    invT.append(i)
                    print(f'{i}: { player.inventory.count(i)}')
                
            a = input('equip (e), use (u), drop (d), or exit (x)?\n')
            if a == 'x':
                del invT
                break
            elif a == 'e':  
                a= input('Which item would you like to equip?\n')
                if a in player.inventory:
                    player.equipItem(a)

                    player.inventory.remove(a)
                    player.checkEquips()
                    print(f'You equipped {a}!')
                else:
                    print(f'You do not have {a} in your inventory!')        
            else:
                invT.clear()
                      

    encounterChance = randint(1, 100)
    if encounterChance <= 15 and moved:
        opponent = Entity([0, 0], choice(['pig']), lvl=randint(1, player.level))
        while True:
            system('clear')
            print(f'You encountered a {opponent.entType}!\n{opponent}\n')
            print(f'You: \nHealth:{player.hp}/{player.maxHp} \nDefense: {player.defense} \nDamage: {player.damage} \nMana: {player.mana}/{player.maxMana}\n')
            Option = input('\nAttack (a),Defend (d), or Use an item (u)?\n')
            if Option == 'a':
                player.hit(opponent)
                opponent.hit(player)

            elif Option == 'd':
                player.defend()
                opponent.hit(player)
                player.undefend()
                
    

            else:
                print('Invalid option')

            if not opponent.checkAlive():
                player.exp += opponent.expGiven
                
                while True:
                    system('clear')
                    print(f'You defeated the {opponent.entType}!\nYou gained {opponent.expGiven} experience points!')
                    if player.checkLevelUp():
                        print(f'{color.green}You leveled up! You are now level {player.level}!')
            
                        print(f'You have {player.skillPoints} skill points to allocate!{color.end}')
                    a = input('\nenter to continue')
                    if a == '':
                        break

                opponent.erase()
                player.inventory.append(opponent.loot[0])
                break
            if not player.checkAlive():
           
                break
    moved = False
    if not player.isAlive:
        print(f'You died! You were level {player.level} with {player.hp}/{player.maxHp} hp.')
        break
    