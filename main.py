import sys
import random
import pygame
pygame.init()

from hrac import Hrac
from enemy import Enemy

rozliseni_x = 800
rozliseni_y = 600

pozice_hrace_x = (rozliseni_x / 2) - 15
pozice_hrace_y = (rozliseni_y / 2) - 15

pozice_enemy_x = (rozliseni_x / 2) - 23
pozice_enemy_y = (rozliseni_y / 4) - 23

fps_casovac = pygame.time.Clock()
fps = 60

random_R = random.randint(0, 255)
random_G = random.randint(0, 255)
random_B = random.randint(0, 255)

random_color = (random_R, random_G, random_B)

player_idle = pygame.image.load("player idle.png")
player_moving = pygame.image.load("player moving.png")

enemy_idle = pygame.image.load("Enemy_1_idle.png")

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

cervena = (255, 0, 0)

strely_1 = []
strely_2 = []

hrac = Hrac(pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving)
enemy = Enemy(pozice_enemy_x, pozice_enemy_y, rozliseni_x, rozliseni_y, okno, enemy_idle)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps_casovac.tick(fps)

    okno.fill(random_color)

    hrac.pohni_se()

    strela_1 = hrac.vystrel_1()
    if strela_1 != None:
        strely_1.append(strela_1)

    strela_2 = hrac.vystrel_2()
    if strela_2 != None:
        strely_2.append(strela_2)

    for strela_1 in strely_1:
        if strela_1 != None:
            strela_1[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_1)

    for strela_2 in strely_2:
        if strela_2 != None:
            strela_2[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_2)

    enemy.vykresli_se()

    pygame.display.flip()