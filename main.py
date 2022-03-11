from faulthandler import disable
import pygame
from map import Map
from enemy import Enemy
from tower import Tower
from game import Game

# Initialize pygame
pygame.init()
pygame.display.set_caption("Tower Defense")
round_started = False

# Set Menu Display
width = 1200
height = 840
display_surface = pygame.display.set_mode((width, height))
my_menu = Game(display_surface, width, height)
my_menu.game_menu(True)

# Set Game Display
display_surface = pygame.display.set_mode((width, height))
my_game = Game(display_surface, width, height)
my_game.draw_hud()

# Create Map
my_map = Map()
my_level = my_map.level1
my_map.draw_map(my_level, display_surface)
spawn_point = my_map.get_spawn_point(my_map.level1)

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()
start_timer = False

# Create game object
my_game = Game(display_surface, width, height)
my_game.draw_hud()

# Create Enemy
my_enemy = Enemy(display_surface, my_map.level1_path)
my_enemy.draw_enemy(spawn_point[0], spawn_point[1])
MOVEENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEENEMY, int((1000/FPS*7)))

# Create Tower
my_tower = Tower(display_surface)
# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    my_tower.draw_towers()
    for event in event_list:
        my_game.main_menu(event)
        my_game.quit_game(event, False)
        my_tower.place(event, round_started)
        if not round_started:
            round_started = my_game.start_round(event, mouse)
        elif round_started:
            round_started = my_game.pause_round(event, mouse)
        if event.type == MOVEENEMY and round_started:
            my_map.draw_map(my_level, display_surface)
            my_tower.draw_towers()
            my_enemy.move()
        pygame.display.update()
    clock.tick(FPS)
