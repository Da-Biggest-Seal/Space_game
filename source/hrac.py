import pygame
pygame.init()

class Hrac:
    def __init__(self, pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown):
        self.pozice_hrace_x = pozice_hrace_x
        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno
        self.player_idle = player_idle
        self.player_moving = player_moving
        self.cooldown_1 = cooldown
        self.cooldown_2 = cooldown

    def pohni_se(self):
        klavesa = pygame.key.get_pressed()

        self.movement = False

        if klavesa[pygame.K_w]:
            self.movement = True
            self.pozice_hrace_y -= 4

        if klavesa[pygame.K_s]:
            self.movement = True
            self.pozice_hrace_y += 4

        if klavesa[pygame.K_a] and self.pozice_hrace_x > 0:
            self.movement = True
            self.pozice_hrace_x -= 4

        if klavesa[pygame.K_d] and self.pozice_hrace_x < self.rozliseni_x - 30:
            self.movement = True
            self.pozice_hrace_x += 4
            
        if self.movement:
            self.okno.blit(self.player_moving, (self.pozice_hrace_x, self.pozice_hrace_y))

        else:
            self.okno.blit(self.player_idle, (self.pozice_hrace_x, self.pozice_hrace_y))

    def sniz_cooldown(self):
        self.cooldown_1 -= 1
        self.cooldown_2 -= 1

    def vystrel_1(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_1 <= 0:
            strela_1 = pygame.Rect(self.pozice_hrace_x + 7, self.pozice_hrace_y, 3, 5)
            self.cooldown_1 = 15
            return strela_1
        
    def vystrel_2(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_2 <= 0:
            strela_2 = pygame.Rect(self.pozice_hrace_x + 21, self.pozice_hrace_y, 3, 5)
            self.cooldown_2 = 15
            return strela_2