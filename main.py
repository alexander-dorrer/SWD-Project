import pygame
from map import level1

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense lol")

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
        pass

    def main_menu(self):
        # start_btn_img = pygame.image.load("Assets/start_btn.png").convert_alpha()
        # exit_btn_img = pygame.image.load("Assets/exit_btn.png").convert_alpha()
        # display_surface.blit(start_btn_img, (200, 400))
        # display_surface.blit(exit_btn_img, (900, 400))
        pass

    def pause_game(self):
        pass

    def start_round(self):
        pass


class Player:
    """Player Class"""
    def __init__(self):
        pass

    def build_turret(self):
        pass


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
my_game.main_menu()
my_game.draw_map()

# The main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.update()
        clock.tick(FPS)

pygame.quit()

