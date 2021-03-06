import pygame
import math


def quit_game(event, is_menu: bool) -> None:
    if is_menu:
        pygame.quit()
        exit("Mousebutton Exit")
    if event.type == pygame.QUIT:  # Click on X (top right corner)
        pygame.quit()
        exit("X Exit")


def game_over(player_hp: float,surface):
    if player_hp <= 0:
        player_hp = 0
        return player_hp


def is_wave_over(enemies) -> bool:
    """checks if round is over"""
    if len(enemies) == 0:
        return True
    else:
        return False


class Game:
    """Class to control Gameplay"""

    def __init__(self, window, width: int, height: int, wave: int):
        self.window = window
        self.width = width
        self.height = height
        self.wave = wave

    def draw_hud(self, money: int):
        playbutton = pygame.image.load("Assets/play.png")
        pausebutton = pygame.image.load("Assets/pause.png")
        restartbutton = pygame.image.load("Assets/restart.png")
        tower1_base = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
        tower1_head = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
        tower2_base = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Base.png")
        tower2_head = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Head.png")
        tower_base_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Base.png")
        tower_head_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Arm.png")
        gold_coin = pygame.image.load("Assets/UI/Icon_Coin.png")
        pygame.draw.rect(self.window, (65, 100, 190), ((0, self.height - 60), (self.width, 60)))
        self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
        self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
        self.window.blit(pygame.transform.scale(restartbutton,(60, 60)),(self.width - 180,self.height - 60))
        self.window.blit(pygame.transform.scale(tower1_base, (60, 60)), (0, self.height - 60))
        self.window.blit(pygame.transform.scale(tower1_head, (60, 60)), (0, self.height - 60))
        self.window.blit(pygame.transform.scale(tower2_base, (60, 60)), (60, self.height - 60))
        self.window.blit(pygame.transform.scale(tower2_head, (60, 60)), (60, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_base_3, (60, 60)), (120, self.height - 60))
        self.window.blit(pygame.transform.scale(tower_head_3, (40, 40)), (120, self.height - 60))
        self.window.blit(pygame.transform.scale(gold_coin, (60, 60)), (self.width - 240, self.height - 60))
        gold = pygame.font.SysFont('Comic Sans MS', 50)
        message_gold = gold.render(str(money), True, (255, 215, 0))
        self.window.blit(message_gold, (self.width - 400, self.height - 65))
        pygame.display.update()

    def draw_game_menu(self, depth_window: int, start_menu: bool) -> None:
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

    def main_menu(self, event, level: int) -> int:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return self.game_menu(False, level)
            else:
                return level
        else:
            return level

    def game_menu(self, start_menu: bool, level: int) -> int:
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

    def pause_round(self, event, mouse: tuple[int, int], money: int) -> tuple[bool, bool]:
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 60 <= mouse[0] <= self.width and self.height - 60 <= \
                mouse[1] <= self.height:  # Click on Pause
            self.draw_hud(money)
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 60, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
            return False, True
        else:
            return True, False

    def pause_round_after_go(self) :
            return False, True

    def start_round(self, event, mouse: tuple[int, int], money: int) -> tuple[bool, bool]:
        playbutton = pygame.image.load("Assets/play.png")
        if event.type == pygame.MOUSEBUTTONUP and self.width - 120 <= mouse[
            0] <= self.width - 60 and self.height - 60 <= mouse[1] <= self.height:  # Click on Play
            self.draw_hud(money)
            pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 120, self.height - 60), (60, 60)))
            self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
            return True, False
        else:
            return False, False

    # def game_over(self,player_hp: float, surface):
    #     if player_hp <= 0:
    #         # game_over_tag = pygame.image.load("Assets/game_over.png")
    #         # game_over_button = pygame.image.load("Assets/restart.png")
    #         # surface.blit(pygame.transform.scale(game_over_tag,(400,150)),(self.width -800,self.height- 600))
    #         # surface.blit(pygame.transform.scale(game_over_button,(400,150)),(self.width -800,self.height- 400))
    #         # pygame.display.update()
    #         # pygame.quit()
    #         # exit("Game over!")

    # def restart_game(self,event,mouse: tuple[int,int]:
    #     restart_button = pygame.image.load("Assets/restartpng.png")
    #     if event.type == pygame.MOUSEBUTTONDOWN and self.width - 180 <= mouse[
    #     if event.type == pygame.MOUSEBUTTONDOWN and self.width - 180 <= mouse[
    #         0] <= self.width - 60 and self.height - 60 <= mouse[1] <= self.height:

    def start_new_wave(self, number_of_enemies: int, enemy_speed_index: int, enemy_hp: float,restart) -> tuple[int, int, float, int,bool]:
        if restart == False:
            self.wave += 1
            number_of_enemies += 2
            if self.wave % 3 == 0 and enemy_speed_index < 9:
                enemy_speed_index += 1
            enemy_hp += 15
        else:
            self.wave = 1
            number_of_enemies = 6
        return number_of_enemies, enemy_speed_index, enemy_hp, self.wave

    def display_wave(self):
        color = (255, 255, 255)
        smallfont_current_wave = pygame.font.SysFont('Comic Sans MS', 34)
        current_wave_text = smallfont_current_wave.render('Wave ' + str(self.wave), True, color)
        self.window.blit(current_wave_text, (self.width - 182, 34))


    def create_tower(self, event, landscape, money: int, tower_positions: list) -> tuple[int]:
        mouse = pygame.mouse.get_pos()
        towers = []
        tower_price = 0
        tower_range = 0
        tower_damage = 0
        tower_base = None
        tower_head = None
        class_tower = 0
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and 0 <= mouse[0] <= 60 and 780 <= mouse[1] <= 840:
            tower_price = 100
            tower_range = 300
            tower_damage = 5
            tower_base = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
            tower_head = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
            class_tower = 0
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and 60 <= mouse[0] <= 120 and 780 <= mouse[
            1] <= 840:
            tower_price = 200
            tower_range = 200
            tower_damage = 10
            tower_base = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Base.png")
            tower_head = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Head.png")
            class_tower = 1
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and 120 <= mouse[0] <= 180 and 780 <= mouse[
            1] <= 840:
            tower_price = 300
            tower_range = 150
            tower_damage = 15
            tower_base = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Base.png")
            tower_head = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Arm.png")
            class_tower = 2
        chosen = True
        if tower_price != 0:
            while chosen:
                font = pygame.font.Font('freesansbold.ttf', 32)
                event_list = pygame.event.get()
                mouse_tower = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP:
                        if 780 <= mouse_tower[1] <= 840:  # if clicked on HUD
                            chosen = False  # toggle place tower off / break loop
                        elif money < tower_price:
                            error_message = font.render('keine Kohle mehr bro', True, (255, 0, 0))
                            self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                            pygame.display.update()
                            chosen = False
                            break
                        else:  # if clicked on map
                            mouse_landscape = mouse_tower
                            mouse_tower = list(mouse_tower)  # hier musss noch das Bild zentriert werden
                            position_x = (mouse_tower[0] % 60)
                            mouse_tower[0] -= ((position_x + 30) - 60)
                            position_y = (mouse_tower[1] % 60)
                            mouse_tower[1] -= ((position_y + 30) - 60)
                            mouse_tower = tuple(mouse_tower)
                            width, heigth = pygame.display.get_window_size()
                            pos_x = math.ceil((mouse_landscape[0] / width) * 20) - 1
                            pos_y = math.ceil((mouse_landscape[1] / heigth) * 14) - 1
                            if 2 <= landscape[pos_y][pos_x] <= 4:  # check if tower on sand
                                error_message = font.render('Error! Turm nicht auf Sand plazierbar!', True, (255, 0, 0))
                                self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                                pygame.display.update()
                            elif landscape[pos_y][pos_x] == 1:  # check if tower in water
                                error_message = font.render('Error! Turm nicht im Wasser plazierbar!', True,
                                                            (255, 0, 0))
                                self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                                pygame.display.update()
                            elif mouse_tower not in tower_positions:  # check if tower is already on position
                                pygame.draw.lines(self.window, (0, 255, 0), True, (
                                    (mouse_tower[0] - (tower_range - 55), mouse_tower[1] - (tower_range - 55)),
                                    (mouse_tower[0] - (tower_range - 55), mouse_tower[1] + (tower_range - 55)),
                                    (mouse_tower[0] + (tower_range - 55), mouse_tower[1] + (tower_range - 55)),
                                    (mouse_tower[0] + (tower_range - 55), mouse_tower[1] - (tower_range - 55))), 3)
                                money = money - tower_price
                                tower_position = mouse_tower
                                tower = tower_price, tower_range, tower_damage, tower_base, tower_head, class_tower, tower_position
                                towers.append(tower)
                                self.window.blit(pygame.transform.scale(tower_base, (60, 60)),
                                                 (mouse_tower[0] - 30, mouse_tower[1] - 30))
                                self.window.blit(pygame.transform.scale(tower_head, (60, 60)),
                                                 (mouse_tower[0] - 30, mouse_tower[1] - 30))
                                pygame.display.update()
                    elif events.type == pygame.KEYUP:
                        if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                            chosen = False  # toggle place tower off / break loop
                    quit_game(events, False)
            return towers, money
        else:
            return towers, money

    def sell_tower(self, event, mouse: tuple[int, int], round_started: bool, position: tuple[int, int], money:  int, sell_cost: int) -> tuple[int, bool]:
        tower_sold = False
        mouse_tower = mouse
        mouse_tower = list(mouse_tower)
        position_x = (mouse_tower[0] % 60)
        mouse_tower[0] -= ((position_x + 30) - 60)
        position_y = (mouse_tower[1] % 60)
        mouse_tower[1] -= ((position_y + 30) - 60)
        mouse_tower = tuple(mouse_tower)
        if event.type == pygame.MOUSEBUTTONDOWN and not round_started and mouse_tower == position and event.button == 3:
            sell = pygame.font.SysFont('Comic Sans MS', 20)
            message_sell = sell.render('SELL', True, (255, 0, 0))
            pygame.draw.rect(self.window, (65, 100, 190), ((mouse_tower[0], mouse_tower[1] + 5), (50, 20)))
            self.window.blit(message_sell, (mouse_tower[0], mouse_tower[1]))
            pygame.display.update()
            chosen = True
            while chosen:
                event_list = pygame.event.get()
                mouse_tower_2 = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP and events.button == 1:
                        if 780 <= mouse_tower_2[1] <= 840:  # if clicked on HUD
                            return money, tower_sold  # toggle place tower off / break loop
                        elif mouse_tower[0] <= mouse_tower_2[0] <= mouse_tower[0] + 50 and mouse_tower[1] + 5 <= \
                                mouse_tower_2[1] <= mouse_tower[1] + 20:
                            cross = pygame.image.load("Assets/cross.png")
                            self.window.blit(pygame.transform.scale(cross, (60, 60)),
                                             (mouse_tower[0] - 30, mouse_tower[1] - 30))
                            pygame.display.update()
                            money = money + sell_cost
                            tower_sold = True
                            return money, tower_sold
                    elif events.type == pygame.KEYUP:
                        if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                            return money, tower_sold  # toggle place tower off / break loop
                    quit_game(events, False)
        return money, tower_sold
