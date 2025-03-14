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
from enemy_3 import Enemy_3

#rozliseni
rozliseni_x = 800
rozliseni_y = 600

#font
font = pygame.font.SysFont("Calibri", 24)

#okno
okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption("Space-Game")

#pozadi
bg_a = pygame.image.load("textury//bg//bg_a.png")
bg_b = pygame.image.load("textury//bg//bg_b.png")
bg_c = pygame.image.load("textury//bg//bg_c.png")

#hrac
pozice_hrace_x = (rozliseni_x / 2) - 15
pozice_hrace_y = (rozliseni_y / 2) - 15

player_idle = pygame.image.load("textury//player textury//player idle.png")
player_moving = pygame.image.load("textury//player textury//player moving.png")

cooldown = 15

money = 0

hrac_hity = 0
hrac_max_hity = 20
damage_1 = 1
damage = damage_1

#pocitani ammo
pocet_ammo = 100

#enemaci
enemy_idle = pygame.image.load("textury//enemy textury//enemy_1//Enemy_1_idle.png")
enemy_2_idle = pygame.image.load("textury//enemy textury//enemy_2//enemy_2_idle.png")
enemy_3_idle = pygame.image.load("textury//enemy textury//enemy_3//enemy_3.png")

hit_point_1 = 0

enemy_1_kill = False
enemy_2_kill = False
enemy_3_kill = False

enemy_1_x = []
enemy_1_y = []

enemy_2_x = []
enemy_2_y = []

enemy_3_x = []
enemy_3_y = []

pocet_LVL_1 = random.randint(4, 8)
pocet_LVL_2 = random.randint(2, 4)
pocet_LVL_3 = random.randint(2, 3)

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

for i in range(pocet_LVL_3):
    pozice_enemy_3_x = random.randint(0, int(rozliseni_x - 99))
    pozice_enemy_3_y = random.randint(0, int(rozliseni_y / 8)) - 6000

    enemy_3_x.append(pozice_enemy_3_x)
    enemy_3_y.append(pozice_enemy_3_y)

list_enemy_1 = [enemy_1_x, enemy_1_y]
list_enemy_2 = [enemy_2_x, enemy_2_y]
list_enemy_3 = [enemy_3_x, enemy_3_y]

enemy_strely_1 = []
enemy_strely_2 = []

enemy_2_strely_1 = []
enemy_2_strely_2 = []
enemy_2_strely_3 = []
enemy_2_strely_4 = []

enemy_3_strely_1 = []
enemy_3_strely_2 = []
enemy_3_strely_3 = []
enemy_3_strely_4 = []
enemy_3_strely_5 = []
enemy_3_strely_6 = []

#fps
fps_casovac = pygame.time.Clock()
fps = 60

#barvicky
cerna = (0, 0, 0)
cervena = (255, 0, 0)
bila = (255, 255, 255)
zluta = (252, 223, 3)

#strely
strely_1 = []
strely_2 = []

#shop
shop_img = pygame.image.load("textury//shop textury//Shop.png")

shop_x = rozliseni_x - 100
shop_y = [(rozliseni_y / 2) - 2550, (rozliseni_y / 2) - 4550, (rozliseni_y / 2) - 6550]
Recty_shopu = []

shop_gui_0 = pygame.image.load("textury//shop textury//shop_gui_0.png")
shop_gui_1 = pygame.image.load("textury//shop textury//shop_gui_1.png")
shop_gui_2 = pygame.image.load("textury//shop textury//shop_gui_2.png")
shop_gui_3 = pygame.image.load("textury//shop textury//shop_gui_3.png")
shop_gui_4 = pygame.image.load("textury//shop textury//shop_gui_4.png")

vyuzite_money = 0

#aktivace class
hrac = Hrac(pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown, pocet_ammo)
enemy_1 = Enemy_1(enemy_1_x, enemy_1_y, rozliseni_x, rozliseni_y, okno, enemy_idle, pocet_LVL_1, damage)
pozadi = Pozadi(bg_a, bg_b, bg_c, pozice_hrace_y, rozliseni_y, list_enemy_1, list_enemy_2, list_enemy_3)
shop = Shop(shop_img, shop_gui_0, shop_gui_1, shop_gui_2, shop_gui_3, shop_gui_4, shop_x, shop_y, pozice_hrace_y, rozliseni_x, rozliseni_y, Recty_shopu, font, list_enemy_1, list_enemy_2, list_enemy_3)
enemy_2 = Enemy_2(enemy_2_x, enemy_2_y, rozliseni_x, rozliseni_y, okno, enemy_2_idle, pocet_LVL_2, damage)
enemy_3 = Enemy_3(enemy_3_x, enemy_3_y, rozliseni_x, rozliseni_y, okno, enemy_3_idle, pocet_LVL_3, damage)

