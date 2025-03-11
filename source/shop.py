import pygame

class Shop:
    def __init__(self, shop_img, shop_gui_0, shop_gui_1, shop_gui_2, shop_gui_3, shop_gui_4, shop_x, shop_y, bila, okno, pozice_hrace_y, rozliseni_x, rozliseni_y, Recty_shopu, font):
        self.shop_png = shop_img
        self.shop_gui_0 = shop_gui_0
        self.shop_gui_1 = shop_gui_1
        self.shop_gui_2 = shop_gui_2
        self.shop_gui_3 = shop_gui_3
        self.shop_gui_4 = shop_gui_4

        self.shop_x = shop_x
        self.shop_y = shop_y

        self.bila = (255, 255, 255)
        self.okno = okno

        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y

        self.y_bg_c = 0
        self.Recty_shopu = Recty_shopu
        self.font = font

    def vykresli_se(self, okno):
        self.Recty_shopu.clear()

        for i in range(len(self.shop_y)):
            okno.blit(self.shop_png, (self.shop_x, self.shop_y[i]))
            self.Recty_shopu.append(pygame.Rect(self.shop_x, self.shop_y[i], 100, 100))

            if self.pozice_hrace_y <= 200:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] += 1

            if self.pozice_hrace_y >= self.rozliseni_y - 150:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] -= 1

    def otevri_se(self, hrac, okno):
        klavesa = pygame.key.get_pressed()
        mys = pygame.mouse.get_pos()
        rmb = False
        text_rmb = False
        text_nakup = self.font.render("", True, self.bila)

        if klavesa[pygame.K_TAB] and hrac.shop_kolize(self.shop_x, self.shop_y) == True:
            self.stav = 0

            self.button_1_rect = pygame.Rect(317, 122, 137, 135)
            self.button_3_rect = pygame.Rect(317, 315, 137, 137)
            self.button_2_rect = pygame.Rect(519, 124, 134, 133)
            self.button_4_rect = pygame.Rect(519, 315, 134, 138)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        rmb = True

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        text_rmb = True

            if self.button_1_rect.collidepoint(mys):
                self.stav = 1
                if rmb:
                    pass

                if text_rmb:
                    text_nakup = self.font.render("Zakoupeno: +10 Ammo", True, self.bila)

            if self.button_2_rect.collidepoint(mys):
                self.stav = 2
                if rmb:
                    pass

                if text_rmb:
                    text_nakup = self.font.render("Zakoupeno: Repair", True, self.bila)
                
            if self.button_3_rect.collidepoint(mys):
                self.stav = 3
                if rmb:
                    pass

                if text_rmb:
                    text_nakup = self.font.render("Zakoupeno: +1 Fire Rate", True, self.bila)

            if self.button_4_rect.collidepoint(mys):
                self.stav = 4
                if rmb:
                    pass

                if text_rmb:
                    text_nakup = self.font.render("Zakoupeno: +0,5 Damage", True, self.bila)

            

            if self.stav == 0:
                okno.blit(self.shop_gui_0, (100, 100))

            if self.stav == 1:
                okno.blit(self.shop_gui_1, (100, 100))

            if self.stav == 2:
                okno.blit(self.shop_gui_2, (100, 100))

            if self.stav == 3:
                okno.blit(self.shop_gui_3, (100, 100))

            if self.stav == 4:
                okno.blit(self.shop_gui_4, (100, 100))

            if self.button_1_rect.collidepoint(mys) or self.button_2_rect.collidepoint(mys) or self.button_3_rect.collidepoint(mys) or self.button_4_rect.collidepoint(mys) and text_rmb:
                text_nakup_rect = text_nakup.get_rect(center= (134, 459))
                okno.blit(text_nakup, text_nakup_rect)