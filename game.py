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
        pygame.draw.rect(self.window, (65, 100, 190), ((0, self.height - 60), (self.width, 60)))
        self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
        self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))

    def draw_game_menu(self):
        pygame.draw.rect(self.window, (65, 100, 190),
                         ((0, 0), (240, 252)))  # background  for Buttons
        color = (255, 255, 255)
        smallfont_main_menu = pygame.font.SysFont('Comic Sans MS', 44)
        main_menu_text = smallfont_main_menu.render('Main Menu', True, color)
        smallfont_options = pygame.font.SysFont('Comic Sans MS', 56)
        options_text = smallfont_options.render('Options', True, color)
        self.window.blit(options_text, (15, 20))
        self.window.blit(main_menu_text, (10, self.height - 230))
        exitbutton = pygame.image.load("Assets/UI/exit_btn.png")
        self.window.blit(pygame.transform.scale(exitbutton, (240, 126)), (0, self.height - 126))
        pygame.display.update()

    def update_hud(self):
        pass

    def main_menu(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                exitbutton = pygame.image.load("Assets/UI/exit_btn.png")
                self.window.blit(pygame.transform.scale(exitbutton, (240, 126)), (self.width / 2 - 120, self.height / 2 - 63))
                pygame.display.update()
                running = True
                while running:  # Loop for menu
                    event_lists = pygame.event.get()
                    mouse_menu = pygame.mouse.get_pos()  # extra mousetracking (for menu)
                    for events in event_lists:
                        if events.type == pygame.MOUSEBUTTONUP:
                            if self.width / 2 - 120 <= mouse_menu[0] <= self.width / 2 + 120 and self.height / 2 - 63 <= mouse_menu[1] <= self.height / 2 + 63:  # Click on Quit
                                self.quit_game(events, True)
                        elif events.type == pygame.KEYUP:
                            if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                                running = False  # break loop

    def game_menu(self):
        self.draw_game_menu()
        running = True
        while running:
            event_list = pygame.event.get()
            mouse = pygame.mouse.get_pos()
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if 0 <= mouse[0] <= 240 and 252 <= mouse[1] <= self.height:  # Click on Quit
                        self.quit_game(event, True)
                    elif 0 <= mouse[0] <= 240 and 126 <= mouse[1] <= 252:  # Click on Main Menu
                        window_height = 840
                        window_width = 1200
                        return window_width, window_height
                    elif 0 <= mouse[0] <= 240 and 0 <= mouse[1] <= 126:  # Click on Options
                        window_height = 840
                        window_width = 1200
                        return window_width, window_height
                self.quit_game(event, False)

    def pause_game(self, event, mouse):
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Pause
            if self.width - 60 <= mouse[0] <= self.width and self.height - 60 <= mouse[1] <= self.height:
                self.draw_hud()
                pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 60, self.height - 60), (60, 60)))
                self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))

    def quit_game(self, event, is_menu):
        if is_menu:
            pygame.quit()
            exit("Mousebutton Exit")
        if event.type == pygame.QUIT:  # Click on X (top right corner)
            pygame.quit()
            exit("X Exit")

    def start_round(self, event, mouse):
        playbutton = pygame.image.load("Assets/play.png")
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Play
            if self.width - 120 <= mouse[0] <= self.width - 60 and self.height - 60 <= mouse[1] <= self.height:
                self.draw_hud()
                pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 120, self.height - 60), (60, 60)))
                self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))
                self.timer(True)

    def timer(self, start):
        smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        color = (255, 255, 255)
        if start:
            global start_time
            start_time = pygame.time.get_ticks()
        try:
            passed_time = pygame.time.get_ticks() - start_time
            timer = smallfont.render(str(passed_time / 1000)+' s', True, color)
            self.window.blit(timer, (self.width - 110, -5))
        except:
            no_timer = smallfont.render('no timer', True, color)
            self.window.blit(no_timer, (self.width - 120, -5))