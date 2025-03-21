import pygame
#pygame.init()

class Hrac:
    def __init__(self, pozice_hrace_x, pozice_hrace_y, rozliseni_x, rozliseni_y, okno, player_idle, player_moving, cooldown, pocet_ammo):
        self.pozice_hrace_x = pozice_hrace_x
        self.pozice_hrace_y = pozice_hrace_y

        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.okno = okno

        self.player_idle = player_idle
        self.player_moving = player_moving

        self.base_cooldown = cooldown
        self.cooldown_1 = cooldown
        self.cooldown_2 = cooldown
        self.pocet_ammo = pocet_ammo

        self.hrac_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)

    def pohni_se_klavesnice(self):
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

        self.hrac_rect = pygame.Rect(self.pozice_hrace_x, self. pozice_hrace_y, 47, 47)
            
        if self.movement:
            self.okno.blit(self.player_moving, (self.pozice_hrace_x, self.pozice_hrace_y))

        else:
            self.okno.blit(self.player_idle, (self.pozice_hrace_x, self.pozice_hrace_y))

    def pohni_se_mys(self, mys_x, mys_y):
        self.movement = False

        if self.pozice_hrace_y > mys_y and self.pozice_hrace_y > 0:
            self.movement = True
            self.pozice_hrace_y -= 4

        if self.pozice_hrace_y < mys_y and self.pozice_hrace_y < self.rozliseni_y - 30:
            self.movement = True
            self.pozice_hrace_y += 4

        if self.pozice_hrace_x > mys_x and self.pozice_hrace_x > 0:
            self.movement = True
            self.pozice_hrace_x -= 4

        if self.pozice_hrace_x < mys_x and self.pozice_hrace_x < self.rozliseni_x - 30:
            self.movement = True
            self.pozice_hrace_x += 4

        self.hrac_rect = pygame.Rect(self.pozice_hrace_x, self. pozice_hrace_y, 47, 47)
            
        if self.movement:
            self.okno.blit(self.player_moving, (self.pozice_hrace_x, self.pozice_hrace_y))

        else:
            self.okno.blit(self.player_idle, (self.pozice_hrace_x, self.pozice_hrace_y))

    def sniz_cooldown(self):
        self.cooldown_1 -= 1
        self.cooldown_2 -= 1

    def vystrel_1(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_1 <= 0 and self.pocet_ammo > 0:
            strela_1 = pygame.Rect(self.pozice_hrace_x + 7, self.pozice_hrace_y, 3, 5)
            self.cooldown_1 = self.base_cooldown
            self.pocet_ammo -= 1
            return strela_1
        
    def vystrel_2(self):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_SPACE] and self.cooldown_2 <= 0 and self.pocet_ammo > 0:
            strela_2 = pygame.Rect(self.pozice_hrace_x + 21, self.pozice_hrace_y, 3, 5)
            self.cooldown_2 = self.base_cooldown
            self.pocet_ammo -= 1
            return strela_2
        
    def vystrel_mys_1(self, udalosti):
        lmb = False

        for udalost in udalosti:
                if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
                    lmb = True

        mys_tlacitko = pygame.mouse.get_pressed()
        lmb = lmb or mys_tlacitko[0]

        if lmb and self.cooldown_1 <= 0 and self.pocet_ammo > 0:
            strela_1 = pygame.Rect(self.pozice_hrace_x + 7, self.pozice_hrace_y, 3, 5)
            self.cooldown_1 = self.base_cooldown
            self.pocet_ammo -= 1
            return strela_1
        
    def vystrel_mys_2(self, udalosti):
        lmb = False

        for udalost in udalosti:
                if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
                    lmb = True

        mys_tlacitko = pygame.mouse.get_pressed()
        lmb = lmb or mys_tlacitko[0]

        if lmb and self.cooldown_2 <= 0 and self.pocet_ammo > 0:
            strela_2 = pygame.Rect(self.pozice_hrace_x + 21, self.pozice_hrace_y, 3, 5)
            self.cooldown_2 = self.base_cooldown
            self.pocet_ammo -= 1
            return strela_2
        
    def pocet_naboju(self):
        return self.pocet_ammo
    
    def shop_kolize(self, shop_x, shop_y):
        for i in range(len(shop_y)):
            if self.hrac_rect.colliderect(pygame.Rect(shop_x, shop_y[i], 100, 100)):
                return True
        return False

    #enemy 1 kolize
    def checkni_kolizi_1_1(self, enemy_strela_1):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_strela_1)
    
    def checkni_kolizi_1_2(self, enemy_strela_2):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_strela_2)
    
    #enemy 2 kolize
    def checkni_kolizi_2_1(self, enemy_2_strela_1):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_2_strela_1)
    
    def checkni_kolizi_2_2(self, enemy_2_strela_2):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_2_strela_2)
    
    def checkni_kolizi_2_3(self, enemy_2_strela_3):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_2_strela_3)
    
    def checkni_kolizi_2_4(self, enemy_2_strela_4):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_2_strela_4)
    
    #enemy 3 kolize
    def checkni_kolizi_3_1(self, enemy_3_strela_1):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_1)
    
    def checkni_kolizi_3_2(self, enemy_3_strela_2):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_2)
    
    def checkni_kolizi_3_3(self, enemy_3_strela_3):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_3)
    
    def checkni_kolizi_3_4(self, enemy_3_strela_4):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_4)
    
    def checkni_kolizi_3_5(self, enemy_3_strela_5):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_5)
    
    def checkni_kolizi_3_6(self, enemy_3_strela_6):
        player_rect = pygame.Rect(self.pozice_hrace_x, self.pozice_hrace_y, 47, 47)
        return player_rect.colliderect(enemy_3_strela_6)