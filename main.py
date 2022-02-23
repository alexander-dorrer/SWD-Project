import pygame
from map import level1

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 970
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """Class to control Gameplay"""
    def __init__(self):
        pass

    def update(self):
        pass

    def draw_map(self):
        grass_tile = pygame.image.load("Assets/grass_tile.png")
        sand_tile = pygame.image.load("Assets/sand_tile.png")
        water_tile = pygame.image.load("Assets/water_tile.png")
        current_row = -1
        for row in level1:
            current_row += 1
            current_tile = 0
            for tile in row:
                if tile == 0:
                    display_surface.blit(pygame.transform.scale(grass_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1
                elif tile == 1:
                    display_surface.blit(pygame.transform.scale(water_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1
                else:
                    display_surface.blit(pygame.transform.scale(sand_tile, (70, 70)), (current_tile * 70, current_row * 70))
                    current_tile += 1

    def draw_hud(self):
        playbutton = pygame.image.load("Assets/play.png")
        pausebutton = pygame.image.load("Assets/pause.png")
        pygame.draw.rect(display_surface, (65, 100, 190), ((0, WINDOW_HEIGHT - 60), (WINDOW_WIDTH, 60)))
        display_surface.blit(pygame.transform.scale(pausebutton, (60, 60)), (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 60))
        display_surface.blit(pygame.transform.scale(playbutton, (60, 60)), (WINDOW_WIDTH - 120, WINDOW_HEIGHT - 60))

    def update_hud(self):
        pass

    def main_menu(self, event):
        color = (255, 255, 255)
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('Quit', True, color)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.draw.rect(display_surface, (65, 100, 190), ((WINDOW_WIDTH / 2 - 32, WINDOW_HEIGHT / 2 - 16), (64, 32)))  # background  for Quit-Button
                display_surface.blit(text, (WINDOW_WIDTH / 2 - 32, WINDOW_HEIGHT / 2 - 16))
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

    def pause_game(self, event):
        pausebutton = pygame.image.load("Assets/pause.png")
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Pause
            if WINDOW_WIDTH - 60 <= mouse[0] <= WINDOW_WIDTH and WINDOW_HEIGHT - 60 <= mouse[1] <= WINDOW_HEIGHT:
                my_game.draw_hud()
                pygame.draw.rect(display_surface, (64, 191, 81), ((WINDOW_WIDTH - 60, WINDOW_HEIGHT - 60), (60, 60)))
                display_surface.blit(pygame.transform.scale(pausebutton, (60, 60)), (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 60))
                pygame.display.update()

    def quit_game(self, mouse_menu, event, is_menu):
        if is_menu:
            if WINDOW_WIDTH / 2 - 32 <= mouse_menu[0] <= WINDOW_WIDTH / 2 + 32 and WINDOW_HEIGHT / 2 - 16 <= mouse_menu[1] <= WINDOW_HEIGHT / 2 + 16:   # Click on Quit
                pygame.quit()
                exit("Mousebutton Exit")
        if event.type == pygame.QUIT:  # Click on X (top right corner)
            pygame.quit()
            exit("X Exit")

    def start_round(self, event):
        playbutton = pygame.image.load("Assets/play.png")
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Play
            if WINDOW_WIDTH - 120 <= mouse[0] <= WINDOW_WIDTH - 60 and WINDOW_HEIGHT - 60 <= mouse[1] <= WINDOW_HEIGHT:
                my_game.draw_hud()
                pygame.draw.rect(display_surface, (64, 191, 81), ((WINDOW_WIDTH - 120, WINDOW_HEIGHT - 60), (60, 60)))
                display_surface.blit(pygame.transform.scale(playbutton, (60, 60)), (WINDOW_WIDTH - 120, WINDOW_HEIGHT - 60))
                pygame.display.update()


class Player:
    """Player Class"""
    def __init__(self):
        pass

    def build_tower(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            Tower.position = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass


class Tower:
    def __init__(self):
        pass

    def shoot_on_target(self):
        pass


# Create game object
my_game = Game()
my_game.draw_map()
my_game.draw_hud()
# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in event_list:
        my_game.main_menu(event)
        my_game.pause_game(event)
        my_game.start_round(event)
        my_game.quit_game(mouse, event, False)
        Player.build_tower(Player, event)
    pygame.display.update()
    clock.tick(FPS)
