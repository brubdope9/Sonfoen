from Map import map
from Player import player
from os import system
player = player([0,0])
m = map(10, 5, cgen=True, mplayer=player)
m.loadChunk(-1, 0)
'''
m.loadChunk(1, 0)
m.loadChunk(2, 0)
m.loadChunk(3, 0)
m.loadChunk(3, -1)
m.loadChunk(3, 1)
'''

done = 0
while True:

    system('cls')
    m.displaysolidAll()
    done += 1
    #print("done: ", done)
    print("pos: ", player.pos)
    try:
        print(m.tiledata[(player.pos[0], player.pos[1])])
    except KeyError:
        pass
    a = input('')
    if a == 'w':
        player.move('up')
    elif a == 's':
        player.move('down')
    elif a == 'a':
        player.move('left')
    elif a == 'd':
        player.move('right')

    player.updateAll()