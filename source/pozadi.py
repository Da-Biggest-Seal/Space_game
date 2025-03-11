import pygame
#pygame.init()

class Pozadi:
    def __init__(self, bg_a, bg_b, bg_c, pozice_hrace_y, rozliseni_y, list_enemy_1, list_enemy_2, list_enemy_3):
        self.bg_a = bg_a
        self.bg_b = bg_b
        self.bg_c = bg_c
        self.bg_a_2 = bg_a
        self.scroll_speed = 4

        self.vyska = bg_a.get_height()
        self.sirka = bg_a.get_width()

        self.y_bg_a = -self.vyska
        self.y_bg_b = -self.vyska * 2
        self.y_bg_c = 0
        self.y_bg_a_2 = -self.vyska * 3
        self.x_bg = 0

        self.pozice_hrace_x = 0
        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_y = rozliseni_y

        self.enemy_1 = list_enemy_1
        self.enemy_2 = list_enemy_2
        self.enemy_3 = list_enemy_3

    def update(self, okno):
        if self.pozice_hrace_y <= 200:
            self.y_bg_a += self.scroll_speed
            self.y_bg_b += self.scroll_speed
            self.y_bg_a_2 += self.scroll_speed
            self.y_bg_c += self.scroll_speed

            for i in range(len(self.enemy_1[1])):
                self.enemy_1[1][i] += 4

            for i in range(len(self.enemy_2[1])):
                self.enemy_2[1][i] += 4

            for i in range(len(self.enemy_3[1])):
                self.enemy_3[1][i] += 4

        if self.pozice_hrace_y >= self.rozliseni_y - 150 and self.y_bg_c >= 0:
            self.y_bg_a -= self.scroll_speed
            self.y_bg_b -= self.scroll_speed
            self.y_bg_a_2 -= self.scroll_speed
            self.y_bg_c -= self.scroll_speed

            for i in range(len(self.enemy_1[1])):
                self.enemy_1[1][i] -=4

            for i in range(len(self.enemy_2[1])):
                self.enemy_2[1][i] -= 4

            for i in range(len(self.enemy_3[1])):
                self.enemy_3[1][i] -= 4

        self.player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)

        self.bg_a_rect = pygame.Rect(self.x_bg, self.y_bg_a, self.sirka, self.vyska)
        self.bg_b_rect = pygame.Rect(self.x_bg, self.y_bg_b, self.sirka, self.vyska)
        self.bg_a_2_rect = pygame.Rect(self.x_bg, self.y_bg_a_2, self.sirka, self.vyska)

        if self.bg_a_rect.colliderect(self.player_rect):
            self.bg_b_rect.y = self.bg_a_rect.y + self.vyska
            self.bg_a_2_rect.y = self.bg_a_rect.y - self.vyska
            print("dfg")

        elif self.bg_b_rect.colliderect(self.player_rect):
            self.bg_a_rect.y = self.bg_b_rect.y - self.vyska
            self.bg_a_2_rect.y = self.bg_b_rect.y + self.vyska
            print("jhk")

        elif self.bg_a_2_rect.colliderect(self.player_rect):
            self.bg_b_rect.y = self.bg_a_2_rect.y - self.vyska
            self.bg_a_rect.y = self.bg_a_2_rect.y + self.vyska
            print("tzu")

        self.y_bg_a = self.bg_a_rect.y
        self.y_bg_b = self.bg_b_rect.y
        self.y_bg_a_2 = self.bg_a_2_rect.y

        okno.blit(self.bg_a, (0, self.y_bg_a))
        okno.blit(self.bg_b, (0, self.y_bg_b))
        okno.blit(self.bg_a_2, (0, self.y_bg_a_2))
        okno.blit(self.bg_c, (0, self.y_bg_c))