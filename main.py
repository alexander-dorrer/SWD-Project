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
        width = display_surface.get_width()
        height = display_surface.get_height()
        pygame.draw.rect(display_surface, (65, 100, 190), ((0, height-60), (width, 60)))

    def update_hud(self):
        pass

    def main_menu(self, event):
        width = display_surface.get_width()
        height = display_surface.get_height()
        color = (255, 255, 255)
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('Quit', True, color)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.draw.rect(display_surface, (65, 100, 190), ((width / 2 - 32, height / 2 - 16), (64, 32)))  # Hintergrund für Quit-Button
                display_surface.blit(text, (width / 2 - 32, height / 2 - 16))
                pygame.display.update()
                running = True
                while running:  # Loop for mouse event tracking
                    event_lists = pygame.event.get()
                    mouse = pygame.mouse.get_pos()
                    for events in event_lists:
                        Game.quit_game(self, mouse, events)
                        if events.type == pygame.KEYUP:
                            if events.key == pygame.K_ESCAPE:   # Wenn Esc. gedrückt wird
                                running = False
                                Game.draw_map(self)
                                pygame.display.update()

    def pause_game(self):
        pass

    def quit_game(self, mouse, event):
        width = display_surface.get_width()
        height = display_surface.get_height()
        if event.type == pygame.MOUSEBUTTONUP:  # Click on Quit
            if width/2-32 <= mouse[0] <= width/2+32 and height/2-16 <= mouse[1] <= height/2+16:     # Check ob Maus auf Koordinaten von Quit
                pygame.quit()
                exit("Mousebutton Exit")

    def start_round(self):
        pass


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
    pygame.init()
    event_list = pygame.event.get()
    for event in event_list:
        my_game.main_menu(event)
        Player.build_tower(Player, event)
    pygame.display.update()
    clock.tick(FPS)
