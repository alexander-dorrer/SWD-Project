import pygame
from map import Map
from enemy import Enemy
from game import Game

# Initialize pygame
pygame.init()
pygame.display.set_caption("Tower Defense")

# Set Menu Display
menu_width = 240
menu_height = 378
display_surface = pygame.display.set_mode((menu_width, menu_height))
my_menu = Game(display_surface, menu_width, menu_height)

# Set Game Display
window = my_menu.game_menu()
display_surface = pygame.display.set_mode((window[0], window[1]))
my_game = Game(display_surface, window[0], window[1])
my_game.draw_map()
my_game.draw_hud()

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()
start_timer = False

# Create game object
my_enemy = Enemy(display_surface)
my_enemy.draw_enemy()

# Create Enemy
my_enemy = Enemy(display_surface, my_map.level1_path)
my_enemy.draw_enemy(spawn_point[0], spawn_point[1])
MOVEENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEENEMY, 150)
# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in event_list:
        my_game.main_menu(event)
        my_game.pause_game(event, mouse)
        my_game.start_round(event, mouse)
        my_game.quit_game(event, False)
        my_game.quit_game(mouse, event, False)

        if event.type == MOVEENEMY:
            my_map.draw_map(my_level, display_surface)
            my_enemy.move()

    my_game.timer(False)
    pygame.display.update()
    clock.tick(FPS)

