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
        
        if self.ypos <= 709 - self.height:
            self.ypos += strength
        

class Player(GameEntity):
    """
    A game entity that is controlled by the user
    """


    def __init__(self,hp,dmg_dealt,x,y,w,h,col,attack_cd):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.col = col
        self.w = w
        self.h = h
        self.cd = attack_cd     
        self.timer = attack_cd
        self.c = 0      
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.w,self.h)
        self.jumpstr = 80
        self.dmg = dmg_dealt    #damage given 
        self.atkhitbox = hitboxes.Hitbox(self.xpos-self.w,self.ypos,10,10)
        self.is_facing = 'right'    #where the player is facing 
    
    def move(self):
        """
        Moving the player on the screen using qd and run when press left shift
        """ 
        keys = pg.key.get_pressed()
        self.hitbox.go_to(self.xpos,self.ypos)      #moves the hitbox of the player with him (to the coordonates of the player)
        if keys[pg.K_d] and self.xpos <1280-self.w :        #moves towards the right when press d 
            self.xpos += 5
            self.is_facing = 'right'
            self.hitbox.go_to(self.xpos,self.ypos)
        elif keys[pg.K_q] and self.xpos >0:               #moves towards the left when press q 
            self.xpos -= 5
            self.hitbox.go_to(self.xpos,self.ypos)
            self.is_facing = 'left'
        if hitboxes.is_touching(self.hitbox,ground):
            is_touching_grass = True                #if touches the ground the true  
        else:
            is_touching_grass = False

        if keys[pg.K_LSHIFT] and keys[pg.K_d] and self.xpos <1280-self.w :      #makes you run towards the right when you press left shift and d 
            self.xpos += 10
            self.hitbox.go_to(self.xpos,self.ypos)
        if keys[pg.K_LSHIFT] and keys[pg.K_q] and self.xpos >0 :        #makes you run towards the left when you press left shift and q
            self.xpos -= 10
            self.hitbox.go_to(self.xpos,self.ypos)
            
        if keys[pg.K_SPACE] and self.ypos > 1 and is_touching_grass:
            #if self.c == 0 or self.c > 50:
            self.ypos -= self.jumpstr
            if self.c == 0: 
                self.c = 60
        
        if self.c > 0:
           self.c -= 1 

        
                
    def attack(self,enemies_list):
        """
        Makes the player attack when press up down left and right
        """
        keys = pg.key.get_pressed()
        
        self.timer -= 1             #a count down to not spam kill
        if self.timer == 0:             
            self.timer = self.cd

        for e in enemies_list:    
            if keys[pg.K_UP]:
                self.atkhitbox = hitboxes.Hitbox(self.xpos, self.ypos - self.h,self.h,self.w)
                self.atkhitbox.go_to(self.xpos,self.ypos-self.h)
            elif keys[pg.K_RIGHT]:
                    self.atkhitbox = hitboxes.Hitbox(self.xpos+self.w,self.ypos,self.w,self.height)
                    self.atkhitbox.go_to(self.xpos+self.w,self.ypos)
            elif keys[pg.K_LEFT]:
                self.atkhitbox = hitboxes.Hitbox(self.xpos -self.w, self.ypos,self.w,self.h)
                self.atkhitbox.go_to(self.xpos-self.w,self.ypos)
            elif keys[pg.K_DOWN]:
                self.atkhitbox = hitboxes.Hitbox(self.xpos,self.ypos+self.h,self.w,self.h)
            else:
                self.atkhitbox = hitboxes.Hitbox(0,0,0,0)
            if hitboxes.is_colliding(self.atkhitbox,e.hitbox):
                print("attacked")
                e.hp -= self.dmg
                e.xpos += 50
                e.ypos -= 50
                pg.draw.rect(screen,(125,20,20),(self.xpos+self.w,self.ypos,10,10))
            
                    
                    
            


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
        self.is_facing = 'left'

    def move(self,play):
        """
        a method that manage the walking part of the enemy
        the enemy walks towards you
        takes a parameter:
        play, it is the player and is used for it's coordinates
        """
        assert type(play) == Player

        if self.xpos - play.xpos > play.w:         # runs towards you if is on your right
            self.xpos -= 2
            
            self.hitbox.go_to(self.xpos,self.ypos)
            self.facing = 'right'

        elif self.xpos - play.xpos < play.w-2*self.width:        # runs towards you if is on your left
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
            self.xpos -= 20  #goes back a little so it won't kill you
            self.hitbox.go_to(self.xpos,self.ypos)
        
class FlyingNmy(Enemy):
    """
    enemies that flys
    """

    def __init__(self, hp, dmg_dealt, x,y,w,h):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.facing = 'left'

    def move(self,play):
        """
        a method that manage the flying and moving part of the enemy
        the enemy flys towards you
        these enemies are not affected by gravity
        takes a parameter:
        play, it is the player taht is used 
        for it's coordinates
        """
        assert type(play) == Player
        self.ypos -= 3      # annule l'effet de la gravité
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
    an enemy that freezes the player when it touches it.
    When it touched the player it dies
    """
    def __init__(self, hp, dmg_dealt, x,y,w,h,play):
        super().__init__(hp,dmg_dealt,x,y,w,h)
        self.facing = ''

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

        if self.ypos < play.ypos:
            self.ypos += 2

            self.hitbox.go_to(self.xpos,self.ypos)

        elif self.ypos > 620 and  self.ypos >= play.ypos:
            self.ypos -= 10


        #self.xpos += 1 
        self.hitbox.go_to(self.xpos,self.ypos) 
        #self.hp = 0

    def freeze(self,play):
        """
        a methode that makes the player freeze and change color when it touches the enemy and the enemy then dies
        it takes a parametre
        play, the player is used for it's coordiantes and hp
        """
        assert type(play)== Player
        if self.xpos == play.xpos-play.w and self.ypos == play.ypos+play.h: #if it touches you
            self.hp = 0             #it dies
            c = 180             #the counter goes to 180 and freezes you until i equals 0
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
        
        if self.xpos == play.xpos-play.w and self.ypos == play.ypos+play.h:    #if it touches you, you die 
            play.hp = 0


player = Player(20,1,25,700,10,10,(255,0,0),50)
enemy1 = Enemy(1,1,700,700,10,10)
entitieslist = [player, enemy1]
