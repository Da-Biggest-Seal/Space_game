import pygame
pygame.init()

class Pozadi:
    def __init__(self, bg_a, bg_b, bg_c, pozice_hrace_y, rozliseni_y, enemy_1):
        self.bg_a = bg_a
        self.bg_b = bg_b
        self.bg_c = bg_c
        self.scroll_speed = 4
        self.vyska = bg_a.get_height()
        self.y_bg_a = -self.vyska
        self.y_bg_b = -self.vyska * 2
        self.y_bg_c = 0
        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_y = rozliseni_y
        self.enemy_1 = enemy_1

    def update(self, okno):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_q]:
            self.y_bg_a += self.scroll_speed
            self.y_bg_b += self.scroll_speed
            self.y_bg_c += self.scroll_speed

            for i in range(len(self.enemy_1[1])):
                self.enemy_1[1][i] += 4

        if klavesa[pygame.K_e] and self.y_bg_c >= 0:
            self.y_bg_a -= self.scroll_speed
            self.y_bg_b -= self.scroll_speed
            self.y_bg_c -= self.scroll_speed

            for i in range(len(self.enemy_1[1])):
                self.enemy_1[1][i] -=4

        if self.y_bg_a >= self.rozliseni_y:
            self.y_bg_a = self.y_bg_b - self.vyska

        if self.y_bg_b >= self.rozliseni_y:
            self.y_bg_b = self.y_bg_a - self.vyska

        if self.y_bg_a <= -self.vyska * 2:
            self.y_bg_a = self.y_bg_b + self.vyska

        if self.y_bg_b <= -self.vyska * 2:
            self.y_bg_b = self.y_bg_a + self.vyska

        okno.blit(self.bg_a, (0, self.y_bg_a))
        okno.blit(self.bg_b, (0, self.y_bg_b))
        okno.blit(self.bg_c, (0, self.y_bg_c))