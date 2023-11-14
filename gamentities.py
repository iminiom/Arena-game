iminiom
iminiom
En ligne

iminiom — 04/11/2023 20:05
but maybe ask @sKtch_axolotl cause it might make his code have less impact in like the movement but idk
sophia — 04/11/2023 20:15
omg yeah can i makw they bigger 😭
sKtch_axolotl — 04/11/2023 20:16
Ye you can 
iminiom — 04/11/2023 20:26
le main
import pygame as pg
import gamentities
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
Afficher plus
message.txt
6 Ko
j'ai pas changé le reste
fin je crois
sKtch_axolotl — 04/11/2023 20:26
je verrai bien
sKtch_axolotl — 05/11/2023 11:24
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
main.py
6 Ko
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
11 Ko
iminiom — 05/11/2023 11:24
thx
iminiom — 05/11/2023 14:30
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
message.txt
6 Ko
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
message.txt
12 Ko
là ca devrais marcher
iminiom — 06/11/2023 08:14
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
12 Ko
import 
hitboxes.py
1 Ko
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
mainV.py
6 Ko
{
    "hitboxes": 
    [
        [0,710,1280,10]
    ]
}
map.json
1 Ko
iminiom — 06/11/2023 08:28
class Hitbox:
    def init(self,x,y,w,h):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.width

    def go_to(self,x,y):

        self.xpos = x
        self.ypos = y
        self.bottom = y + self.height
        self.top = y
        self.left = x
        self.right = x + self.width


def is_colliding(hitbox1 : Hitbox,hitbox2 : Hitbox):
    """checks if it is colliding"""
    colliding = False

    if hitbox1.bottom <= hitbox2.bottom and hitbox1.bottom >= hitbox2.top:
        if hitbox2.right >= hitbox1.left and hitbox2.left <= hitbox1.left:
            colliding = True 
    elif hitbox1.right >= hitbox2.left and hitbox1.left <= hitbox2.left:
        colliding = True
    return colliding
def is_touching(h1 : Hitbox, h2: Hitbox):
    "Unlike is_colliding , here it's only if it's strictly the same values (== instead of <= / >=)"

    from_where = ''
    if h1.bottom == h2.top:
        from_where = 'down'
    elif h1.top == h2.bottom:
        from_where = 'up'
    elif h1.right == h2.left:
        from_where = 'right'
    elif h1.left == h2.right:
        from_where = 'left'
    return from_where 

h1 = Hitbox(0,0,10,10)
h2 = Hitbox(5,5,10,10)
h1.go_to(5,5)
sKtch_axolotl — 06/11/2023 08:38
iminiom — 06/11/2023 08:46
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
message.txt
6 Ko
iminiom — 06/11/2023 09:50
import os
path=r'\\0641-SRV-FILES\perso\ELEVES_LYC\T10\NEGRIE\Documents\T\nsi\projet\projet1 (1)\projet1'
os.chdir(path)

import pygame as pg
import gamentities
Afficher plus
message.txt
7 Ko
iminiom — 07/11/2023 18:52
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
16 Ko
class Hitbox:
    def __init__(self,x,y,w,h):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
