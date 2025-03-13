import pygame

class Enemy_3:
    def __init__(self, enemy_3_x, enemy_3_y, rozliseni_x, rozliseni_y, okno, enemy_3_idle, pocet_LVL_3, damage):
        self.enemy_3_x = enemy_3_x
        self.enemy_3_y = enemy_3_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno
        self.enemy_3_idle = enemy_3_idle
        self.Pocet_LVL_3 = pocet_LVL_3
        self.Recty_3 = []
        self.direction = [1] * len(enemy_3_x)
        self.enemy_cooldown_1 = [15] * len(enemy_3_x)
        self.enemy_cooldown_2 = [15/2] * len(enemy_3_x)
        self.enemy_cooldown_3 = [15] * len(enemy_3_x)
        self.enemy_cooldown_4 = [15/2] * len(enemy_3_x)
        self.enemy_cooldown_5 = [15] * len(enemy_3_x)
        self.enemy_cooldown_6 = [15/2] * len(enemy_3_x)
        self.damage = damage

        self.hit_pointy = [0] * len(self.enemy_3_x)
        self.zdravicko = 10

    def vykresli_se(self):

        self.Recty_3 = []

        if len(self.enemy_3_x) == 0:
            return

        for i in range(len(self.enemy_3_x)):
            self.okno.blit(self.enemy_3_idle, (self.enemy_3_x[i], self.enemy_3_y[i]))
            self.Recty_3.append(pygame.Rect(self.enemy_3_x[i], self.enemy_3_y[i], 99, 99))

        for i, y in enumerate(self.enemy_3_y):
            if y >= -99:
                self.enemy_3_x[i] += 4 * self.direction[i]

                if self.enemy_3_x[i] >= self.rozliseni_x - 70:
                    self.direction[i] = -1

                elif self.enemy_3_x[i] <= 0:
                    self.direction[i] = 1

    def checkni_kolizi_1(self, strela_1):
        if len(self.Recty_3) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_3):
            if rect.colliderect((strela_1[0], strela_1[1], strela_1[2], strela_1[3])):
                self.hit_pointy[i] += self.damage
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None
    
    def checkni_kolizi_2(self, strela_2):
        if len(self.Recty_3) == 0:
            return False, None

        for i, rect in enumerate(self.Recty_3):
            if rect.colliderect((strela_2[0], strela_2[1], strela_2[2], strela_2[3])):
                self.hit_pointy[i] += self.damage
                if self.hit_pointy[i] >= self.zdravicko:
                    return True, i
                return True, None
        return False, None
    
    def sniz_enemy_cooldown(self):
        for i in range(len(self.enemy_3_x)):
            if self.enemy_3_y[i] >= -55:
                self.enemy_cooldown_1[i] -= 1
                self.enemy_cooldown_2[i] -= 1
                self.enemy_cooldown_3[i] -= 1
                self.enemy_cooldown_4[i] -= 1
                self.enemy_cooldown_5[i] -= 1
                self.enemy_cooldown_6[i] -= 1
    
    def strelba_enemy_1(self):
        enemy_strely_1 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_1[i] <= 0:
                    enemy_strela_1 = pygame.Rect(self.enemy_3_x[i] + 21, self.enemy_3_y[i] + 80, 3, 5)
                    self.enemy_cooldown_1[i] = 15
                    enemy_strely_1.append(enemy_strela_1)

        return enemy_strely_1
    
    def strelba_enemy_2(self):
        enemy_strely_2 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_2[i] <= 0:
                    enemy_strela_2 = pygame.Rect(self.enemy_3_x[i] + 35, self.enemy_3_y[i] + 81, 3, 5)
                    self.enemy_cooldown_2[i] = 15
                    enemy_strely_2.append(enemy_strela_2)

        return enemy_strely_2
    
    def strelba_enemy_3(self):
        enemy_strely_3 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_3[i] <= 0:
                    enemy_strela_3 = pygame.Rect(self.enemy_3_x[i] + 50, self.enemy_3_y[i] + 82, 3, 5)
                    self.enemy_cooldown_3[i] = 15
                    enemy_strely_3.append(enemy_strela_3)

        return enemy_strely_3
    
    def strelba_enemy_4(self):
        enemy_strely_4 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_4[i] <= 0:
                    enemy_strela_4 = pygame.Rect(self.enemy_3_x[i] + 60, self.enemy_3_y[i] + 82, 3, 5)
                    self.enemy_cooldown_4[i] = 15
                    enemy_strely_4.append(enemy_strela_4)

        return enemy_strely_4
    
    def strelba_enemy_5(self):
        enemy_strely_5 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_5[i] <= 0:
                    enemy_strela_5 = pygame.Rect(self.enemy_3_x[i] + 65, self.enemy_3_y[i] + 81, 3, 5)
                    self.enemy_cooldown_5[i] = 15
                    enemy_strely_5.append(enemy_strela_5)

        return enemy_strely_5
    
    def strelba_enemy_6(self):
        enemy_strely_6 = []

        for i in range(len(self.enemy_3_y)):
            if self.enemy_3_y[i] >= -99:

                if self.enemy_cooldown_6[i] <= 0:
                    enemy_strela_6 = pygame.Rect(self.enemy_3_x[i] + 70, self.enemy_3_y[i] + 80, 3, 5)
                    self.enemy_cooldown_6[i] = 15
                    enemy_strely_6.append(enemy_strela_6)

        return enemy_strely_6