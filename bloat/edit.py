from init import *

tiles_load('etiles.png')

import sys

if len(sys.argv) != 2:
    print "python edit.py fname.lvl"
    sys.exit()

fname = sys.argv[1]

load(fname)

n = 0
quit = 0
while not quit:
    update_all()
    render()
    for e in pygame.event.get():
	if e.type is QUIT:
	    quit = 1
	elif e.type is KEYDOWN:
	    if e.key == K_s:
		save(fname)
	    elif e.key == K_l:
		load(fname)
	    elif e.key == K_ESCAPE:
		quit = 1
	    elif e.key in range(K_1,K_8+1):
		n = n/8*8 + e.key-K_1
		print n
	    elif e.key == K_9:
		n -= 8
		print n
	    elif e.key == K_0:
		n += 8
		print n
	elif e.type is MOUSEMOTION:
	    x,y = (e.pos[0]-AX)/TW,(e.pos[1]-AY)/TH
	    if e.buttons[0]!=0:
		game.map[y][x] = n
	elif e.type is MOUSEBUTTONDOWN:
	    x,y = (e.pos[0]-AX)/TW,(e.pos[1]-AY)/TH
	    if e.button==1:
		game.map[y][x] = n
	    elif e.button==3:
		n = game.map[y][x]
		
    
