import pygame
from pygame.locals import *

pygame.init()
#pygame.display.init()
#pygame.font.init()
#pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption("Goat Bloat")

SW,SH = 640,480
screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
TW,TH = 16,16
VW,VH = SW,SH-TH*2
W,H = VW/TW,VH/TH
AX,AY = 0,TH

class tile:
    pass

class sprite:
    def toimage(self,iname):
	self.iname = iname
	self.image = game.images[iname]

class _game:
	pass

game = _game()

game.images = {}

img = pygame.image.load("player.png").convert_alpha()
x = 0
for i in ('1','2','3','4','5','6','7','8'):
	game.images['player.%s'%i] = img.subsurface((x*32,0,32,32))
	x+=1
img = pygame.image.load("goat.png").convert_alpha()
x = 0
for i in ('1','2','3','4','5','6','7','8'):
	game.images['goat.%s'%i] = img.subsurface((x*48,0,48,32))
	x+=1

game.sounds={}
game.sounds['bah'] = pygame.mixer.Sound('bah.wav')
game.sounds['bang'] = pygame.mixer.Sound('bang.wav')
game.sounds['bloop'] = pygame.mixer.Sound('bloop.wav')
game.sounds['hey'] = pygame.mixer.Sound('infect.wav')
game.sounds['infect'] = pygame.mixer.Sound('infect.wav')

game.tiles=[None for n in range(0,64)]
game.sprites=[]

grass = pygame.image.load("grass16.png").convert()

fontsmall = pygame.font.Font("mailrays.ttf",15)
fontmedium = pygame.font.Font("mailrays.ttf",35)
#font72 = pygame.font.Font("mailrays.ttf",72)
fontlarge = pygame.font.Font("mailrays.ttf",135)

colororange = (255,165,0)
coloryellow = (255,250,0)

def tiles_load(fname):
    img = pygame.image.load(fname).convert_alpha()
    n = 0
    for y in range(0,8):
        for x in range(0,8):
		t = tile()
        	t.image = img.subsurface((x*TW,y*TH,TW,TH))
        	game.tiles[n] = t
        	n+=1

tiles_load('tiles.png')

game.map = [[0 for x in range(0,W)] for y in range(0,H)]
game.updates = []

def update_all():
	for y in range(0,H):
		for x in range(0,W):
			game.updates.append((x,y))
update_all()
#game.solid = [[0 for x in range(0,W)] for y in range(0,H)]

def load(fname):
    f = open(fname,"r")
    for y in range(0,H):
	vs = f.readline().split()
	for x in range (0,W):
	    game.map[y][x] = int(vs[x])
    f.close()

def save(fname):
    f = open(fname,"w")
    for y in range(0,H):
	vs = [str(game.map[y][x]) for x in range(0,W)]
	f.write(" ".join(vs)+"\n")
    f.close()
    
import random

sarcasm = [
"Don't let those goats get away!",
"Have you ever seen a bloated goat afloat in a boat?",
"Buy a goat today!",
"Ruminants are fun!",
"Watch out for exploding goats!",
]
sarcasm_x = 0
sarcasm_image = None
sarcasm_text = ""

def render():
    updates = []
    gw,gh = grass.get_width()/TW,grass.get_height()/TH
    for u in game.updates:
	    x,y = u
	    if x>=0 and x<W and y>=0 and y<H:
		n = game.map[y][x]
        	t = game.tiles[n]
        	screen.blit(grass.subsurface((x%gw*TW,y%gh*TH,TW,TH)),(x*TW+AX,y*TH+AY))
		screen.blit(t.image,(x*TW+AX,y*TH+AY))
		updates.append(Rect(x*TW+AX,y*TH+AY,TW,TH))
    game.updates = []
    for s in game.sprites:
	    img = s.image
	    if hasattr(s,'angle'):
		    angle = int(s.angle*360/(2*3.14159))/10*10
		    iname = '%s-%d'%(s.iname,angle)
		    if iname in game.images: img = game.images[iname]
		    else:
        		    img = pygame.transform.rotate(img,angle)
			    #print iname
			    game.images[iname] = img
            w,h = img.get_width(),img.get_height()
	    x = s.cur.centerx - w/2
	    y = s.cur.centery - h/2
	    r = Rect((x,y,w,h))
	    screen.blit(img,(x+AX,y+AY))
	    updates.append(Rect(x+AX,y+AY,w,h))
	    yy = y/TH
	    while yy < r.bottom/TH+1:
		xx = x/TW
		while xx < r.right/TW+1:
		    game.updates.append((xx,yy))
		    xx += 1
		yy += 1
   
    #display scoares, etc
    screen.fill((0,0,0),Rect(0,0,SW,TH))
    if hasattr(game,'score'):
	img = fontsmall.render("Score: %d   Time Left: %d   Vaccinated: %2d%%"%(game.score,game.time,int(game.total_saved*100/game.total_goats)),1,coloryellow,(0,0,0))
	screen.blit(img,(0,0))
    updates.append(Rect(0,0,SW,TH))
   
    #display sarcasm
    global sarcasm_image, sarcasm_x, sarcasm_text
    if sarcasm_image == None or -sarcasm_image.get_width() > sarcasm_x:
	sarcasm_text = random.choice(sarcasm)
	sarcasm_image = fontsmall.render(sarcasm_text,1,coloryellow,(0,0,0))
	sarcasm_x = SW
    screen.fill((0,0,0),Rect(0,SH-TH,SW,TH))
    screen.blit(sarcasm_image,(sarcasm_x,SH-TH))
    updates.append(Rect(0,SH-TH,SW,TH))
    sarcasm_x -= 4
    #print sarcasm_x,sarcasm_text
    
    #pygame.display.flip()
    pygame.display.update(updates)
