from init import *
from math import *

"""
import sys

if len(sys.argv) != 2:
    print "python play.py fname.lvl"
    sys.exit()

fname = sys.argv[1]
"""

import random
def rand():
	return random.randrange(0,65536)
	

def run(state):
    while state != state_quit:
	state = state()
    state()

def state_quit():
    pass

def goat_new(x,y):
	a = sprite()
	a.toimage('goat.1')
	
	a.cur = Rect((x,y,32,32))
	a.prev = Rect((x,y,32,32))
	a.dest = Rect((x,y,32,32))
	a.x,a.y = x,y
	a.update = goat_update
	a.speed = 5
	a.type = 'goat'
	a.bloat = 0
	a.infected = 0
	a.timer = 0
	game.sprites.append(a)
	return a
	
def goat_update(a):
	if a.infected:
	    	x,y = a.cur.centerx/TW,a.cur.centery/TH
		game.infected[y][x]-=1
		
	#if a.cur.x != a.dest.x or a.cur.y != a.dest.y:
	a.toimage('goat.%d'%(1+a.bloat*2+(game.frames/12)%2))
	
	a.speed -= 0.01
	if a.speed < 5: a.speed = 5

	s = game.player
	dx,dy = a.cur.x-s.cur.x,a.cur.y-s.cur.y
	h = max(hypot(a.cur.x-s.cur.x,a.cur.y-s.cur.y),1)
	if h < 75:
		a.dest.x,a.dest.y = a.cur.x+dx+10-rand()%20,a.cur.y+dy+10-rand()%20
		item_angle(a)
		if rand()%45 == 0:
		    game.sounds['bah'].play()
		
	if rand()%100 == 0:
		a.dest.x,a.dest.y = rand()%VW,rand()%VH
		item_angle(a)
	
	if a.bloat != 3:
		item_move(a)
	
    	x,y = a.cur.centerx/TW,a.cur.centery/TH
	if game.infected[y][x] and a.infected == 0: 
	    a.infected = 1
	    game.score -= 50
	    game.sounds['infect'].play()
	n = game.map[y][x]
	if n/8 == 3:
		game.sprites.remove(a)
		game.total_saved += 1
		game.score += 100
		game.sounds['bloop'].play()
		return
	
	if a.infected:
		if a.timer == 0:
			a.bloat += 1
			a.timer = 500
			if a.bloat == 2:
			    game.sounds['infect'].play()
			if a.bloat == 3: 
			    a.timer = 20
			    game.sounds['bang'].play()
		a.timer -= 1
		if a.bloat == 4:
		    game.sprites.remove(a)
		    game.total_dead += 1
		    #game.infected[y][x] -= 1
		    game.score -= 100
		    return
		game.infected[y][x]+=1


KEYS,KUP,KDOWN,KLEFT,KRIGHT,KBUT = 5,0,1,2,3,4

def player_new(x,y):
    a = sprite()
    a.toimage('player.1')
    a.cur = Rect((x,y,32,32))
    a.prev = Rect((x,y,32,32))
    a.x,a.y = a.cur.x,a.cur.y
    a.dest = Rect((x,y,32,32))
    a.update = player_update
    a.speed = 5
    a.type = 'player'
    a.keys = [0 for i in range(0,KEYS)]
    a.px,a.py = 0,0
    game.sprites.append(a)
    return a


def solids(r,n):
	y = r.y
	while y < r.bottom:
		x = r.x
		while x < r.right:
			xx,yy = x/TW,y/TH
			game.solid[yy][xx]+=n
			if game.solid[yy][xx]<0:
				game.solid[yy][xx]=0 #HACK
			x+=TW
		y+=TH
			
def item_angle(a):
	#HACK
	dx = a.dest.x-a.cur.x
	dy = a.dest.y-a.cur.y
	a.angle = atan2(-dy,dx)
	a.angle = a.angle

def item_canmove(a,dx,dy,dp):
	ax = a.x+dx*dp
	ay = a.y+dy*dp
	a.cur.x,a.cur.y = ax,ay
	x,y = a.cur.centerx/TW,a.cur.centery/TH
	bad = 0
	n = game.map[y][x]
	if n/8 == 1: bad = 1
	if n/8 == 2 and a.type == 'goat': bad = 1
	if n/8 == 4 and a.type == 'player': bad = 1
	if not bad:
		a.x,a.y = ax,ay
	return 1-bad
	

def item_move(a):
	dx = a.dest.x-a.cur.x
	dy = a.dest.y-a.cur.y
	dt = hypot(dx,dy)
	if not dt: return
	dp = a.speed/dt
	if dp>1: dp=1
	
	bad = 1
	if item_canmove(a,dx,dy,dp): bad = 0
	elif item_canmove(a,dx,0,dp): bad = 0
	elif item_canmove(a,0,dy,dp): bad = 0
	
	if bad:
		a.cur.x,a.cur.y = a.prev.x,a.prev.y
		a.x,a.y = a.cur.x,a.cur.y

def player_update(a):
	#if a.cur.x != a.dest.x or a.cur.y != a.dest.y:
	a.toimage('player.%d'%(1+(game.frames/12)%2))
	item_move(a)
	

