import random
import pygame
pygame.init()

class Enemy:
    def __init__(self, pozice_enemy_x, pozice_enemy_y, rozliseni_x, rozliseni_y, okno, enemy_idle):
        self.pozice_enemy_x = pozice_enemy_x
        self.pozice_enemy_y = pozice_enemy_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno
        self.enemy_idle = enemy_idle

    def vykresli_se(self):
        self.okno.blit(self.enemy_idle, (self.pozice_enemy_x, self.pozice_enemy_y))
        self.Rect = pygame.Rect(self.pozice_enemy_x, self.pozice_enemy_y, 47, 47)

    def checkni_kolizi_1(self, strela_1):
        return self.Rect.colliderect((strela_1[0], strela_1[1], strela_1[2], strela_1[3]))
    
    def checkni_kolizi_2(self, strela_2):
        return self.Rect.colliderect((strela_2[0], strela_2[1], strela_2[2], strela_2[3]))