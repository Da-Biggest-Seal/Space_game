import random
import pygame
pygame.init()

class Enemy:
    def __init__(self, enemy_1_x, enemy_1_y, rozliseni_x, rozliseni_y, okno, enemy_idle, Pocet_LVL_1):
        self.enemy_1_x = enemy_1_x
        self.enemy_1_y = enemy_1_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno
        self.enemy_idle = enemy_idle
        self.Pocet_LVL_1 = Pocet_LVL_1
        self.Recty_1 = []

        self.hit_pointy = [0] * len(self.enemy_1_x)
        self.zdravicko = 6

    def vykresli_se(self):

        self.Recty_1 = []

        if len(self.enemy_1_x) == 0:
            return

        for i in range(len(self.enemy_1_x)):
            self.okno.blit(self.enemy_idle, (self.enemy_1_x[i], self.enemy_1_y[i]))
            self.Recty_1.append(pygame.Rect(self.enemy_1_x[i], self.enemy_1_y[i], 47, 47))

        for i, y in enumerate(self.enemy_1_y):
            if y >= -47:

                if self.enemy_1_x[i] >= self.rozliseni_x - 50:
                    self.enemy_1_x[i] -=4
                
                elif self.enemy_1_x[i] <= 0:
                    self.enemy_1_x[i] += 4

                elif self.enemy_1_x[i] - 4 >= 0 and self.enemy_1_x[i] + 4 <= self.rozliseni_x - 50:
                    self.enemy_1_x[i] -= 4

    def checkni_kolizi_1(self, strela_1):
        if len(self.Recty_1) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_1):
            if rect.colliderect((strela_1[0], strela_1[1], strela_1[2], strela_1[3])):
                self.hit_pointy[i] += 1
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None
    
    def checkni_kolizi_2(self, strela_2):
        if len(self.Recty_1) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_1):
            if rect.colliderect((strela_2[0], strela_2[1], strela_2[2], strela_2[3])):
                self.hit_pointy[i] += 1
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None