#game loop
while True:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fps_casovac.tick(fps)

    okno.fill(cerna)

    pozadi.pozice_hrace_y = hrac.pozice_hrace_y
    pozadi.update(okno)

    mys = pygame.mouse.get_pos()

    mys_x = mys[0]
    mys_y = mys[1]

    #shop
    shop.pozice_hrace_y = hrac.pozice_hrace_y

    shop.vykresli_se(okno)

    hrac.shop_kolize(shop_x, shop_y)

    shop_return = shop.otevri_se(hrac, okno, udalosti, money, hrac_hity, pocet_ammo, cooldown, damage)
    if shop_return != None:
        money, pocet_ammo, hrac_hity, cooldown, damage = shop_return

        vyuzite_money = money - shop_return[0]
        money = shop_return[0]

        hrac_hity = shop_return[2]
        pocet_ammo = shop_return[1]
        new_cooldown = shop_return[3]
        new_damage = shop_return[4]

        hrac.pocet_ammo = pocet_ammo
        damage = new_damage
        cooldown = new_cooldown

    hrac.base_cooldown = cooldown

    # After updating damage, update it in your enemy instances
    enemy_1.damage = damage
    enemy_2.damage = damage
    enemy_3.damage = damage

    #sniz cooldown
    hrac.sniz_cooldown()

    #sniz enemy cooldown
    enemy_1.sniz_enemy_cooldown()
    enemy_2.sniz_enemy_cooldown()
    enemy_3.sniz_enemy_cooldown()

    #vykresleni hrace
    hrac.pohni_se()

    #strely
    strela_1 = hrac.vystrel_1()
    if strela_1 != None:
        strely_1.append(strela_1)

    strela_2 = hrac.vystrel_2()
    if strela_2 != None:
        strely_2.append(strela_2)

    pocet_ammo = hrac.pocet_ammo

    #enemy 1 strely
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

    #enemy 2 strely
    enemy_2_strely_1_alfa = enemy_2.strelba_enemy_1()
    if enemy_2_strely_1_alfa:
        enemy_2_strely_1.extend(enemy_2_strely_1_alfa)

    enemy_2_strely_2_alfa = enemy_2.strelba_enemy_2()
    if enemy_2_strely_2_alfa:
        enemy_2_strely_2.extend(enemy_2_strely_2_alfa)

    enemy_2_strely_3_alfa = enemy_2.strelba_enemy_3()
    if enemy_2_strely_3_alfa:
        enemy_2_strely_3.extend(enemy_2_strely_3_alfa)

    enemy_2_strely_4_alfa = enemy_2.strelba_enemy_4()
    if enemy_2_strely_4_alfa:
        enemy_2_strely_4.extend(enemy_2_strely_4_alfa)

    try:
        for i in enemy_2_strely_1:
            enemy_2_strela_1 = i

        for i in enemy_2_strely_2:
            enemy_2_strela_2 = i

        for i in enemy_2_strely_3:
            enemy_2_strela_3 = i

        for i in enemy_2_strely_4:
            enemy_2_strela_4 = i

    except:
        pass

    #enemy 3 strely
    enemy_3_strely_1_alfa = enemy_3.strelba_enemy_1()
    if enemy_3_strely_1_alfa:
        enemy_3_strely_1.extend(enemy_3_strely_1_alfa)

    enemy_3_strely_2_alfa = enemy_3.strelba_enemy_2()
    if enemy_3_strely_2_alfa:
        enemy_3_strely_2.extend(enemy_3_strely_2_alfa)

    enemy_3_strely_3_alfa = enemy_3.strelba_enemy_3()
    if enemy_3_strely_3_alfa:
        enemy_3_strely_3.extend(enemy_3_strely_3_alfa)

    enemy_3_strely_4_alfa = enemy_3.strelba_enemy_4()
    if enemy_3_strely_4_alfa:
        enemy_3_strely_4.extend(enemy_3_strely_4_alfa)

    enemy_3_strely_5_alfa = enemy_3.strelba_enemy_5()
    if enemy_3_strely_5_alfa:
        enemy_3_strely_5.extend(enemy_3_strely_5_alfa)

    enemy_3_strely_6_alfa = enemy_3.strelba_enemy_6()
    if enemy_3_strely_6_alfa:
        enemy_3_strely_6.extend(enemy_3_strely_6_alfa)

    try:
        for i in enemy_3_strely_1:
            enemy_3_strela_1 = i

        for i in enemy_3_strely_2:
            enemy_3_strela_2 = i

        for i in enemy_3_strely_3:
            enemy_3_strela_3 = i

        for i in enemy_3_strely_4:
            enemy_3_strela_4 = i

        for i in enemy_3_strely_5:
            enemy_3_strela_5 = i

        for i in enemy_3_strely_6:
            enemy_3_strela_6 = i

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
            pygame.draw.ellipse(okno, zluta, enemy_strela_1)

    for enemy_strela_2 in enemy_strely_2:
        if enemy_strela_2 != None:
            enemy_strela_2[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_strela_2)

    #vystreleni enemy 2 strel
    for enemy_2_strela_1 in enemy_2_strely_1:
        if enemy_2_strela_1 != None:
            enemy_2_strela_1[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_2_strela_1)

    for enemy_2_strela_2 in enemy_2_strely_2:
        if enemy_2_strela_2 != None:
            enemy_2_strela_2[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_2_strela_2)

    for enemy_2_strela_3 in enemy_2_strely_3:
        if enemy_2_strela_3 != None:
            enemy_2_strela_3[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_2_strela_3)

    for enemy_2_strela_4 in enemy_2_strely_4:
        if enemy_2_strela_4 != None:
            enemy_2_strela_4[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_2_strela_4)

    #vystreleni enemy 3 strel
    for enemy_3_strela_1 in enemy_3_strely_1:
        if enemy_3_strela_1 != None:
            enemy_3_strela_1[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_1)

    for enemy_3_strela_2 in enemy_3_strely_2:
        if enemy_3_strela_2 != None:
            enemy_3_strela_2[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_2)

    for enemy_3_strela_3 in enemy_3_strely_3:
        if enemy_3_strela_3 != None:
            enemy_3_strela_3[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_3)

    for enemy_3_strela_4 in enemy_3_strely_4:
        if enemy_3_strela_4 != None:
            enemy_3_strela_4[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_4)

    for enemy_3_strela_5 in enemy_3_strely_5:
        if enemy_3_strela_5 != None:
            enemy_3_strela_5[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_5)

    for enemy_3_strela_6 in enemy_3_strely_6:
        if enemy_3_strela_6 != None:
            enemy_3_strela_6[1] += 10
            pygame.draw.ellipse(okno, zluta, enemy_3_strela_6)

    #vykresleni enemy
    enemy_1.vykresli_se()
    enemy_2.vykresli_se()
    enemy_3.vykresli_se()

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



    for strela_1 in strely_1[:]:
            hit, hit_index = enemy_2.checkni_kolizi_1(strela_1)

            if hit:
                if strela_1 in strely_1:
                    strely_1.remove(strela_1)

                if hit_index is not None and hit_index < len(list_enemy_2[0]):
                    list_enemy_2[0].pop(hit_index)
                    list_enemy_2[1].pop(hit_index)
                    enemy_2.hit_pointy.pop(hit_index)

                    enemy_2.enemy_cooldown_1.pop(hit_index)
                    enemy_2.enemy_cooldown_2.pop(hit_index)
                    enemy_2.enemy_cooldown_3.pop(hit_index)
                    enemy_2.enemy_cooldown_4.pop(hit_index)
                    enemy_2_kill = True

                    enemy_2.Recty_1 = []
                    for i in range(len(list_enemy_2[0])):
                        enemy_2.Recty_1.append(pygame.Rect(list_enemy_2[0][i], list_enemy_2[1][i], 65, 65))

    for strela_2 in strely_2[:]:

            hit, hit_index = enemy_2.checkni_kolizi_2(strela_2)

            if hit:
                if strela_2 in strely_2:
                    strely_2.remove(strela_2)

                if hit_index is not None and hit_index < len(list_enemy_2[0]):
                    list_enemy_2[0].pop(hit_index)
                    list_enemy_2[1].pop(hit_index)
                    enemy_2.hit_pointy.pop(hit_index)

                    enemy_2.enemy_cooldown_1.pop(hit_index)
                    enemy_2.enemy_cooldown_2.pop(hit_index)
                    enemy_2.enemy_cooldown_3.pop(hit_index)
                    enemy_2.enemy_cooldown_4.pop(hit_index)
                    enemy_2_kill = True

                    enemy_2.Recty_1 = []
                    for i in range(len(list_enemy_2[0])):
                        enemy_2.Recty_1.append(pygame.Rect(list_enemy_2[0][i], list_enemy_2[1][i], 65, 65))

    for strela_1 in strely_1[:]:
            hit, hit_index = enemy_3.checkni_kolizi_1(strela_1)

            if hit:
                if strela_1 in strely_1:
                    strely_1.remove(strela_1)

                if hit_index is not None and hit_index < len(list_enemy_3[0]):
                    list_enemy_3[0].pop(hit_index)
                    list_enemy_3[1].pop(hit_index)
                    enemy_3.hit_pointy.pop(hit_index)

                    enemy_3.enemy_cooldown_1.pop(hit_index)
                    enemy_3.enemy_cooldown_2.pop(hit_index)
                    enemy_3.enemy_cooldown_3.pop(hit_index)
                    enemy_3.enemy_cooldown_4.pop(hit_index)
                    enemy_3.enemy_cooldown_5.pop(hit_index)
                    enemy_3.enemy_cooldown_6.pop(hit_index)
                    enemy_3_kill = True

                    enemy_3.Recty_3 = []
                    for i in range(len(list_enemy_3[0])):
                        enemy_3.Recty_3.append(pygame.Rect(list_enemy_3[0][i], list_enemy_3[1][i], 99, 99))

    for strela_2 in strely_2[:]:

            hit, hit_index = enemy_3.checkni_kolizi_2(strela_2)

            if hit:
                if strela_2 in strely_2:
                    strely_2.remove(strela_2)

                if hit_index is not None and hit_index < len(list_enemy_3[0]):
                    list_enemy_3[0].pop(hit_index)
                    list_enemy_3[1].pop(hit_index)
                    enemy_3.hit_pointy.pop(hit_index)

                    enemy_3.enemy_cooldown_1.pop(hit_index)
                    enemy_3.enemy_cooldown_2.pop(hit_index)
                    enemy_3.enemy_cooldown_3.pop(hit_index)
                    enemy_3.enemy_cooldown_4.pop(hit_index)
                    enemy_3.enemy_cooldown_5.pop(hit_index)
                    enemy_3.enemy_cooldown_6.pop(hit_index)
                    enemy_3_kill = True

                    enemy_3.Recty_3 = []
                    for i in range(len(list_enemy_3[0])):
                        enemy_3.Recty_3.append(pygame.Rect(list_enemy_3[0][i], list_enemy_3[1][i], 99, 99))

    #hity hrace
    enemy_strely_1_trefa = []
    enemy_strely_2_trefa = []

    enemy_2_strely_1_trefa = []
    enemy_2_strely_2_trefa = []
    enemy_2_strely_3_trefa = []
    enemy_2_strely_4_trefa = []

    enemy_3_strely_1_trefa = []
    enemy_3_strely_2_trefa = []
    enemy_3_strely_3_trefa = []
    enemy_3_strely_4_trefa = []
    enemy_3_strely_5_trefa = []
    enemy_3_strely_6_trefa = []

    for i, enemy_strela_1_trefa in enumerate(enemy_strely_1):
        if hrac.checkni_kolizi_1_1(enemy_strela_1_trefa):
            enemy_strely_1_trefa.append(i)
            hrac_hity += 1

    for i, enemy_strela_2_trefa in enumerate(enemy_strely_2):
        if hrac.checkni_kolizi_1_2(enemy_strela_2_trefa):
            enemy_strely_2_trefa.append(i)
            hrac_hity += 1



    for i, enemy_2_strela_1_trefa in enumerate(enemy_2_strely_1):
        if hrac.checkni_kolizi_2_1(enemy_2_strela_1_trefa):
            enemy_2_strely_1_trefa.append(i)
            hrac_hity += 2

    for i, enemy_2_strela_2_trefa in enumerate(enemy_2_strely_2):
        if hrac.checkni_kolizi_2_2(enemy_2_strela_2_trefa):
            enemy_2_strely_2_trefa.append(i)
            hrac_hity += 2

    for i, enemy_2_strela_3_trefa in enumerate(enemy_2_strely_3):
        if hrac.checkni_kolizi_2_3(enemy_2_strela_3_trefa):
            enemy_2_strely_3_trefa.append(i)
            hrac_hity += 2

    for i, enemy_2_strela_4_trefa in enumerate(enemy_2_strely_4):
        if hrac.checkni_kolizi_2_4(enemy_2_strela_4_trefa):
            enemy_2_strely_4_trefa.append(i)
            hrac_hity += 2



    for i, enemy_3_strela_1_trefa in enumerate(enemy_3_strely_1):
        if hrac.checkni_kolizi_3_1(enemy_3_strela_1_trefa):
            enemy_3_strely_1_trefa.append(i)
            hrac_hity += 5/2

    for i, enemy_3_strela_2_trefa in enumerate(enemy_3_strely_2):
        if hrac.checkni_kolizi_3_2(enemy_3_strela_2_trefa):
            enemy_3_strely_2_trefa.append(i)
            hrac_hity += 5/2

    for i, enemy_3_strela_3_trefa in enumerate(enemy_3_strely_3):
        if hrac.checkni_kolizi_3_3(enemy_3_strela_3_trefa):
            enemy_3_strely_3_trefa.append(i)
            hrac_hity += 5/2

    for i, enemy_3_strela_4_trefa in enumerate(enemy_3_strely_4):
        if hrac.checkni_kolizi_3_4(enemy_3_strela_4_trefa):
            enemy_3_strely_4_trefa.append(i)
            hrac_hity += 5/2

    for i, enemy_3_strela_5_trefa in enumerate(enemy_3_strely_5):
        if hrac.checkni_kolizi_3_5(enemy_3_strela_5_trefa):
            enemy_3_strely_5_trefa.append(i)
            hrac_hity += 5/2

    for i, enemy_3_strela_6_trefa in enumerate(enemy_3_strely_6):
        if hrac.checkni_kolizi_3_6(enemy_3_strela_6_trefa):
            enemy_3_strely_6_trefa.append(i)
            hrac_hity += 5/2



    for i in sorted(enemy_strely_1_trefa, reverse=True):
        if i < len(enemy_strely_1):
            enemy_strely_1.pop(i)

    for i in sorted(enemy_strely_2_trefa, reverse=True):
        if i < len(enemy_strely_2):
            enemy_strely_2.pop(i)



    for i in sorted(enemy_2_strely_1_trefa, reverse=True):
        if i < len(enemy_2_strely_1):
            enemy_2_strely_1.pop(i)

    for i in sorted(enemy_2_strely_2_trefa, reverse=True):
        if i < len(enemy_2_strely_2):
            enemy_2_strely_2.pop(i)

    for i in sorted(enemy_2_strely_3_trefa, reverse=True):
        if i < len(enemy_2_strely_3):
            enemy_2_strely_3.pop(i)

    for i in sorted(enemy_2_strely_4_trefa, reverse=True):
        if i < len(enemy_2_strely_4):
            enemy_2_strely_4.pop(i)


    
    for i in sorted(enemy_3_strely_1_trefa, reverse=True):
        if i < len(enemy_3_strely_1):
            enemy_3_strely_1.pop(i)

    for i in sorted(enemy_3_strely_2_trefa, reverse=True):
        if i < len(enemy_3_strely_2):
            enemy_3_strely_2.pop(i)

    for i in sorted(enemy_3_strely_3_trefa, reverse=True):
        if i < len(enemy_3_strely_3):
            enemy_3_strely_3.pop(i)

    for i in sorted(enemy_3_strely_4_trefa, reverse=True):
        if i < len(enemy_3_strely_4):
            enemy_3_strely_4.pop(i)

    for i in sorted(enemy_3_strely_5_trefa, reverse=True):
        if i < len(enemy_3_strely_5):
            enemy_3_strely_5.pop(i)

    for i in sorted(enemy_3_strely_6_trefa, reverse=True):
        if i < len(enemy_3_strely_6):
            enemy_3_strely_6.pop(i)

    hp = 100 - ((hrac_hity / hrac_max_hity) * 100)

    #pricteni penez za kill
    if enemy_1_kill == True:
        money += 10
        enemy_1_kill = False

    if enemy_2_kill == True:
        money += 25
        enemy_2_kill = False

    if enemy_3_kill == True:
        money += 40
        enemy_3_kill = False

    blit_money = money - vyuzite_money

    #info hud
    text_ammo = font.render("Počet nábojů: " + str(pocet_ammo), True, bila)
    text_ammo_rect = text_ammo.get_rect(center= (90, (rozliseni_y - 20)))

    text_money = font.render("Rudium: " + str(blit_money), True, bila)
    text_money_rect = text_money.get_rect(center= (((rozliseni_x / 4) * 3), (rozliseni_y - 20)))

    text_hp = font.render("HP: " + str(hp) + "%", True, bila)
    text_hp_rect = text_hp.get_rect(center= ((rozliseni_x / 2), (rozliseni_y - 20)))

    okno.blit(text_ammo, text_ammo_rect)
    okno.blit(text_money, text_money_rect)
    okno.blit(text_hp, text_hp_rect)

    if hrac_hity >= hrac_max_hity:
        okno.fill(cerna)
        kill_text = font.render("You died!", True, bila)
        kill_text_rect = kill_text.get_rect(center= ((rozliseni_x / 2), (rozliseni_y / 2)))
        okno.blit(kill_text, kill_text_rect)

    pygame.display.flip()