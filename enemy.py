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
        pygame.Rect(self.pozice_enemy_x, self.pozice_enemy_y, 47, 47)