import sys
import random
import pygame
pygame.font.init()

#class import
from hrac import Hrac
from enemy_1 import Enemy_1
from pozadi import Pozadi
from shop import Shop
from enemy_2 import Enemy_2

#rozliseni
rozliseni_x = 800
rozliseni_y = 600

#font
font = pygame.font.SysFont("Calibri", 24)

#okno
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption("Space-Game")

#pozadi
bg_a = pygame.image.load("bg//bg_a.png")
bg_b = pygame.image.load("bg//bg_b.png")
bg_c = pygame.image.load("bg//bg_c.png")

#hrac
pozice_hrace_x = (rozliseni_x / 2) - 15
pozice_hrace_y = (rozliseni_y / 2) - 15

player_idle = pygame.image.load("player textury//player idle.png")
player_moving = pygame.image.load("player textury//player moving.png")

cooldown = 15

money = 0

hrac_hity = 0
hrac_max_hity = 20

#enemaci
enemy_idle = pygame.image.load("enemy textury//enemy_1//Enemy_1_idle.png")
enemy_2_idle = pygame.image.load("enemy textury//enemy_2//enemy_2_idle.png")

hit_point_1 = 0

enemy_1_kill = False

enemy_1_x = []
enemy_1_y = []

enemy_2_x = []
enemy_2_y = []

pocet_LVL_1 = random.randint(4, 8)
pocet_LVL_2 = random.randint(2, 4)

for i in range(pocet_LVL_1):
    pozice_enemy_x = random.randint(0, int(rozliseni_x - 47))
    pozice_enemy_y = random.randint(0, int((rozliseni_y / 4) - 47)) - 2000

    enemy_1_x.append(pozice_enemy_x)
    enemy_1_y.append(pozice_enemy_y)

for i in range(pocet_LVL_2):
    pozice_enemy_2_x = random.randint(0, int(rozliseni_x - 65))
    pozice_enemy_2_y = random.randint(0, int(rozliseni_y / 8)) - 4000

    enemy_2_x.append(pozice_enemy_2_x)
    enemy_2_y.append(pozice_enemy_2_y)

list_enemy_1 = [enemy_1_x, enemy_1_y]
list_enemy_2 = [enemy_2_x, enemy_2_y]

enemy_strely_1 = []
enemy_strely_2 = []

#fps
fps_casovac = pygame.time.Clock()
fps = 60

#barvicky
cerna = (0, 0, 0)
cervena = (255, 0, 0)
bila = (255, 255, 255)

#strely
strely_1 = []
strely_2 = []

#shop
shop = pygame.image.load("Shop.png")

shop_x = rozliseni_x - 100
shop_y = [(rozliseni_y / 2) - 2550, (rozliseni_y / 2) - 4550, (rozliseni_y / 2) - 6550]

#aktivace class
hrac = Hrac(pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown)
enemy_1 = Enemy_1(enemy_1_x, enemy_1_y, rozliseni_x, rozliseni_y, okno, enemy_idle, pocet_LVL_1)
pozadi = Pozadi(bg_a, bg_b, bg_c, pozice_hrace_y, rozliseni_y, list_enemy_1, list_enemy_2)
shop = Shop(shop, shop_x, shop_y, okno)
enemy_2 = Enemy_2(enemy_2_x, enemy_2_y, rozliseni_x, rozliseni_y, okno, enemy_2_idle, pocet_LVL_2)

