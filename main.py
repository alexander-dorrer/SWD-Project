import pygame
from map import level1

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defense")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()


class Game:
    """Class to control Gameplay"""
    def __init__(self, x, y):
        # self.rect = self.image.get_rect(center = (x, y))
        # self.clicked = False
        # self.image = pygame.surface
        pass

    def update(self, event_list):
        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if self.rect.collidepoint(event.pos):
        #             self.clicked = not self.clicked
        #
        # self.image = self.click_image if self.clicked else self.original_image
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

    def update_hud(self):
        pass

    def main_menu(self):
        pass

    def pause_game(self):
        pass

    def quit_game(self,event):
        width = display_surface.get_width()
        height = display_surface.get_height()
        color = (255, 255, 255)
        smallfont = pygame.font.SysFont('Corbel', 35)
        text = smallfont.render('quit', True, color)
        mouse = pygame.mouse.get_pos()
        display_surface.blit(text, (width-70, height-40))
        # pygame.draw.rect(display_surface, 000, [height-40, height, width-70, width])    # Rahmen um Quit Button
        if event.type == pygame.MOUSEBUTTONUP:
            if width-70 <= mouse[0] <= width and height-40 <= mouse[1] <= height:
                pygame.quit()
                exit()

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
my_game = Game(0, 0)
my_game.draw_map()
# The main game loop
while True:
    pygame.init()
    event_list = pygame.event.get()
    for event in event_list:
        Game.quit_game(Game, event)
        Player.build_tower(Player, event)
    pygame.display.update()
    clock.tick(FPS)
# Game.update(event_list)
