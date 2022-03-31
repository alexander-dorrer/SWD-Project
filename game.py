import pygame


def quit_game(event, is_menu):
    if is_menu:
        pygame.quit()
        exit("Mousebutton Exit")
    if event.type == pygame.QUIT:  # Click on X (top right corner)
        pygame.quit()
        exit("X Exit")


def game_over(player_hp):
    if player_hp <= 0:
        pygame.quit()
        exit("Game over!")


class Game:
    """Class to control Gameplay"""

    def __init__(self, window, width, height, wave):
        self.window = window
        self.width = width
        self.height = height
        self.wave = wave

    def draw_hud(self, money):
        playbutton = pygame.image.load("Assets/play.png")
        pausebutton = pygame.image.load("Assets/pause.png")
        tower1_base = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
        tower1_head = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
        tower2_base = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Base.png")
        tower2_head = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Head.png")
        tower2_arm = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Arm.png")
        tower_base_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Base.png")
        tower_head_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Arm.png")
        pygame.draw.rect(self.window, (65, 100, 190), ((0, self.height - 60), (self.width, 60)))
        self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
        self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
        self.window.blit(pygame.transform.scale(tower1_base, (60, 60)), (0, self.height - 60))
        self.window.blit(pygame.transform.scale(tower1_head, (60, 60)), (0, self.height - 60))
        self.window.blit(pygame.transform.scale(tower2_base, (60, 60)), (60, self.height - 60))
        self.window.blit(pygame.transform.scale(tower2_head, (60, 60)), (60, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_base_3, (60, 60)), (120, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_head_3, (40, 40)), (120, self.height - 60))
        gold = pygame.font.SysFont('Comic Sans MS', 50)
        message_gold = gold.render(str(int(money)) + ' G', True, (255, 215, 0))
        self.window.blit(message_gold, (75, self.height - 65))
        pygame.display.update()

    def draw_game_menu(self, depth_window, start_menu):
        if start_menu:
            pygame.draw.rect(self.window, (65, 100, 190),
                             ((0, 0), (self.width, self.height)))  # Full screen blue
        if depth_window == 1:
            pygame.draw.rect(self.window, (0, 0, 0),
                             ((self.width / 2 - 120, self.height / 2 - 63), (240, 126)))  # border Main Menu
            pygame.draw.rect(self.window, (65, 100, 190),
                             ((self.width / 2 - 118, self.height / 2 - 62), (236, 124)))  # blue of Main Menu
            color = (255, 255, 255)
            smallfont_main_menu = pygame.font.SysFont('Comic Sans MS', 44)
            main_menu_text = smallfont_main_menu.render('Main Menu', True, color)
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

    def main_menu(self, event, level):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return self.game_menu(False, level)
            else:
                return level
        else:
            return level

    def game_menu(self, start_menu, level):
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
                            quit_game(event, True)
                        elif self.width / 2 - 120 <= mouse[0] <= self.width / 2 + 120 and self.height / 2 - 63 <= mouse[
                            1] <= self.height / 2 + 63:  # Click on Main Menu
                            running = 'level choice'
                            self.draw_game_menu(2, start_menu)
                        elif self.width / 2 - 120 <= mouse[0] <= self.width / 2 + 120 and self.height / 2 - 189 <= \
                                mouse[1] <= self.height / 2 - 63:  # Click on Start
                            return level
                        else:
                            return level
                    elif event.type == pygame.KEYUP and not start_menu:
                        if event.key == pygame.K_ESCAPE:  # Esc. is pressed
                            return level
                    quit_game(event, False)
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
                                return levels
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:  # Esc. is pressed
                            running = 'main menu'  # break loop
                            self.draw_game_menu(1, start_menu)
                    quit_game(event, False)

    def pause_round(self, event, mouse, money):
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 60 <= mouse[0] <= self.width and self.height - 60 <= \
                mouse[1] <= self.height:  # Click on Pause
            self.draw_hud(money)
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 60, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
            return False, True
        else:
            return True, False

    def start_round(self, event, mouse, money):
        playbutton = pygame.image.load("Assets/play.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 120 <= mouse[
            0] <= self.width - 60 and self.height - 60 <= mouse[1] <= self.height:  # Click on Play
            self.draw_hud(money)
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 120, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
            return True, False
        else:
            return False, False

    def is_wave_over(self, enemies):
        """checks if round is over"""
        if len(enemies) == 0:
            return True
        else:
            return False

    def start_new_wave(self, number_of_enemies, enemy_speed_index, enemy_hp):
        self.wave += 1
        number_of_enemies += 1
        if self.wave % 3 == 0 and enemy_speed_index <= 9:
            enemy_speed_index += 1
        enemy_hp += 10
        return number_of_enemies, enemy_speed_index, enemy_hp, self.wave

    def display_wave(self):
        color = (255, 255, 255)
        smallfont_current_wave = pygame.font.SysFont('Comic Sans MS', 34)
        current_wave_text = smallfont_current_wave.render('Wave: ' + str(self.wave), True, color)
        self.window.blit(current_wave_text, (10, 0))
