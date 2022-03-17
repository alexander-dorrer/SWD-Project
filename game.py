import pygame


class Game:
    """Class to control Gameplay"""

    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw_hud(self):
        playbutton = pygame.image.load("Assets/play.png")
        pausebutton = pygame.image.load("Assets/pause.png")
        tower_base = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
        tower_head = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
        pygame.draw.rect(self.window, (65, 100, 190), ((0, self.height - 60), (self.width, 60)))
        self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
        self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_base, (60, 60)), (0, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_head, (60, 60)), (0, self.height - 60))

    def draw_game_menu(self, depth_window, start_menu):
        if start_menu:
            pygame.draw.rect(self.window, (65, 100, 190),
                             ((0, 0), (self.width, self.height)))  # Full screen blue
        if depth_window == 1:
            # pygame.draw.rect(self.window, (0, 0, 0),
            #                  ((self.width / 2 - 120, self.height / 2 - 189), (240, 126)))   # border Options
            pygame.draw.rect(self.window, (0, 0, 0),
                             ((self.width / 2 - 120, self.height / 2 - 63), (240, 126)))  # border Main Menu
            # pygame.draw.rect(self.window, (65, 100, 190),
            #                  ((self.width / 2 - 118, self.height / 2 - 187), (236, 124)))   # blue of Options
            pygame.draw.rect(self.window, (65, 100, 190),
                             ((self.width / 2 - 118, self.height / 2 - 62), (236, 124)))  # blue of Main Menu
            color = (255, 255, 255)
            smallfont_main_menu = pygame.font.SysFont('Comic Sans MS', 44)
            main_menu_text = smallfont_main_menu.render('Main Menu', True, color)
            # smallfont_options = pygame.font.SysFont('Comic Sans MS', 56)
            # options_text = smallfont_options.render('Options', True, color)
            # self.window.blit(options_text,
            #                  (self.width / 2 - 120 + 10, self.height / 2 - 189 + 15))  # Options Button Text
            startbutton = pygame.image.load("Assets/UI/start_btn.png")
            self.window.blit(pygame.transform.scale(startbutton, (240, 378 / 3)),
                             (self.width / 2 - 120, self.height / 2 - 189))
            self.window.blit(main_menu_text, (self.width / 2 - 120 + 10, self.height / 2 - 63 + 20))  # Main Menu Text
            exitbutton = pygame.image.load("Assets/UI/exit_btn.png")
            self.window.blit(pygame.transform.scale(exitbutton, (240, 378 / 3)),
                             (self.width / 2 - 120, self.height / 2 + 63))
            pygame.display.update()
        elif depth_window == 2:
            pygame.draw.rect(self.window, (0, 0, 0),
                             ((self.width / 2 - 120, self.height / 2 - 189),
                              (240, 3 * 126)))  # border for level choice
            pygame.draw.rect(self.window, (65, 100, 190),
                             ((self.width / 2 - 118, self.height / 2 - 187),
                              (236, 375)))  # background for level choice
            color = (255, 255, 255)
            smallfont_size_menu = pygame.font.SysFont('Comic Sans MS', 30)
            size_menu_text = smallfont_size_menu.render('Level Choice!', True, color)
            self.window.blit(size_menu_text, (self.width / 2 - 120 + 10, self.height / 2 - 189 + 15))
            for levels in range(6):  # levels choice print (6 levels example)
                smallfont = pygame.font.SysFont('Comic Sans MS', 30)
                text = smallfont.render('Level ' + str(levels + 1), True, color)
                self.window.blit(text, (self.width / 2 - 120 + 10, self.height / 2 - 126 + levels / 6 * 315))
            pygame.display.update()

    def update_hud(self):
        pass

    def main_menu(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.game_menu(False)

    def game_menu(self, start_menu):
        self.draw_game_menu(1, start_menu)
        menu = True
        running = 'main menu'
        while menu:
            while running == 'main menu':  # main game menu
                event_list = pygame.event.get()
                mouse = pygame.mouse.get_pos()
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.width / 2 - 120 <= mouse[0] <= self.width / 2 + 120 and self.height / 2 + 63 <= mouse[
                            1] <= self.height / 2 + 189:  # Click on Quit
                            self.quit_game(event, True)
                        elif self.width / 2 - 120 <= mouse[0] <= self.width / 2 + 120 and self.height / 2 - 63 <= mouse[
                            1] <= self.height / 2 + 63:  # Click on Main Menu
                            running = 'level choice'
                            self.draw_game_menu(2, start_menu)
                        elif self.width / 2 - 120 <= mouse[0] <= self.width / 2 + 120 and self.height / 2 - 189 <= \
                                mouse[1] <= self.height / 2 - 63:  # Click on Options
                            return
                    elif event.type == pygame.KEYUP and not start_menu:
                        if event.key == pygame.K_ESCAPE:  # Esc. is pressed
                            running = ''  # break loop
                            menu = False
                    self.quit_game(event, False)
            while running == 'level choice':  # levels choice menu
                event_list = pygame.event.get()
                mouse = pygame.mouse.get_pos()
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        for levels in range(6):
                            if self.width / 2 - 120 <= mouse[
                                0] <= self.width / 2 + 120 and self.height / 2 - 126 + levels / 6 * 315 <= mouse[
                                1] <= self.height / 2 - 126 + (levels + 1) / 6 * 315:  # Click on level
                                ########################################
                                # implement actions on choice of level #
                                ########################################
                                running = ''
                                menu = False
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:  # Esc. is pressed
                            running = 'main menu'  # break loop
                            self.draw_game_menu(1, start_menu)
                    self.quit_game(event, False)

    def pause_round(self, event, mouse):
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 60 <= mouse[0] <= self.width and self.height - 60 <= mouse[1] <= self.height:  # Click on Pause
            self.draw_hud()
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 60, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
            return False, True
        else:
            return True, False

    def quit_game(self, event, is_menu):
        if is_menu:
            pygame.quit()
            exit("Mousebutton Exit")
        if event.type == pygame.QUIT:  # Click on X (top right corner)
            pygame.quit()
            exit("X Exit")

    def start_round(self, event, mouse):
        playbutton = pygame.image.load("Assets/play.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 120 <= mouse[0] <= self.width - 60 and self.height - 60 <= mouse[1] <= self.height:      # Click on Play
            self.draw_hud()
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 120, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
            return True, False
        else:
            return False, False
