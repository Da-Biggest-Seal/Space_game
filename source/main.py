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

#okno
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

#hrac
pozice_hrace_x = (rozliseni_x / 2) - 15
pozice_hrace_y = (rozliseni_y / 2) - 15

player_idle = pygame.image.load("player idle.png")
player_moving = pygame.image.load("player moving.png")

cooldown = 15

#enemak
enemy_idle = pygame.image.load("Enemy_1_idle.png")
enemy_1 = []

enemy_1_x = []
enemy_1_y = []

pocet_LVL_1 = random.randint(4, 8)

for i in range(pocet_LVL_1):
    pozice_enemy_x = random.randint(0, int(rozliseni_x - 47))
    pozice_enemy_y = random.randint(0, int((rozliseni_y / 4) - 47))

    enemy_1_x.append(pozice_enemy_x)
    enemy_1_y.append(pozice_enemy_y)

    print(f"x = {pozice_enemy_x}")
    print(f"y = {pozice_enemy_y}")

#fps
fps_casovac = pygame.time.Clock()
fps = 60

#barvicky
cerna = (30, 30, 30)
cervena = (255, 0, 0)

#strely
strely_1 = []
strely_2 = []

#aktivace class
hrac = Hrac(pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown)
enemy = Enemy(enemy_1_x, enemy_1_y, rozliseni_x, rozliseni_y, okno, enemy_idle, pocet_LVL_1)

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

    #sestreleni enemaka
    for strela_1 in strely_1[:]:
        if enemy.checkni_kolizi_1(strela_1) == True:
            if strela_1 in strely_1:
                strely_1.remove(strela_1)

    for strela_2 in strely_2[:]:
        if enemy.checkni_kolizi_2(strela_2) == True:
            if strela_2 in strely_2:
                strely_2.remove(strela_2)

    pygame.display.flip()