import sys
import random
import pygame
pygame.init()

#class import
from hrac import Hrac
from enemy import Enemy

#rozliseni
rozliseni_x = 800
rozliseni_y = 600

#hrac
pozice_hrace_x = (rozliseni_x / 2) - 15
pozice_hrace_y = (rozliseni_y / 2) - 15

player_idle = pygame.image.load("player idle.png")
player_moving = pygame.image.load("player moving.png")

cooldown = 15

#enemak
pozice_enemy_x = (rozliseni_x / 2) - 23
pozice_enemy_y = (rozliseni_y / 4) - 23

enemy_idle = pygame.image.load("Enemy_1_idle.png")

#fps
fps_casovac = pygame.time.Clock()
fps = 60

#barvicky
cerna = (30, 30, 30)
cervena = (255, 0, 0)

#okno
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

#strely
strely_1 = []
strely_2 = []

#aktivace class
hrac = Hrac(pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown)
enemy = Enemy(pozice_enemy_x, pozice_enemy_y, rozliseni_x, rozliseni_y, okno, enemy_idle)

#game loop
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps_casovac.tick(fps)

    okno.fill(cerna)

    #sniz cooldowj
    hrac.sniz_cooldown()

    #vykresleni hrace
    hrac.pohni_se()

    #strely
    strela_1 = hrac.vystrel_1()
    if strela_1 != None:
        strely_1.append(strela_1)

    strela_2 = hrac.vystrel_2()
    if strela_2 != None:
        strely_2.append(strela_2)

    #vykresleni strel
    for strela_1 in strely_1:
        if strela_1 != None:
            strela_1[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_1)

    for strela_2 in strely_2:
        if strela_2 != None:
            strela_2[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_2)

    #vykresleni enemy
    enemy.vykresli_se()

    pygame.display.flip()