def state_play():
    game.score = 0
    game.level = 1
    return state_level

def state_level():
    fname = "%d.lvl"%game.level
    pygame.mixer.music.load("soldier.ogg")
    pygame.mixer.music.play(-1)
    game.sprites = []
    load(fname)
    game.frames = 0
    game.time = 100
    game.total_goats = 0
    game.total_dead = 0
    game.total_saved = 0
    for y in range(0,H):
	for x in range(0,W):
	    xx,yy=x*TW,y*TH
	    n = game.map[y][x]
	    if n == 1:
	        player = game.player = player_new(xx,yy)
	    elif n == 2:
		goat = goat_new(xx,yy)
		game.total_goats+=1
	    elif n == 3:
		goat = goat_new(xx,yy)
		goat.infected = 1
		goat.bloat = 1
		goat.timer=500
		game.total_goats+=1
    
    game.infected = [[0 for x in range(0,W)] for y in range(0,H)]
    for s in game.sprites:
	    if s.type == 'goat' and s.infected == 1:
		    x,y = s.cur.centerx/TW,s.cur.centery/TH
		    game.infected[y][x] += 1
	
    #so that all bloated goats show, etc
    for a in game.sprites:
	a.prev.x = a.cur.x
	a.prev.y = a.cur.y
	a.update(a)
		    
   
    screen.fill((0,0,0))
    update_all()
    message("GET READY!")
   
    game.nt = float(pygame.time.get_ticks())

    while 1:
	    #delay
	    ft = 1000.0/40.0
	    ct = pygame.time.get_ticks()
	    if ct < game.nt:
		pygame.time.wait(int(game.nt-ct))
		game.nt += ft
	    else:
		game.nt = float(ct) + ft

	    #render
	    render()

	    #events
	    for e in pygame.event.get():
		if e.type is KEYDOWN:
		    if e.key == K_ESCAPE:
			return state_hs
		    elif e.key == K_UP:
			player.keys[KUP] = 1
		    elif e.key == K_DOWN:
			player.keys[KDOWN] = 1
		    elif e.key == K_LEFT:
			player.keys[KLEFT] = 1
		    elif e.key == K_RIGHT:
			player.keys[KRIGHT] = 1
		    elif e.key == K_LCTRL:
			player.keys[KBUT] = 1
		    elif e.key == K_RETURN or e.key == K_p or e.key == K_SPACE:
			pygame.mixer.music.pause()
			message("PAUSE")
			pygame.mixer.music.unpause()
		    elif e.key == K_F12:
			for s in game.sprites[:]:
			    if s.type == 'goat':
				game.sprites.remove(s)
			game.time = 2 #just in case
		elif e.type is MOUSEMOTION:
		    player.dest.x,player.dest.y = player.cur.x+e.rel[0]*TW,player.cur.y+e.rel[1]*TH
		    item_angle(player)
		elif e.type is KEYUP:
		    if e.key == K_UP:
			player.keys[KUP] = 0
		    elif e.key == K_DOWN:
			player.keys[KDOWN] = 0
		    elif e.key == K_LEFT:
			player.keys[KLEFT] = 0
		    elif e.key == K_RIGHT:
			player.keys[KRIGHT] = 0
		    elif e.key == K_LCTRL:
			player.keys[KBUT] = 0
	    
	    player.px = -player.keys[KLEFT] + player.keys[KRIGHT]
	    player.py = -player.keys[KUP] + player.keys[KDOWN]
	    if player.px != 0 or player.py != 0:
		player.dest.x = player.cur.x + player.px * 16
		player.dest.y = player.cur.y + player.py * 16
		item_angle(player)
	    #sprites
	    for a in game.sprites:
		    a.prev.x = a.cur.x
		    a.prev.y = a.cur.y
		    a.update(a)
		    
	    #another frame
	    game.frames += 1

	    if int(game.total_dead*100/game.total_goats) > 25:
		message("Game Over","over 25% of your goats died!")
		return state_hs
	    
	    if game.frames%40 == 0:
		game.time -= 1

	    if game.time == 0:
		message("Game Over","You ran out of time!")
		return state_hs

	    if len(game.sprites) == 1: #Only the player
		p = game.time*10
		pygame.mixer.music.load("win.ogg")
		pygame.mixer.music.play()
		message("Good job!","Time Bonus: %d points" % p)
		game.score += p
		game.level += 1
		if game.level == 6: #they won!
		    message("You Won!")
		    return state_hs
		return state_level
	    

def state_intro():

    img = pygame.image.load("intro1.jpg")
    screen.blit(img,(0,0))
    pygame.display.flip()
    pygame.time.wait(800) #HACK: for fullscreen
    pygame.time.wait(800)

    img = pygame.image.load("intro2.jpg")
    game.sounds['infect'].play()
    screen.blit(img,(0,0))
    pygame.display.flip()
    pygame.time.wait(800)

    img = pygame.image.load("intro3.jpg")
    game.sounds['infect'].play()
    screen.blit(img,(0,0))
    pygame.display.flip()
    pygame.time.wait(800)

    img1 = pygame.image.load("intro4.jpg")
    img2 = pygame.image.load("intro5.jpg")
    game.sounds['bang'].play()
    for i in range(5):
       screen.blit(img1,(0,0))
       pygame.display.flip()
       pygame.time.wait(100)
       screen.blit(img2,(0,0))
       pygame.display.flip()
       pygame.time.wait(100)
        
    for e in pygame.event.get():
	pass
    
    return state_title

