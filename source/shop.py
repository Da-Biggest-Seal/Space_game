import pygame
pygame.init()

class Shop:
    def __init__(self, shop, shop_x, shop_y, okno):
        self.shop_png = shop
        self.shop_x = shop_x
        self.shop_y = shop_y
        self.okno = okno

    def vykresli_se(self):
        klavesa = pygame.key.get_pressed()

        self.Recty_shopu = []

        for i in range(len(self.shop_y)):
            self.okno.blit(self.shop_png, (self.shop_x, self.shop_y[i]))
            self.Recty_shopu.append(pygame.Rect(self.shop_x, self.shop_y[i], 100, 100))

            if klavesa[pygame.K_q]:
                self.shop_y[i] += 4

            if klavesa[pygame.K_e]:
                self.shop_y[i] -= 4