Afficher plus
hitboxes.py
2 Ko
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
mainV.py
7 Ko
avec les assertions
sKtch_axolotl — 07/11/2023 20:58
@iminiom @sophia my latest (I'll add the assertions). Changes : on the hitbox I remade the conditions of colliding(it wasn't working properly), on GE I'm currently adding a cd to the player attack( with new hitboxes you're basically a bulldozer) & changing boss attack condition (it didn't work)
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
main.py
7 Ko
class Hitbox:
    def __init__(self,x,y,w,h):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
Afficher plus
hitboxes.py
2 Ko
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
12 Ko
main I added the boss wave 5
iminiom — 07/11/2023 21:00
Ok Check the assertions on the other ones too then cause it’ll prob change
sKtch_axolotl — 07/11/2023 21:00
ok
sophia — 07/11/2023 21:34
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
16 Ko
Ok changed a tiny bit but otherise all good
sKtch_axolotl — 07/11/2023 21:37
ok
what you mean it has changed 'A tiny bit'? and why does the bossnmy has been replaced by the code of the player ?
sophia — 07/11/2023 21:40
I added assertations and added documentation
sKtch_axolotl — 07/11/2023 21:41
i saw
but why did the boss got replaced by the code of the player ?
sophia — 07/11/2023 21:54
in my updated? uhh i have no idea 
i’ll fix
sophia — 07/11/2023 22:37
OKK can i copy paste all the code pls
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
message.txt
15 Ko
ok this hsould be goof
my entire code glitched b4
sKtch_axolotl — 07/11/2023 23:10
@everyone can yall send your latest files so I can add everything tmrw morning
iminiom — 08/11/2023 06:02
Did that already
sKtch_axolotl — 09/11/2023 13:54
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
main.py
6 Ko
class Hitbox:
    def __init__(self,x,y,w,h):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.width

    def go_to(self,x,y):
        
        self.xpos = x
        self.ypos = y
        self.bottom = y + self.height
        self.top = y
        self.left = x
        self.right = x + self.width
    
    
def is_colliding(hitbox1 : Hitbox,hitbox2 : Hitbox):
    """checks if it is colliding"""
    colliding = False
    
    if ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)) and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        colliding = True
    return colliding

def is_touching(h1 : Hitbox, h2: Hitbox):
    "Unlike is_colliding , here it's only if it's strictly the same values (== instead of <= / >=)"
    
    from_where = ''
    if h1.bottom == h2.top:
        from_where = 'down'
    elif h1.top == h2.bottom:
        from_where = 'up'
    elif h1.right == h2.left:
        from_where = 'right'
    elif h1.left == h2.right:
        from_where = 'left'
        
    return from_where 

h1 = Hitbox(0,0,10,10)
h2 = Hitbox(5,5,10,10)
h1.go_to(5,5)
Réduire
hitboxes.py
2 Ko
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]
Afficher plus
gamentities.py
13 Ko
sKtch_axolotl — 11/11/2023 19:48
added working attack, display of current wave n fixed Freezenmy's hitbox & code so it's not half in the ground
import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
Afficher plus
main.py
7 Ko
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]

ground = hitboxes.Hitbox(groundhitboxes[0][0],groundhitboxes[0][1],groundhitboxes[0][2],groundhitboxes[0][3])


width = 1280
height = 720
screen = pg.display.set_mode((width,height),vsync=0)
clock = pg.time.Clock()

class GameEntity:
    """ An Entity of the game, the larger cal"""
    def __init__(self,hp,dmg_dealt,x,y,w,h):
        self.hp = hp
        self.dmg_dealt = dmg_dealt
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.width,self.height)
        
    def gravity(self,strength):
        assert strength > 0, "Gravity strength must be positive"
        if self.ypos <= 709 - self.height:
            self.ypos += strength
        
class Attack(hitboxes.Hitbox):
    def __init__(self,x,y,w,h,cooldown,dmg,xoffset,yoffset):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.timer =  cooldown
        self.cd = cooldown
        self.dmg_dealt = dmg
        self.enemies_hit = []
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.width
        self.xoffset = xoffset#permet de décaler l'attaque en x par rapport à son éméteur (sinon self.hitbox = éméteur.hitbox)
        self.yoffset = yoffset#same en y

    def update(self,enemies_list = list):
        
        if self.timer > 0:
            self.timer -= 1
        for e in enemies_list:
            if hitboxes.is_colliding(self,e.hitbox) and e not in self.enemies_hit:
                e.hp -= self.dmg_dealt
                self.enemies_hit.append(e)
        print(self.timer)

    def follow(self,x,y):
        self.go_to(x+self.xoffset,y+self.yoffset)