def state_title():
    pygame.mixer.music.load("turkey.ogg")
    pygame.mixer.music.play()

    bg = pygame.image.load("bg.jpg")
    img = pygame.image.load("title.png")

    pys = [227,295,360,426]
    px = 300
    pos = 0
    icon = game.images['goat.1']
    while 1:
        screen.blit(bg,(0,0))
        screen.blit(img,(0,0))
	py = pys[pos]
	screen.blit(icon,(px-icon.get_width(),py-icon.get_height()/2))
        pygame.display.flip()
        e = getch()
	if e.key == K_UP:
	    pos -= 1
	    game.sounds['bloop'].play()
	if e.key == K_DOWN:
	    pos += 1
	    game.sounds['bloop'].play()
	pos = (pos+4)%4
	if e.key == K_RETURN:
	    if pos == 0:
		return state_play
	    elif pos == 1:
		return state_hs
	    elif pos == 2:
		return state_help
	    elif pos == 3:
		return state_quit
	if e.key == K_ESCAPE:
	    return state_quit
	pygame.time.wait(1)

import pickle
def state_hs():
    try:
	hs = pickle.load(open("hs.sav","rb"))
    except:
	hs = [(100,'Cuzco'),(100,'Phil'),(100,'Nan'),(100,'Lyn'),(100,'Jet')]

    if not hasattr(game,'score'): game.score = 0
    sc = game.score
    game.score = 0
    uc = (sc,'_')
    hs.append(uc)
    hs.sort()
    hs.reverse()
    hs.pop()
    
    hs_show(hs,uc)
    
    if uc in hs:
	done = 0
	while not done:
	    e = getch()
	    if e.key == K_RETURN: done = 1
	    elif e.key == K_BACKSPACE:
		nc = (uc[0],uc[1][:-2]+"_")
		hs[hs.index(uc)]=nc
		uc = nc
	    else: 
		if len(uc[1]) < 15:
			nc = (uc[0],uc[1][:-1]+e.unicode+"_")
			hs[hs.index(uc)]=nc
			uc = nc
	    hs_show(hs,uc)
	nc = (uc[0],uc[1][:-1])
	hs[hs.index(uc)]=nc
	uc = nc
    else:
	getch()

    pickle.dump(hs,open("hs.sav","wb"))
    return state_title

def hs_show(hs,uc):
    img = pygame.image.load("bg.jpg")
    screen.blit(img,(0,0))
    img = pygame.image.load("hs.png")
    screen.blit(img,(0,0))

    pys = [138,204,270,337,404]
    px = 297 
    pxr = 618

    for i in range(0,5):
	v = hs[i]
	py = pys[i]+6
	s = v[1]
	img = fontmedium.render(s,1,(0,0,0)) 
        w,h = img.get_width(),img.get_height()
        screen.blit(img,(px+2,py+2))
        img = fontmedium.render(s,1,colororange)
	screen.blit(img,(px,py))

	s = str(v[0])
	img = fontmedium.render(s,1,(0,0,0)) 
        w,h = img.get_width(),img.get_height()
        screen.blit(img,(pxr-w+2,py+2))
        img = fontmedium.render(s,1,colororange)
	screen.blit(img,(pxr-w,py))
    
    if uc in hs:
	img = fontmedium.render("You got a high score!",1,coloryellow)
        screen.blit(img,(297,88))
	
    pygame.display.flip()
    
def state_help():
    img = pygame.image.load("bg.jpg")
    screen.blit(img,(0,0))
    img = pygame.image.load("help.png")
    screen.blit(img,(0,0))
    pygame.display.flip()
    getch()
    return state_title

def getch():
    while 1:
        for e in pygame.event.get():
	    if e.type is KEYDOWN:
	        return e
        pygame.time.wait(1)

def message(s,s2=""):
    render()
    
    img = fontlarge.render(s,1,(0,0,0)) 
    w,h = img.get_width(),img.get_height()
    screen.blit(img,((SW-w)/2+2,(SH-h)/2+2))
    img = fontlarge.render(s,1,colororange)
    screen.blit(img,((SW-w)/2,(SH-h)/2))

    y = (SH+h)/2
    
    img = fontmedium.render(s2,1,(0,0,0)) 
    w,h = img.get_width(),img.get_height()
    screen.blit(img,((SW-w)/2+2,y+2))
    img = fontmedium.render(s2,1,colororange)
    screen.blit(img,((SW-w)/2,y))
    
    pygame.display.flip()
    ok = 1
    while ok:
	e = getch()
	if e.key == K_RETURN: ok = 0
    update_all()
    render()


#import profile
#profile.run('run(STATE_PLAY)')

pygame.mouse.set_visible(0)
run(state_intro)
