import pygame as pg
import gamentities
import hitboxes
import json
from random import randint as rd
with open("map.json") as json_file:
    file = dict(json.load(json_file))
    groundhitboxes = file["hitboxes"]

pg.init()

width = 1280
height = 720
screen = pg.display.set_mode((width,height),vsync=0)
clock = pg.time.Clock()


#==============================================ENTITIES======================================================

player = gamentities.Player(20,1,50,600,20,30,(255,0,0),200)
enemy1 = gamentities.WalkingNmy(2,1,800,600,35,45)      
enemy2 = gamentities.FlyingNmy(1,1,666,50,25,25)
enemy3 = gamentities.FreezeNmy(1,5,rd(600,1200),650,50,50,player)
enemies_list = []
#enemies_list.append(enemy1)
#enemies_list.append(enemy2)
ground = hitboxes.Hitbox(groundhitboxes[0][0],groundhitboxes[0][1],groundhitboxes[0][2],groundhitboxes[0][3])

def show_player_life(life):
    font = pg.font.Font(None, 36)
    texte_life = font.render(f'Player lifes : {life}', True, (255, 255, 255))
    screen.blit(texte_life, (10, 10))
#===============================================IMAGES=======================================================

main_char = pg.image.load("mc.png")
mc_left = pg.transform.flip(main_char,True,False)
walking_nmy = pg.image.load("zombie.png")
walking_nmy_right = pg.transform.flip(walking_nmy,True,False)
flying_nmy = pg.image.load("flying.png")
flying_nmy_right = pg.transform.flip(flying_nmy,True,False)
elsa = pg.image.load("letitgo.png")
 

#=======================================CE QUI FAIT TOURNER LE JEU===========================================
def waves(wave_num):
    enemy_num = wave_num ** 2
    for _ in range(enemy_num):
        enemy_type = rd(1,3)
        enemies_list.append(
            {
                1: gamentities.WalkingNmy(5,1,rd(250,1200),650,35,45),
                2: gamentities.FlyingNmy(1,1,rd(0,1200),50,25,25),
                3: gamentities.FreezeNmy(1,5,rd(600,1200),650,50,50,player)

            }[enemy_type]
        )

def run_game():
    
    running = True
    wave_num = 0
    while running:
        clock.tick(60)
        pg.time.delay(50)
        for event in pg.event.get():
            if event.type == pg.QUIT or player.hp <= 0:
                running = False
                pg.quit()
        bg = pg.image.load("background.jpg")
        screen.blit(bg,(0,0))

        player.move()
        if len(enemies_list) <= 0:
            wave_num += 1
            print("on viens de poasser a la wave ", wave_num)
            waves(wave_num)

            
        
        for e in enemies_list:
            if hitboxes.is_touching(player.hitbox, e.hitbox) == 'left':
                player.xpos -= 20
        for e in enemies_list:    
            if hitboxes.is_touching(player.hitbox, e.hitbox) == 'right':
                player.xpos += 20
        if not hitboxes.is_touching(player.hitbox,ground) or not hitboxes.is_colliding(player.hitbox,ground):
            player.gravity(5)
        
        for e in enemies_list:
            if e.hp > 0:
                e.move(player)
                if type(e) != gamentities.FreezeNmy:
                    e.attack(player)
                else:
                    if e.xpos == player.xpos and e.ypos == player.ypos:
                        e.freeze(player)
                        print('i froze the player')
                    
            else:
                if len(enemies_list) > 0:
                    #deleted_enemy = e
                    enemies_list.remove(e)
                    
        
        player.attack(enemies_list)

        for e in enemies_list:
            if not hitboxes.is_colliding(e.hitbox,ground) or not hitboxes.is_touching(e.hitbox,ground):
                e.gravity(5)
        
        if player.is_facing == 'right':
            screen.blit(main_char,(player.xpos-25,player.ypos-40))
        elif player.is_facing == 'left':
            screen.blit(mc_left,(player.xpos-25,player.ypos-40))

        show_player_life(player.hp)

        pg.draw.rect(screen,(255,0,0),(player.hitbox.xpos,player.hitbox.ypos,player.hitbox.width,player.hitbox.height))
               
        for e in enemies_list:
            if e.hp > 0:
                pg.draw.rect(screen,(0,255,0),(e.hitbox.xpos,e.hitbox.ypos,e.hitbox.width,e.hitbox.height)) #devtool, showing enemies hitboxes
                if e.facing == 'left':
                    if type(e) == gamentities.WalkingNmy :
                        screen.blit(walking_nmy,(e.xpos-20,e.ypos-25))
                    elif type(e) == gamentities.FlyingNmy:
                        screen.blit(flying_nmy,(e.xpos-20,e.ypos-35))
                    elif type(e) == gamentities.FreezeNmy:
                        screen.blit(elsa,(e.xpos,e.ypos))
                    
                elif e.facing == 'right':
                    if type(e) == gamentities.WalkingNmy:
                        screen.blit(walking_nmy_right,(enemy1.xpos-20,enemy1.ypos-25))
                    if type(e) == gamentities.FlyingNmy:
                        screen.blit(flying_nmy_right,(e.xpos-20,e.ypos-35))
        
        

        pg.draw.rect(screen,(252,255,0),(player.atkhitbox.xpos,player.atkhitbox.ypos,player.atkhitbox.width,player.atkhitbox.height))
        
        
        
        
        
        pg.display.update()
        

pg.mixer.music.load("dumbsong.mp3")
pg.mixer.music.play(loops=-1)
run_game()