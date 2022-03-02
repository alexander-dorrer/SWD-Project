import pygame
from map import level1

class Game:
    """Class to control Gameplay"""
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw_map(self):
        grass_tile = pygame.image.load("Assets/grass_tile.png")
        sand_tile = pygame.image.load("Assets/sand_tile.png")
        water_tile = pygame.image.load("Assets/water_tile.png")
        enemy_goal = pygame.image.load('Assets/Towers&Projectiles/Tower_12/Tower_12.png')
        current_row = -1
        for row in level1:
            current_row += 1
            current_tile = 0
            for tile in row:
                if tile == 0:
                    self.window.blit(pygame.transform.scale(grass_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1
                elif tile == 1:
                    self.window.blit(pygame.transform.scale(water_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1
                elif tile == 4:
                    self.window.blit(pygame.transform.scale(sand_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    self.window.blit(pygame.transform.scale(enemy_goal, (65, 65)), (current_tile * 70, current_row * 70))
                else:
                    self.window.blit(pygame.transform.scale(sand_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1

    def draw_hud(self):
        playbutton = pygame.image.load("Assets/play.png")
        pausebutton = pygame.image.load("Assets/pause.png")
        pygame.draw.rect(self.window, (65, 100, 190), ((0, self.height - 60), (self.width, 60)))
        self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))
        self.window.blit(pygame.transform.scale(playbutton, (60, 60)), (self.width - 120, self.height - 60))

    def update_hud(self):
        pass

    def main_menu(self, event):
        color = (255, 255, 255)
        smallfont = pygame.font.SysFont('Comic Sans MS', 30)
        text = smallfont.render('Quit', True, color)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.draw.rect(self.window, (65, 100, 190), ((self.width / 2 - 36, self.height / 2 - 22), (72, 40)))  # background  for Quit-Button
                self.window.blit(text, (self.width / 2 - 32, self.height / 2 - 26))
                pygame.display.update()
                running = True
                while running:  # Loop for menu
                    event_lists = pygame.event.get()
                    mouse_menu = pygame.mouse.get_pos()  # extra mousetracking (for menu)
                    for events in event_lists:
                        if events.type == pygame.MOUSEBUTTONUP:
                            Game.quit_game(self, mouse_menu, events, True)
                        elif events.type == pygame.KEYUP:
                            if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                                running = False  # break loop
                                Game.draw_map(self)
                                pygame.display.update()

    def pause_game(self, event, mouse):
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Pause
            if self.width - 60 <= mouse[0] <= self.width and self.height - 60 <= mouse[1] <= self.height:
                self.draw_hud()
                pygame.draw.rect(self.window, (64, 191, 81), ((self.width - 60, self.height - 60), (60, 60)))
                self.window.blit(pygame.transform.scale(pausebutton, (60, 60)), (self.width - 60, self.height - 60))

    def quit_game(self, mouse_menu, event, is_menu):
        if is_menu:
            if self.width / 2 - 36 <= mouse_menu[0] <= self.width / 2 + 36 and self.height / 2 - 26 <= mouse_menu[1] <= self.height / 2 + 14:   # Click on Quit
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
            Game.draw_map(self)
            self.window.blit(timer, (self.width - 110, -5))
        except:
            no_timer = smallfont.render('no timer', True, color)
            self.window.blit(no_timer, (self.width - 120, -5))