#game loop
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps_casovac.tick(fps)

    okno.fill(cerna)

    pozadi.pozice_hrace_y = hrac.pozice_hrace_y
    pozadi.update(okno)

    #sniz cooldown
    hrac.sniz_cooldown()

    #sniz enemy cooldown
    enemy_1.sniz_enemy_cooldown()
    enemy_2.sniz_enemy_cooldown()

    #vykresleni hrace
    hrac.pohni_se()

    #strely
    strela_1 = hrac.vystrel_1()
    if strela_1 != None:
        strely_1.append(strela_1)

    strela_2 = hrac.vystrel_2()
    if strela_2 != None:
        strely_2.append(strela_2)

    #enemy strely
    enemy_strely_1_alfa = enemy_1.strelba_enemy_1()
    if enemy_strely_1_alfa:
        enemy_strely_1.extend(enemy_strely_1_alfa)

    enemy_strely_2_alfa = enemy_1.strelba_enemy_2()
    if enemy_strely_2_alfa:
        enemy_strely_2.extend(enemy_strely_2_alfa)

    try:
        for i in enemy_strely_1:
            enemy_strela_1 = i

        for i in enemy_strely_2:
            enemy_strela_2 = i

    except:
        pass

    #vykresleni strel
    for strela_1 in strely_1:
        if strela_1 != None:
            strela_1[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_1)

    for strela_2 in strely_2:
        if strela_2 != None:
            strela_2[1] -= 10
            pygame.draw.ellipse(okno, cervena, strela_2)

    #vykresleni enemy 1 strel
    for enemy_strela_1 in enemy_strely_1:
        if enemy_strela_1 != None:
            enemy_strela_1[1] += 10
            pygame.draw.ellipse(okno, cervena, enemy_strela_1)

    for enemy_strela_2 in enemy_strely_2:
        if enemy_strela_2 != None:
            enemy_strela_2[1] += 10
            pygame.draw.ellipse(okno, cervena, enemy_strela_2)

    #vykresleni enemy
    enemy_1.vykresli_se()
    enemy_2.vykresli_se()

    #pocitani ammo
    pocet_ammo = hrac.pocet_naboju()

    #sestreleni enemaka
    for strela_1 in strely_1[:]:
            hit, hit_index = enemy_1.checkni_kolizi_1(strela_1)

            if hit:
                if strela_1 in strely_1:
                    strely_1.remove(strela_1)

                if hit_index is not None and hit_index < len(list_enemy_1[0]):
                    list_enemy_1[0].pop(hit_index)
                    list_enemy_1[1].pop(hit_index)
                    enemy_1.hit_pointy.pop(hit_index)

                    enemy_1.enemy_cooldown_1.pop(hit_index)
                    enemy_1.enemy_cooldown_2.pop(hit_index)
                    enemy_1_kill = True

                    enemy_1.Recty_1 = []
                    for i in range(len(list_enemy_1[0])):
                        enemy_1.Recty_1.append(pygame.Rect(list_enemy_1[0][i], list_enemy_1[1][i], 47, 47))

    for strela_2 in strely_2[:]:

            hit, hit_index = enemy_1.checkni_kolizi_2(strela_2)

            if hit:
                if strela_2 in strely_2:
                    strely_2.remove(strela_2)

                if hit_index is not None and hit_index < len(list_enemy_1[0]):
                    list_enemy_1[0].pop(hit_index)
                    list_enemy_1[1].pop(hit_index)
                    enemy_1.hit_pointy.pop(hit_index)

                    enemy_1.enemy_cooldown_1.pop(hit_index)
                    enemy_1.enemy_cooldown_2.pop(hit_index)
                    enemy_1_kill = True

                    enemy_1.Recty_1 = []
                    for i in range(len(list_enemy_1[0])):
                        enemy_1.Recty_1.append(pygame.Rect(list_enemy_1[0][i], list_enemy_1[1][i], 47, 47))

    #hity hrace
    enemy_strely_1_trefa = []
    enemy_strely_2_trefa = []

    for i, enemy_strela_1_trefa in enumerate(enemy_strely_1):
        if hrac.checkni_kolizi_1(enemy_strela_1_trefa):
            enemy_strely_1_trefa.append(i)
            hrac_hity += 1

    for i, enemy_strela_2_trefa in enumerate(enemy_strely_2):
        if hrac.checkni_kolizi_2(enemy_strela_2_trefa):
            enemy_strely_2_trefa.append(i)
            hrac_hity += 1

    for i in sorted(enemy_strely_1_trefa, reverse=True):
        if i < len(enemy_strely_1):
            enemy_strely_1.pop(i)

    for i in sorted(enemy_strely_2_trefa, reverse=True):
        if i < len(enemy_strely_2):
            enemy_strely_2.pop(i)

    hp = 100 - ((hrac_hity / hrac_max_hity) * 100)

    #pricteni penez za kill
    if enemy_1_kill == True:
        money += 10
        enemy_1_kill = False

    #info hud
    text_ammo = font.render("Počet nábojů: " + str(pocet_ammo), True, bila)
    text_ammo_rect = text_ammo.get_rect(center= (90, (rozliseni_y - 20)))

    text_money = font.render("Finance: " + str(money), True, bila)
    text_money_rect = text_money.get_rect(center= (((rozliseni_x / 4) * 3), (rozliseni_y - 20)))

    text_hp = font.render("HP: " + str(hp) + "%", True, bila)
    text_hp_rect = text_hp.get_rect(center= ((rozliseni_x / 2), (rozliseni_y - 20)))

    okno.blit(text_ammo, text_ammo_rect)
    okno.blit(text_money, text_money_rect)
    okno.blit(text_hp, text_hp_rect)

    #shop
    shop.vykresli_se()

    if hrac_hity >= hrac_max_hity:
        okno.fill(cerna)
        kill_text = font.render("You died!", True, bila)
        kill_text_rect = kill_text.get_rect(center= ((rozliseni_x / 2), (rozliseni_y / 2)))
        okno.blit(kill_text, kill_text_rect)

    pygame.display.flip()