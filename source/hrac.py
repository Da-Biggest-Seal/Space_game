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
        self.pocet_ammo = 100
        self.strela_1 = pygame.Rect(self.pozice_hrace_x + 7, self.pozice_hrace_y, 3, 5)
        self.strela_2 = pygame.Rect(self.pozice_hrace_x + 21, self.pozice_hrace_y, 3, 5)

    def pohni_se(self):
        klavesa = pygame.key.get_pressed()

        self.movement = False

        if klavesa[pygame.K_w] and self.pozice_hrace_y > 0:
            self.movement = True
            self.pozice_hrace_y -= 4

        if klavesa[pygame.K_s] and self.pozice_hrace_y < self.rozliseni_y - 30:
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
            pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)

        else:
            self.okno.blit(self.player_idle, (self.pozice_hrace_x, self.pozice_hrace_y))
            pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)

    def sniz_cooldown(self):
        self.cooldown_1 -= 1
        self.cooldown_2 -= 1

    def vystrel_1(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_1 <= 0 and self.pocet_ammo > 0:
            self.strela_1
            self.cooldown_1 = 15
            self.pocet_ammo -= 1
            return self.strela_1
        
    def vystrel_2(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_2 <= 0 and self.pocet_ammo > 0:
            self.strela_2
            self.cooldown_2 = 15
            self.pocet_ammo -= 1
            return self.strela_2
        
    def pocet_naboju(self):
        return self.pocet_ammo
    
    def checkni_kolizi_1(self, enemy_strela_1):
        return self.strela_1.colliderect(enemy_strela_1[0], enemy_strela_1[1], enemy_strela_1[2], enemy_strela_1[3])
    
    def checkni_kolizi_2(self, enemy_strela_2):
        return self.strela_1.colliderect(enemy_strela_2[0], enemy_strela_2[1], enemy_strela_2[2], enemy_strela_2[3])