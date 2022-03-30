import pygame
from map import Map
from enemy import Enemy
from tower import Tower
import game
from game import Game
from player import Player

# Initialize pygame
pygame.init()
pygame.display.set_caption("Tower Defense")
round_started = False

# Set Menu Display
width = 1200
height = 840

# Set Game Display
display_surface = pygame.display.set_mode((width, height))

# Create game object
money = 1000
my_game = Game(display_surface, width, height)
level = my_game.game_menu(True, 0)
my_game.draw_hud(money)

# Create Player
my_player = Player(display_surface, height, width)

# Create Map
my_map = Map()
my_level = my_map.level1
my_map.draw_map(my_level, display_surface)
spawn_point = my_map.get_spawn_point(my_map.level1)

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()
start_timer = False

# Create Enemy
enemy_counter = 0
enemy_speed = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]  # 0-11; 3 is standard
enemies = []
pos_enemies = []
# my_enemy = Enemy(display_surface, my_map.level1_path, 100, enemy_speed[3])
# my_enemy.draw_enemy(spawn_point[0], spawn_point[1])
MOVEENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEENEMY, int((1000 / FPS * 7)))
CREATEENEMY = pygame.USEREVENT + 3
pygame.time.set_timer(CREATEENEMY, int(2000))

# Create Tower
tower_base_1 = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
tower_head_1 = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
tower_base_2 = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Base.png")
tower_head_2 = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Head.png")
tower = Tower(display_surface, 100, 200, 5, tower_base_1, tower_head_1, 0)
my_tower2 = Tower(display_surface, 150, 300, 10, tower_base_2, tower_head_2, 1)
tower_list = [tower, my_tower2]
SHOOT = pygame.USEREVENT + 2
pygame.time.set_timer(SHOOT, int(1000))
# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    for event in event_list:
        if event.type == CREATEENEMY and enemy_counter < 6 and round_started:
            enemies.append(Enemy(display_surface, my_map.level1_path, 100, enemy_speed[3]))
            enemies[enemy_counter].draw_enemy(spawn_point[0], spawn_point[1])
            enemy_counter += 1
        level = my_game.main_menu(event, level)
        for tower in tower_list:
            money = tower.place(event, round_started, my_level, money)
            money = tower.sell(event, mouse, round_started, money)
        if not round_started:
            round_started, game_paused = my_game.start_round(event, mouse, money)
        elif round_started:
            round_started, game_paused = my_game.pause_round(event, mouse, money)
            if game_paused:  # draw tower-range if game is paused
                for tower in tower_list:
                    tower.draw_range()
                game_paused = not game_paused
        if event.type == MOVEENEMY and round_started:
            my_map.draw_map(my_level, display_surface)
            for tower in tower_list:
                tower.draw_towers()
            pos_enemies.clear()
            for enemy in enemies:
                enemy.move()
                pos_enemies.append(enemy.position())
            # my_enemy.move()
        if event.type == SHOOT and round_started and pos_enemies:
            for tower in tower_list:
                has_target, target = tower.tower_target(pos_enemies)
                if has_target:
                    money, enemy_killed = enemies[target].get_shot(
                        tower.shoot(enemies[target].is_alive()), money)
                    if not enemies[target].is_alive() and enemy_killed:  # after killing enemy +50g for more enemies enemy_killed --> list
                        enemies.pop(target)
                        my_game.draw_hud(money)
                        enemy_killed = False
                    tower.projectile(pos_enemies[target], enemies[target].is_alive())
        my_player.display_hp()
        # my_player.enemy_finished(my_enemy.in_goal_pos(round_started))
        pygame.display.update()
        game.game_over(my_player.player_hp())
        game.quit_game(event, False)
    clock.tick(FPS)
