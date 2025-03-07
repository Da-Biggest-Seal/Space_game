import pygame
#pygame.init()

class Shop:
    def __init__(self, shop_img, shop_x, shop_y, okno, pozice_hrace_y, rozliseni_y):
        self.shop_png = shop_img
        self.shop_x = shop_x
        self.shop_y = shop_y
        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_y = rozliseni_y
        self.y_bg_c = 0
        self.okno = okno

    def vykresli_se(self):
        klavesa = pygame.key.get_pressed()

        self.Recty_shopu = []

        for i in range(len(self.shop_y)):
            self.okno.blit(self.shop_png, (self.shop_x, self.shop_y[i]))
            self.Recty_shopu.append(pygame.Rect(self.shop_x, self.shop_y[i], 100, 100))

        if klavesa[pygame.K_w] and self.pozice_hrace_y > 0:
            self.pozice_hrace_y -= 4

            if self.pozice_hrace_y <= 200:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] += 4
        
        if klavesa[pygame.K_s] and self.pozice_hrace_y < self.rozliseni_y - 30:
            self.pozice_hrace_y += 4

            if self.pozice_hrace_y >= self.rozliseni_y - 150:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] -= 4

        print(self.shop_y)
        print(self.pozice_hrace_y)