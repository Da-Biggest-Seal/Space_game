import pygame

class Shop:
    def __init__(self, shop_img, shop_gui_0, shop_gui_1, shop_gui_2, shop_gui_3, shop_gui_4, shop_x, shop_y, pozice_hrace_y, rozliseni_x, rozliseni_y, Recty_shopu, font, list_enemy_1, list_enemy_2, list_enemy_3):
        self.shop_png = shop_img
        self.shop_gui_0 = shop_gui_0
        self.shop_gui_1 = shop_gui_1
        self.shop_gui_2 = shop_gui_2
        self.shop_gui_3 = shop_gui_3
        self.shop_gui_4 = shop_gui_4

        self.shop_x = shop_x
        self.shop_y = shop_y

        self.enemy_1 = list_enemy_1
        self.enemy_2 = list_enemy_2
        self.enemy_3 = list_enemy_3

        self.bila = (255, 255, 255)
        self.cervena = (255, 0, 0)

        self.pozice_hrace_y = pozice_hrace_y
        self.rozliseni_x = rozliseni_x
        self.rozliseni_y = rozliseni_y

        self.y_bg_c = 0
        self.Recty_shopu = Recty_shopu
        self.font = font
        self.text_timer = 0
        self.text_nakup = None
        self.zakoupeno_cooldown = 0

    def vykresli_se(self, okno):
        self.Recty_shopu.clear()

        encounter = False

        if self.enemy_1[1]:
            if min(self.enemy_1[1]) >= 0:
                encounter = True

        if self.enemy_2[1]:
            if min(self.enemy_2[1]) >= 0:
                encounter = True

        if self.enemy_3[1]:
            if min(self.enemy_3[1]) >= 0:
                encounter = True

        for i in range(len(self.shop_y)):
            okno.blit(self.shop_png, (self.shop_x, self.shop_y[i]))
            self.Recty_shopu.append(pygame.Rect(self.shop_x, self.shop_y[i], 100, 100))

            if self.pozice_hrace_y <= 200 and encounter == False:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] += 1

            if self.pozice_hrace_y >= self.rozliseni_y - 150 and encounter == False:
                for i in range(len(self.shop_y)):
                    self.shop_y[i] -= 1

    def otevri_se(self, hrac, okno, udalosti, money, hrac_hity, pocet_ammo, cooldown, damage):
        klavesa = pygame.key.get_pressed()
        mys = pygame.mouse.get_pos()
        rmb = False
        rudium = money

        pozadovane_money_1 = 3
        pozadovane_money_2 = 1 * hrac_hity
        pozadovane_money_3 = 6
        pozadovane_money_4 = 6

        if klavesa[pygame.K_TAB] and hrac.shop_kolize(self.shop_x, self.shop_y) == True:

            for udalost in udalosti:
                if udalost.type == pygame.MOUSEBUTTONUP and udalost.button == 3:
                    rmb = True

            self.stav = 0

            self.button_1_rect = pygame.Rect(317, 122, 137, 135)
            self.button_3_rect = pygame.Rect(317, 315, 137, 137)
            self.button_2_rect = pygame.Rect(519, 124, 134, 133)
            self.button_4_rect = pygame.Rect(519, 315, 134, 138)

            if rmb:

                #ammo
                #dost penez
                if self.button_1_rect.collidepoint(mys):
                    if pozadovane_money_1 <= rudium:
                        rudium -= 3
                        pocet_ammo += 10

                        self.text_nakup = self.font.render("Zakoupeno: +10 Ammo", True, self.bila)
                        self.text_timer = 30

                #malo penez
                    else:
                        self.text_nakup = self.font.render("Nedostatek Rudia", True, self.bila)
                        self.text_timer = 30

                #hp
                #dost penez
                elif self.button_2_rect.collidepoint(mys):
                    if pozadovane_money_2 <= rudium and hrac_hity != 0:
                        rudium -= pozadovane_money_2
                        hrac_hity = 0

                        self.text_nakup = self.font.render("Zakoupeno: Repair", True, self.bila)
                        self.text_timer = 30

                #full hp
                    elif hrac_hity == 0:
                        self.text_nakup = self.font.render("Není potřeba opravit!", True, self.bila)
                        self.text_timer = 30

                #malo penez    
                    else:
                        self.text_nakup = self.font.render("Nedostatek Rudia", True, self.bila)
                        self.text_timer = 30

                #fire rate
                #dost penez
                elif self.button_3_rect.collidepoint(mys):
                    if pozadovane_money_3 <= rudium and self.zakoupeno_cooldown < 5:
                        rudium -= 6
                        cooldown -= 3
                        self.zakoupeno_cooldown += 1

                        self.text_nakup = self.font.render("Zakoupeno: +1 Fire Rate", True, self.bila)
                        self.text_timer = 30

                #moc upgrade
                    elif self.zakoupeno_cooldown >= 5:
                        self.text_nakup = self.font.render("Zakoupeno až moc tohoto upgradu", True, self.bila)
                        self.text_timer = 30

                #malo penez
                    elif rudium < pozadovane_money_3:
                        self.text_nakup = self.font.render("Nedostatek Rudia", True, self.bila)
                        self.text_timer = 30

                #damage
                #dost penez
                elif self.button_4_rect.collidepoint(mys):
                    if pozadovane_money_4 <= rudium:
                        rudium -= 6
                        damage += 1/2

                        self.text_nakup = self.font.render("Zakoupeno: +0.5 Damage", True, self.bila)
                        self.text_timer = 30

                #malo penez
                    else:
                        self.text_nakup = self.font.render("Nedostatek Rudia", True, self.bila)
                        self.text_timer = 30

            if self.button_1_rect.collidepoint(mys):
                self.stav = 1

            if self.button_2_rect.collidepoint(mys):
                self.stav = 2

            if self.button_3_rect.collidepoint(mys):
                self.stav = 3

            if self.button_4_rect.collidepoint(mys):
                self.stav = 4



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

            cena_repair_text = self.font.render(str(pozadovane_money_2), True, self.cervena)
            cena_repair_text_rect = cena_repair_text.get_rect(center= (532, 218))
            okno.blit(cena_repair_text, cena_repair_text_rect)

            if hasattr(self, 'text_timer') and self.text_timer > 0:
                self.text_timer -= 1

                if self.text_timer >= 0:
                    text_nakup_rect = self.text_nakup.get_rect(center= (224, 479))
                    okno.blit(self.text_nakup, text_nakup_rect)

            return rudium, pocet_ammo, hrac_hity, cooldown, damage