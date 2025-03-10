import pygame
#pygame.init()

class Enemy_2:
    def __init__(self, enemy_2_x, enemy_2_y, rozliseni_x, rozliseni_y, okno, enemy_2_idle, pocet_LVL_2):
        self.enemy_2_x = enemy_2_x
        self.enemy_2_y = enemy_2_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno
        self.enemy_2_idle = enemy_2_idle
        self.Pocet_LVL_2 = pocet_LVL_2
        self.Recty_2 = []
        self.direction = [1] * len(enemy_2_x)
        self.enemy_cooldown_1 = [15] * len(enemy_2_x)
        self.enemy_cooldown_2 = [15/2] * len(enemy_2_x)
        self.enemy_cooldown_3 = [15] * len(enemy_2_x)
        self.enemy_cooldown_4 = [15/2] * len(enemy_2_x)

        self.hit_pointy = [0] * len(self.enemy_2_x)
        self.zdravicko = 8

    def vykresli_se(self):

        self.Recty_2 = []

        if len(self.enemy_2_x) == 0:
            return

        for i in range(len(self.enemy_2_x)):
            self.okno.blit(self.enemy_2_idle, (self.enemy_2_x[i], self.enemy_2_y[i]))
            self.Recty_2.append(pygame.Rect(self.enemy_2_x[i], self.enemy_2_y[i], 65, 65))

        for i, y in enumerate(self.enemy_2_y):
            if y >= -65:
                self.enemy_2_x[i] += 4 * self.direction[i]

                if self.enemy_2_x[i] >= self.rozliseni_x - 70:
                    self.direction[i] = -1

                elif self.enemy_2_x[i] <= 0:
                    self.direction[i] = 1

    def checkni_kolizi_1(self, strela_1):
        if len(self.Recty_2) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_2):
            if rect.colliderect((strela_1[0], strela_1[1], strela_1[2], strela_1[3])):
                self.hit_pointy[i] += 1
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None
    
    def checkni_kolizi_2(self, strela_2):
        if len(self.Recty_2) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_2):
            if rect.colliderect((strela_2[0], strela_2[1], strela_2[2], strela_2[3])):
                self.hit_pointy[i] += 1
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None
    
    def sniz_enemy_cooldown(self):
        for i in range(len(self.enemy_2_x)):
            if self.enemy_2_y[i] >= -55:
                self.enemy_cooldown_1[i] -= 1
                self.enemy_cooldown_2[i] -= 1
                self.enemy_cooldown_3[i] -= 1
                self.enemy_cooldown_4[i] -= 1
    
    def strelba_enemy_1(self):
        enemy_strely_1 = []

        for i in range(len(self.enemy_2_y)):
            if self.enemy_2_y[i] >= -65:

                if self.enemy_cooldown_1[i] <= 0:
                    enemy_strela_1 = pygame.Rect(self.enemy_2_x[i] + 10, self.enemy_2_y[i] + 24, 3, 5)
                    self.enemy_cooldown_1[i] = 15
                    enemy_strely_1.append(enemy_strela_1)

        return enemy_strely_1
    
    def strelba_enemy_2(self):
        enemy_strely_2 = []

        for i in range(len(self.enemy_2_y)):
            if self.enemy_2_y[i] >= -65:

                if self.enemy_cooldown_2[i] <= 0:
                    enemy_strela_2 = pygame.Rect(self.enemy_2_x[i] + 15, self.enemy_2_y[i] + 24, 3, 5)
                    self.enemy_cooldown_2[i] = 15
                    enemy_strely_2.append(enemy_strela_2)

        return enemy_strely_2
    
    def strelba_enemy_3(self):
        enemy_strely_3 = []

        for i in range(len(self.enemy_2_y)):
            if self.enemy_2_y[i] >= -65:

                if self.enemy_cooldown_3[i] <= 0:
                    enemy_strela_3 = pygame.Rect(self.enemy_2_x[i] + 51, self.enemy_2_y[i] + 24, 3, 5)
                    self.enemy_cooldown_3[i] = 15
                    enemy_strely_3.append(enemy_strela_3)

        return enemy_strely_3
    
    def strelba_enemy_4(self):
        enemy_strely_4 = []

        for i in range(len(self.enemy_2_y)):
            if self.enemy_2_y[i] >= -65:

                if self.enemy_cooldown_4[i] <= 0:
                    enemy_strela_4 = pygame.Rect(self.enemy_2_x[i] + 56, self.enemy_2_y[i] + 24, 3, 5)
                    self.enemy_cooldown_4[i] = 15
                    enemy_strely_4.append(enemy_strela_4)

        return enemy_strely_4