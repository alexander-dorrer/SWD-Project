from faulthandler import disable
import pygame
from map import level1
from enemy import Enemy
from game import Game

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
start_timer = False
timer_started = 0


# Create game object
my_game = Game(display_surface, WINDOW_WIDTH, WINDOW_HEIGHT)
my_game.draw_map()
my_game.draw_hud()

my_enemy = Enemy(display_surface)
my_enemy.draw_enemy()

# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in event_list:
        my_game.main_menu(event)
        my_game.pause_game(event, mouse)
        my_game.start_round(event, mouse)
        my_game.quit_game(mouse, event, False)
        # Player.build_tower(Player, event)
    my_game.timer(False)
    pygame.display.update()
    clock.tick(FPS)

