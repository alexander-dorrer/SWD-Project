import tkinter.messagebox

import pygame
from map import Map
from enemy import Enemy
from tower import Tower
import game
from game import Game
from player import Player
import random
from tkinter import messagebox

# Initialize pygame
pygame.init()
pygame.display.set_caption("nicht geil aber es funktioniert manchmal")
round_started = False
restart = False

# Set Menu Display
width = 1200
height = 840

# Set Game Display
display_surface = pygame.display.set_mode((width, height))


# Create game object
money = 1000
my_game = Game(display_surface, width, height, 0)
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
number_of_enemies = 6
enemy_speed = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 300]
enemy_speed_index = 0
enemies = []
enemy_hp = 85
dead_enemies = []
pos_enemies = []
MOVEENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(MOVEENEMY, int((1000 / FPS * 7)))
CREATEENEMY = pygame.USEREVENT + 3
pygame.time.set_timer(CREATEENEMY, int(1500))

# Create Tower
# tower_base_1 = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
# tower_head_1 = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
# tower_base_2 = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Base.png")
# tower_head_2 = pygame.image.load("Assets/Towers&Projectiles/Tower_2/Tower_2_Head.png")
# tower_base_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Base.png")
# tower_head_3 = pygame.image.load("Assets/Towers&Projectiles/Tower_3/Tower_3_Arm.png")
# my_tower = Tower(display_surface, 100, 150, 5, tower_base_1, tower_head_1, 0)
# my_tower2 = Tower(display_surface, 200, 200, 10, tower_base_2, tower_head_2, 1)
# my_tower3 = Tower(display_surface, 300, 300, 15, tower_base_3, tower_head_3, 2)
"""my_tower, my_tower2, my_tower3"""
tower_list = []
tower_list_old = []
tower_positions = []
sold = False
SHOOT = pygame.USEREVENT + 2
pygame.time.set_timer(SHOOT, int(1000))

# The main game loop
while True:
    event_list = pygame.event.get()
    mouse = pygame.mouse.get_pos()
    if game.is_wave_over(enemies) and round_started:
        dead_enemies.clear()
        number_of_enemies, enemy_speed_index, enemy_hp, wave = my_game.start_new_wave(number_of_enemies,
                                                                                      enemy_speed_index, enemy_hp,restart)
        for time in range(number_of_enemies):
            enemy_hp_new = enemy_hp * random.randint(6, 15) / 10
            enemy_speed_index_new = enemy_speed_index + random.randint(1, 2)
            if enemy_speed_index_new >= 9:
                enemy_speed_index_new = 9
            enemies.append(Enemy(display_surface, my_map.level1_path, enemy_hp_new, enemy_speed[enemy_speed_index_new], time))
        for enemy in enemies:
            enemy.draw_enemy(spawn_point[0], spawn_point[1])

        # round_started, game_paused = False, True
        # """einkommentieren, wenn nach jeder Wave neu Start gedr??ckt werden soll"""

    for event in event_list:
        if event.type == CREATEENEMY and round_started:
            for enemy in enemies:
                enemy.create_enemy()
        level = my_game.main_menu(event, level)
        towers_created, money = my_game.create_tower(event, my_level, money, tower_positions)
        if towers_created:
            for towers in towers_created:
                tower_list.append(
                    Tower(display_surface, towers[0], towers[1], towers[2], towers[3], towers[4], towers[5], towers[6]))
        if tower_list != tower_list_old:
            for tower in tower_list:
                tower_positions.append(tower.get_position())
            tower_list_old = tower_list
        for tower in tower_list:
            money, sold = my_game.sell_tower(event, mouse, round_started, tower.position, money, tower.sell_cost)
            if sold:
                index_tower = tower_list.index(tower)
                tower_list.pop(index_tower)
                tower_positions.clear()
                for towers in tower_list:
                    tower_positions.append(towers.position)
        if not round_started:
            round_started, game_paused = my_game.start_round(event, mouse, money)
        elif round_started:
            round_started, game_paused = my_game.pause_round(event, mouse, money)
            if game_paused:  # draw tower-range if game is paused
                for tower in tower_list:
                    tower.draw_range()
                game_paused = not game_paused
            if event.type == pygame.MOUSEBUTTONUP and width - 180 <= mouse[
            0] <= width - 120 and height - 60 <= mouse[1] <= height:
                tower_list = []
                tower_list_old = []
                tower_positions = []
                sold = False
                enemy_counter = 0
                enemy_speed = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20]
                enemy_speed_index = 1
                enemies = []
                enemy_hp = 85
                dead_enemies = []
                pos_enemies = []
                money = 1000
                my_game.draw_hud(money)
                my_player.health_points = 100
                restart = True
            if player_hp == 0:
                game_over = True
                my_game.pause_round_after_go()
                game_over_tag = pygame.image.load("Assets/game_over.png")
                game_over_button = pygame.image.load("Assets/restart.png")
                display_surface.blit(pygame.transform.scale(game_over_tag, (400, 150)), (width - 800, height - 600))
                display_surface.blit(pygame.transform.scale(game_over_button, (400, 150)),
                             (width - 800, height - 400))
                pygame.display.update()
                while game_over:
                    event_list = pygame.event.get()
                    mouse = pygame.mouse.get_pos()
                    for event in event_list:
                        if event.type == pygame.MOUSEBUTTONUP and width - 800 <= mouse[
                            0] <= width - 400 and height - 400 <= mouse[1] <= height - 250:
                            tower_list = []
                            tower_list_old = []
                            tower_positions = []
                            sold = False
                            enemy_counter = 0
                            enemy_speed = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20]
                            enemy_speed_index = 1
                            enemies = []
                            enemy_hp = 85
                            dead_enemies = []
                            pos_enemies = []
                            money = 1000
                            my_game.draw_hud(money)
                            restart = True
                            my_player.health_points = 100
                            game_over = False
                            break
                        game.quit_game(event,False)


        if event.type == MOVEENEMY and round_started:
            my_map.draw_map(my_level, display_surface)
            for tower in tower_list:
                tower.draw_towers()
            pos_enemies.clear()
            for enemy in enemies:
                enemy.move()
                pos_enemies.append(enemy.position())
        if event.type == SHOOT and round_started and pos_enemies:
            for tower in tower_list:
                has_target, target, damage = tower.tower_target(pos_enemies)
                if has_target and enemies and target < len(enemies):
                    money, enemy_killed = enemies[target].get_shot(
                        damage, money)
                    if not enemies[
                        target].is_alive() and enemy_killed:  # after killing enemy +10g for more enemies enemy_killed --> list
                        dead_enemies.append(enemies.pop(target))
                        my_game.draw_hud(money)
                        enemy_killed = False
                    if enemies and target < len(enemies):
                        tower.projectile(pos_enemies[target], enemies[target].is_alive())
        if round_started:
            my_game.display_wave()
            my_player.display_hp()
        for enemy in enemies:
            enemy_hp_in_goal_pos, enemy_in_goal_pos = enemy.in_goal_pos(round_started)
            my_player.enemy_finished(enemy_hp_in_goal_pos)
            if enemy_in_goal_pos:
                if enemy_in_goal_pos:
                    dead_enemies.append(enemies.pop(enemies.index(enemy)))
        pygame.display.update()
        player_hp = game.game_over(my_player.health_points,display_surface)
        game.quit_game(event, False)
    clock.tick(FPS)
