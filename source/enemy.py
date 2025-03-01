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
        self.direction = [1] * len(enemy_1_x)
        self.enemy_cooldown_1 = [15] * len(enemy_1_x)
        self.enemy_cooldown_2 = [15] * len(enemy_1_x)

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
                self.enemy_1_x[i] += 4 * self.direction[i]

                if self.enemy_1_x[i] >= self.rozliseni_x - 50:
                    self.direction[i] = -1

                elif self.enemy_1_x[i] <= 0:
                    self.direction[i] = 1

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
    
    def sniz_enemy_cooldown(self):
        for i in range(len(self.enemy_1_x)):
            if self.enemy_1_y[i] >= -55:
                self.enemy_cooldown_1[i] -= 1 / 2
                self.enemy_cooldown_2[i] -= 1 / 2
    
    def strelba_enemy_1(self):
        enemy_strely_1 = []

        for i in range(len(self.enemy_1_y)):
            if self.enemy_1_y[i] >= -47:

                if self.enemy_cooldown_1[i] <= 0:
                    enemy_strela_1 = pygame.Rect(self.enemy_1_x[i] + 11, self.enemy_1_y[i] + 24, 3, 5)
                    self.enemy_cooldown_1[i] = 15
                    enemy_strely_1.append(enemy_strela_1)

        return enemy_strely_1
    
    def strelba_enemy_2(self):
        enemy_strely_2 = []

        for i in range(len(self.enemy_1_y)):
            if self.enemy_1_y[i] >= -47:

                if self.enemy_cooldown_2[i] <= 0:
                    enemy_strela_2 = pygame.Rect(self.enemy_1_x[i] + 35, self.enemy_1_y[i] + 24, 3, 5)
                    self.enemy_cooldown_2[i] = 15
                    enemy_strely_2.append(enemy_strela_2)

        return enemy_strely_2