class Player(GameEntity):

    """
        A game entity that is controlled by the user

        entity in the game world:
            hp : hit points (health) of the entity
            dmg_dealt:  amount of damage the entity can deal
            xpos :  x-coordinate of the entity's position
            ypos :  y-coordinate of the entity's position
            width: width of the entity
            height :height of the entity
            hitbox: object representing the collision hitbox for the entity
        """

    """A game entity that is controlled by the player"""
    def __init__(self,hp,dmg_dealt,x,y,w,h,col,attack_cd):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        assert attack_cd >= 0, "Attack cooldown must not be < to 0"
        self.col = col
        self.w = w
        self.h = h
        self.cd = attack_cd
        self.timer = attack_cd
        self.c = 0
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.w,self.h)
        self.jumpstr = 50
        self.dmg = dmg_dealt #damage given
        self.facing = 'right' #where the player is facing
        self.is_attacking = False
        self.sword = Attack(0,0,0,0,20,1,0,0)
        

        assert isinstance(hp, int), "hp should be an integer"
        assert isinstance(dmg_dealt, int), "dmg_dealt should be an integer"
        assert isinstance(x, int), "xpos should be an integer"

    
... (276 lignes restantes)
Réduire
gamentities.py
14 Ko
@everyone
sKtch_axolotl — 12/11/2023 14:51
import pygame as pg
import gamentities
import hitboxes
import json
import time
from random import randint as rd
Afficher plus
main.py
7 Ko
added scream at death (+1 sec delay between death and leaving)
sophia — 12/11/2023 14:57
Like a sound?
sKtch_axolotl — 12/11/2023 14:57
ye
the one i sent sooner
﻿
import pygame as pg
import hitboxes
import json
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]

ground = hitboxes.Hitbox(groundhitboxes[0][0],groundhitboxes[0][1],groundhitboxes[0][2],groundhitboxes[0][3])


width = 1280
height = 720
screen = pg.display.set_mode((width,height),vsync=0)
clock = pg.time.Clock()

class GameEntity:
    """ An Entity of the game, the larger cal"""
    def __init__(self,hp,dmg_dealt,x,y,w,h):
        self.hp = hp
        self.dmg_dealt = dmg_dealt
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.width,self.height)
        
    def gravity(self,strength):
        assert strength > 0, "Gravity strength must be positive"
        if self.ypos <= 709 - self.height:
            self.ypos += strength
        
class Attack(hitboxes.Hitbox):
    def __init__(self,x,y,w,h,cooldown,dmg,xoffset,yoffset):
        self.xpos = x
        self.ypos = y
        self.width = w
        self.height = h
        self.timer =  cooldown
        self.cd = cooldown
        self.dmg_dealt = dmg
        self.enemies_hit = []
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.width
        self.xoffset = xoffset#permet de décaler l'attaque en x par rapport à son éméteur (sinon self.hitbox = éméteur.hitbox)
        self.yoffset = yoffset#same en y

    def update(self,enemies_list = list):
        
        if self.timer > 0:
            self.timer -= 1
        for e in enemies_list:
            if hitboxes.is_colliding(self,e.hitbox) and e not in self.enemies_hit:
                e.hp -= self.dmg_dealt
                self.enemies_hit.append(e)
        print(self.timer)

    def follow(self,x,y):
        self.go_to(x+self.xoffset,y+self.yoffset)


