import pygame
from game import Game
import math


class Tower:
    def __init__(self, window):
        self.window = window
        self.height = 60
        self.width = 60
        self.price = 100
        self.sell_cost = self.price * 0.5
        self.tower_base_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Base.png')
        self.tower_head_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Head.png')
        self.range = 200
        self.damage = 5
        self.positions = []
        self.collision_circle = pygame.image.load('assets/Towers&Projectiles/Collision_Circle/collision_circle.png')
        self.mask = pygame.mask.from_surface(self.collision_circle)

    def place(self, event, round_started, landscape, money):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font('freesansbold.ttf', 32)
        if event.type == pygame.MOUSEBUTTONUP and 0 <= mouse[0] <= 60 and 780 <= mouse[1] <= 840 and not round_started and money >= self.price:
            chosen = True
            tower_base = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Base.png")
            tower_head = pygame.image.load("Assets/Towers&Projectiles/Tower_1/Tower_1_Head.png")
            pygame.draw.rect(self.window, (64, 191, 81), ((0, 780), (60, 60)))
            self.window.blit(pygame.transform.scale(tower_base, (60, 60)), (0, 780))
            self.window.blit(pygame.transform.scale(tower_head, (60, 60)), (0, 780))
            pygame.display.update()
            while chosen:
                event_list = pygame.event.get()
                mouse_tower = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP:
                        if 780 <= mouse_tower[1] <= 840:    # if clicked on HUD
                            chosen = False      # toggle place tower off / break loop
                        elif money < self.price:
                            error_message = font.render('keine Kohle mehr bro', True, (255, 0, 0))
                            self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                            pygame.display.update()
                            chosen = False
                            break
                        else:   # if clicked on map
                            mouse_landscape = mouse_tower
                            mouse_tower = list(mouse_tower)  # hier musss noch das Bild zentriert werden
                            position_x = (mouse_tower[0] % 60)
                            mouse_tower[0] -= ((position_x + 30) - 60)
                            position_y = (mouse_tower[1] % 60)
                            mouse_tower[1] -= ((position_y + 30) - 60)
                            mouse_tower = tuple(mouse_tower)
                            width, heigth = pygame.display.get_window_size()
                            pos_x = math.ceil((mouse_landscape[0] / width) * 20) - 1
                            pos_y = math.ceil((mouse_tower[1] / heigth) * 14) - 1
                            if 2 <= landscape[pos_y][pos_x] <= 4:    # check if tower on sand
                                error_message = font.render('Error! Turm nicht auf Sand plazierbar!', True, (255, 0, 0))
                                self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                                pygame.display.update()
                            elif landscape[pos_y][pos_x] == 1:  # check if tower in water
                                error_message = font.render('Error! Turm nicht im Wasser plazierbar!', True, (255, 0, 0))
                                self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                                pygame.display.update()
                            elif mouse_tower not in self.positions:  # check if tower is already on position
                                self.positions.append(mouse_tower)
                                surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
                                pygame.draw.circle(surface, (50, 50, 50, 100), (self.range, self.range), self.range, 0)
                                self.window.blit(surface, (mouse_tower[0] - self.range, mouse_tower[1] - self.range))
                                self.draw_towers()
                                money = money - self.price
                                pygame.display.update()
                    elif events.type == pygame.KEYUP:
                        if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                            chosen = False  # toggle place tower off / break loop
                    Game.quit_game(self, events, False)
        return money

    def draw_towers(self):
        for tower in self.positions:
            tower_base_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Base.png')
            tower_head_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Head.png')
            self.window.blit(pygame.transform.scale(tower_base_img, (self.width, self.height)),
                             (tower[0] - 30, tower[1] - 30))
            self.window.blit(pygame.transform.scale(tower_head_img, (self.width, self.height)),
                             (tower[0] - 30, tower[1] - 30))

    def draw_range(self):
        for tower in self.positions:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (50, 50, 50, 100), (self.range, self.range), self.range, 0)
            self.window.blit(surface, (tower[0] - self.range, tower[1] - self.range))
        self.draw_towers()

    def sell(self, event, mouse,  round_started, money):
        if event.type == pygame.MOUSEBUTTONUP and 250 <= mouse[0] <= 400 and 780 <= mouse[1] <= 840 and not round_started:
            chosen = True
            while chosen:
                event_list = pygame.event.get()
                mouse_tower = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP:
                        if 780 <= mouse_tower[1] <= 840:  # if clicked on HUD
                            chosen = False  # toggle place tower off / break loop
                            break
                        mouse_tower = list(mouse_tower)  # hier musss noch das Bild zentriert werden
                        position_x = (mouse_tower[0] % 60)
                        mouse_tower[0] -= ((position_x + 30) - 60)
                        position_y = (mouse_tower[1] % 60)
                        mouse_tower[1] -= ((position_y + 30) - 60)
                        mouse_tower = tuple(mouse_tower)
                        if mouse_tower in self.positions:  # check if tower is on position
                            cross = pygame.image.load("Assets/cross.png")
                            self.window.blit(pygame.transform.scale(cross, (60, 60)), (mouse_tower[0] - 30, mouse_tower[1] - 30))
                            index_mouse_tower = self.positions.index(mouse_tower)
                            self.positions.pop(index_mouse_tower)
                            pygame.display.update()
                            money = money + self.sell_cost
                    elif events.type == pygame.KEYUP:
                        if events.key == pygame.K_ESCAPE:  # Esc. is pressed
                            chosen = False  # toggle place tower off / break loop
                    Game.quit_game(self, events, False)
        return money

    def projectile(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def enemy_in_range(self, pos_enemy):
        damage = 0
        for towers in self.positions:
            if towers[0] + self.range >= pos_enemy[0] >= towers[0] - self.range and towers[1] + self.range >= pos_enemy[1] >= towers[1] - self.range:
                damage += self.shoot()
        return damage

    def draw_circle(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def shoot(self):
        return self.damage

    def animate(self):
        pass
