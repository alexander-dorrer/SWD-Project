from calendar import c
from distutils.spawn import spawn
import pygame
import math


class Enemy:

    def __init__(self, window, path):
        self.current_position = None
        self.goal_position = 0
        self.animation_count = 0
        self.width = 55
        self.height = 55
        self.window = window
        self.enemy_animation_imgs = [
            pygame.image.load('Assets/Enemy/WALK_000.png'),
            pygame.image.load('Assets/Enemy/WALK_001.png'),
            pygame.image.load('Assets/Enemy/WALK_002.png'),
            pygame.image.load('Assets/Enemy/WALK_003.png'),
            pygame.image.load('Assets/Enemy/WALK_004.png'),
            pygame.image.load('Assets/Enemy/WALK_005.png'),
            pygame.image.load('Assets/Enemy/WALK_006.png')
        ]
        self.path = path
        self.step = 1
        self.x = 0
        self.y = 0
        self.next_step = [self.path[self.step][0] * 60, self.path[self.step][1] * 60]
        self.enemy_mask_image = pygame.image.load('Assets/Enemy/WALK_000.png')
        # self.enemy_sprite.image = self.enemy_mask_image
        self.enemy_mask = pygame.mask.from_surface(self.enemy_mask_image)
        self.health_points = 100
        self.alive = True
        self.goal_position_reached = False

    def draw_enemy(self, spawn_point_x, spawn_point_y):
        self.x, self.y = spawn_point_x, spawn_point_y
        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[0], (self.width, self.height)),
                         (self.x, self.y))

    def move(self):
        if self.alive:
            self.goal_position = [self.path[len(self.path) - 1][0] * 60, self.path[len(self.path) - 1][1] * 60]
            self.current_position = [self.y, self.x]
            if self.current_position != self.goal_position:
                if self.current_position == self.next_step:
                    self.step += 1
                    self.next_step = [self.path[self.step][0] * 60, self.path[self.step][1] * 60]

                if self.current_position[0] != self.next_step[0]:
                    if self.current_position[0] > self.next_step[0]:
                        self.y -= 4
                        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                                (self.width, self.height)), (self.x, self.y))
                    elif self.current_position[0] < self.next_step[0]:
                        self.y += 4
                        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                                (self.width, self.height)), (self.x, self.y))
                elif self.current_position[1] != self.next_step[1]:
                    if self.current_position[1] > self.next_step[1]:
                        self.x -= 4
                        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                                (self.width, self.height)), (self.x, self.y))
                    elif self.current_position[1] < self.next_step[1]:
                        self.x += 4
                        self.window.blit(pygame.transform.scale(self.enemy_animation_imgs[self.animation_count],
                                                                (self.width, self.height)), (self.x, self.y))
            if self.animation_count >= 6:
                self.animation_count = 0
            else:
                self.animation_count += 1
            self.draw_health_bar()

    def get_shot(self, damage, money):
        if self.alive:
            if self.health_points > 0 and not self.goal_position_reached:
                self.health_points = self.health_points - damage
                return money, False
            if self.health_points <= 0:
                self.alive = False
                money += 50
                return money, True
        else:
            return money, False

    def position(self):
        return self.x, self.y

    def draw_health_bar(self):
        if self.alive:
            pygame.draw.rect(self.window, (64, 64, 64), ((self.x + self.width * 0.1, self.y - self.height * 0.1), (self.width * 0.8, 4)))
            pygame.draw.rect(self.window, (255, 0, 0), ((self.x + self.width * 0.1, self.y - self.height * 0.1), ((self.health_points / 100) * self.width * 0.8, 4)))

    def is_alive(self):
        return self.alive

    def in_goal_pos(self, round_started):
        if self.current_position == self.goal_position and round_started and not self.goal_position_reached:  # check if enemy on goal pos
            self.goal_position_reached = True
            return self.health_points
        else:
            return 0