class Player(GameEntity):

    """
        A game entity that is controlled by the user

        entity in the game world:
            hp : hit points (health) of the entity
            dmg_dealt:  amount of damage the entity can deal
            xpos :  x-coordinate of the entity's position
            ypos :  y-coordinate of the entity's position
            width: width of the entity
            height :height of the entity
            hitbox: object representing the collision hitbox for the entity
        """

    """A game entity that is controlled by the player"""
    def __init__(self,hp,dmg_dealt,x,y,w,h,col,attack_cd):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        assert attack_cd >= 0, "Attack cooldown must not be < to 0"
        self.col = col
        self.w = w
        self.h = h
        self.cd = attack_cd
        self.timer = attack_cd
        self.c = 0
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.w,self.h)
        self.jumpstr = 50
        self.dmg = dmg_dealt #damage given
        self.facing = 'right' #where the player is facing
        self.is_attacking = False
        self.sword = Attack(0,0,0,0,20,1,0,0)
        

        assert isinstance(hp, int), "hp should be an integer"
        assert isinstance(dmg_dealt, int), "dmg_dealt should be an integer"
        assert isinstance(x, int), "xpos should be an integer"

    
    def move(self):
        """Moving the player on the screen using zqsd"""
        
        keys = pg.key.get_pressed()
        self.hitbox.go_to(self.xpos,self.ypos) #moves the hitbox of the player with him (to the coordonates of the player)
        if keys[pg.K_d] and self.xpos <1280-self.w : #moves towards the right when press d
            self.xpos += 5
            self.facing = 'right'
            self.hitbox.go_to(self.xpos,self.ypos)

            
        elif keys[pg.K_q] and self.xpos >0:   #moves towards the left when press q
            self.xpos -= 5
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'left'

        
                    
        if keys[pg.K_LSHIFT] and keys[pg.K_d] and self.xpos <1280-self.w : #makes you run towards the right when you press left shift and d
            self.xpos += 10
            self.hitbox.go_to(self.xpos,self.ypos)


            assert self.hitbox.xpos == self.xpos
            assert self.hitbox.ypos == self.ypos

        if keys[pg.K_LSHIFT] and keys[pg.K_q] and self.xpos >0 :#makes you run towards the left when you press left shift and q
            self.xpos -= 10
            self.hitbox.go_to(self.xpos,self.ypos)
                
    def jump(self):
        """gives entity capability of jumping with space key
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] and self.ypos > 1 and hitboxes.is_touching(self.hitbox,ground):
            #if self.c == 0 or self.c > 50:
            print("sapcebar")
            self.ypos -= self.jumpstr
            print("jumped")  
        
            if self.c == 0: 
                self.c = 60
        
        if self.c > 0:
           self.c -= 1 
    def attack(self,enemies_list):
        """
        Makes the player attack when press up down left and right
        """
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] and not self.is_attacking:
            self.sword = Attack(self.xpos,self.ypos,self.width,self.h,self.cd,self.dmg_dealt,self.w,0)
            self.is_attacking = True
            print(self.sword.timer)
            if self.sword.timer <= 1:
                self.is_attacking = False
        if keys[pg.K_LEFT] and not self.is_attacking:
            self.sword = Attack(self.xpos,self.ypos,self.w,self.h,self.cd,self.dmg_dealt,-self.w,0)
            self.is_attacking = True
            if self.sword.timer <= 1:
                self.is_attacking = False
        if keys[pg.K_UP] and not self.is_attacking:
            self.sword = Attack(self.xpos,self.ypos,self.w,self.h,self.cd,self.dmg_dealt,0,-self.h)
            self.is_attacking = True
            if self.sword.timer <= 1:
                self.is_attacking = False
        if keys[pg.K_DOWN] and not self.is_attacking:
            self.sword = Attack(self.xpos,self.ypos,self.w,self.h,self.cd,self.dmg_dealt,0,self.h)
        if self.is_attacking:
            self.sword.update(enemies_list)
            self.sword.follow(self.xpos,self.ypos)
            if self.sword.timer <= 0:
                self.is_attacking = False
                self.sword.timer = self.sword.cd
                self.sword = Attack(0,0,0,0,0,0,0,0)
                
        print(self.is_attacking)

        
                
                    
                    
            


class Enemy(GameEntity):
    """
    the general code for enemies
    """
    def __init__(self, hp,dmg_dealt,x,y,w,h):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.width = w
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.width,self.height)
        
class WalkingNmy(Enemy):
    """
    enemies that can walk. 
    """
    def __init__(self, hp, dmg_dealt, x,y,w,h):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.facing = 'left'

    def move(self,play):
        """
        a method that manage the walking part of the enemy
        the enemy walks and speeds up when near you
        takes a parameter:
        play, it is the player and is used for it's coordinates
        """
        assert type(play) == Player
        if self.xpos - play.xpos > play.w: # runs towards you if is on your right
            self.xpos -= 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'right'
        elif self.xpos - play.xpos < play.w-2*self.width: # runs towards you if is on your left
            self.xpos += 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'left'
        
    def attack(self,play):
        """
        a method that manage the attack part of the enemy
        takes a parameter:
        play, it is the the player and is used for it's coordinates and hp
        """
        assert type(play) == Player
        if self.xpos == play.xpos - play.w or self.xpos == play.xpos + play.w:        # if touches you
            play.hp -= 1          # gives you damage
            self.xpos -=20  #goes back a little so it won't kill you
            self.hitbox.go_to(self.xpos,self.ypos)
        
class FlyingNmy(Enemy):
    """
    enemies that flys. 
    """
    def __init__(self, hp, dmg_dealt, x,y,w,h):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.facing = 'left'

    def move(self,play):
        """
        a method that manage the flaing and moving part of the enemy
        the enemy flys and speeds up when near you
        those enemies are not affected by gravity
        takes a parameter:
        play, it is the player and is used 
        for it's coordinates
        """
        assert type(play) == Player
        self.ypos -= 3      # annule l'effet de la gravitÃ©
        if self.xpos - play.xpos > play.w:         # runs towards you if is on your right
            self.xpos -= 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'left'
        elif self.xpos - play.xpos < play.w-2*self.width:        # runs towards you if is on your left
            self.xpos += 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'right'
        if self.ypos < play.ypos:
            self.ypos += 2
            self.hitbox.go_to(self.xpos,self.ypos)
        elif self.ypos >= play.ypos:
            self.ypos -= 10
            
            
            
    def attack(self,play):
        """
        a method that manage the attack part of the enemy
        takes a parameter:
        play, it is the the player and is used for it's coordinates and hp
        """
        if self.xpos == play.xpos - play.w or self.xpos == play.xpos + play.w:              # if touches you
            play.hp -= 1                         # gives you damage
            self.xpos -=20.     #goes back a little so it won't kill you
            self.hitbox.go_to(self.xpos,self.ypos)
            
       
class FreezeNmy(Enemy):
    """
    an enemy that freezes the player when it touches it. When it touches the player, the player changes color
    One it touched the player it dies
    """
    def __init__(self, hp, dmg_dealt, x,y,w,h,play):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.facing = 'left'

    def move(self,play):
        """
        a method that manage the moving part of the enemy
        takes a parameter:
        play, it is the player and is used for it's coordinates
        """
        assert type(play) == Player
        if self.xpos < 0 and self.xpos - play.xpos > play.w:
            self.xpos -=2

            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'left'

        elif self.xpos < 1180 and self.xpos - play.xpos < play.w:
            self.xpos +=2

            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'right'

        
        self.hitbox.go_to(self.xpos,self.ypos)

    def freeze(self,play):
        """
        a methode that makes the player freeze and change color when it touches the enemy and the enemy then dies
        it takes a parametre
        play, the player is used for it's coordiantes and hp
        """
        assert type(play)== Player
        if self.xpos == play.xpos-play.w and self.ypos == play.ypos+play.h: #if it touches you
            self.hp = 0
            c = 180
            
            while c !=  0:
                c -=1

            
        
        



class BossNmy(Enemy):
    """
    a boss enemy that can one shot you, can walk and teleport.
    """
    def __init__(self,hp, dmg_dealt, x,y,w,h,play):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.w = 2*play.w
        self.facing = 'left'

    def move(self,play):
        """
        a method that manage the flying and moving part of the enemy
        the enemy walk and speeds up when near you
        takes a parameter:
        play, it is the player and is used for it's coordinates
        """
        assert type(play) == Player
        
        if self.xpos - play.xpos > play.w:         # runs towards you if is on your right
            self.xpos -= 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'left'
        elif self.xpos - play.xpos < play.w-2*self.width:        # runs towards you if is on your left
            self.xpos += 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'right'
    def attack(self,play):
        """
        a method that manages the attacks. This enemy can one shot the player
        it takes a parameter:
        play, the player, it is used for it's coordinates and hp.
        """
        
        if hitboxes.is_touching(self.hitbox,play.hitbox) == 'up' or hitboxes.is_touching(self.hitbox,play.hitbox) == 'left' or hitboxes.is_touching(self.hitbox,play.hitbox) == 'right' or hitboxes.is_colliding(self.hitbox,play.hitbox):    #if it touches you, it gives you damage
            play.hp = 0
            print('Aouch')


player = Player(20,1,25,700,10,10,(255,0,0),50)
enemy1 = Enemy(1,1,700,700,10,10)
entitieslist = [player, enemy1]
