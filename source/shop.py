import pygame

class Shop:
    def __init__(self, shop_img, shop_gui_0, shop_gui_1, shop_gui_2, shop_gui_3, shop_gui_4, shop_x, shop_y, okno, pozice_hrace_y, rozliseni_x, rozliseni_y, Recty_shopu):
        self.shop_png = shop_img
        self.shop_gui_0 = shop_gui_0
        self.shop_gui_1 = shop_gui_1
        self.shop_gui_2 = shop_gui_2
        self.shop_gui_3 = shop_gui_3
        self.shop_gui_4 = shop_gui_4
        self.shop_x = shop_x
        self.shop_y = shop_y
        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y
        self.y_bg_c = 0
        self.okno = okno
        self.Recty_shopu = Recty_shopu
        self.okno = okno

    def vykresli_se(self):

        for i in range(len(self.shop_y)):
            self.okno.blit(self.shop_png, (self.shop_x, self.shop_y[i]))
            self.Recty_shopu.append(pygame.Rect(self.shop_x, self.shop_y[i], 100, 100))

            if self.pozice_hrace_y <= 200:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] += 1

            if self.pozice_hrace_y >= self.rozliseni_y - 150:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] -= 1

    def otevri_se(self, hrac):
        klavesa = pygame.key.get_pressed()

        if klavesa[pygame.K_TAB] and hrac.shop_kolize(self.shop_x, self.shop_y) == True:
            self.okno.blit(self.shop_gui_0, (100, 100))