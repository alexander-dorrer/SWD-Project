import pygame


class Tower:
    def __init__(self, window, price: int, range: int, damage: int, tower_base, tower_head, number_of_tower: int, position: tuple[int, int]):
        self.tower_has_target = False
        self.window = window
        self.height = 60
        self.width = 60
        self.price = price
        self.sell_cost = self.price * 0.5
        self.tower_base_img = tower_base
        self.tower_head_img = tower_head
        self.range = range
        self.damage = damage
        self.position = position
        self.collision_circle = pygame.image.load('assets/Towers&Projectiles/Collision_Circle/collision_circle.png')
        self.mask = pygame.mask.from_surface(self.collision_circle)
        self.number_of_tower = number_of_tower

    # def place(self, event, round_started, landscape, money):
    #     towers = 0
    #     mouse = pygame.mouse.get_pos()
    #     font = pygame.font.Font('freesansbold.ttf', 32)
    #     chosen = False
    #     if event.type == pygame.MOUSEBUTTONUP and self.number_of_tower * 60 <= mouse[
    #         0] <= self.number_of_tower * 60 + 60 and 780 <= mouse[
    #         1] <= 840 and not round_started and money >= self.price:
    #         chosen = True
    #         pygame.draw.rect(self.window, (64, 191, 81), ((self.number_of_tower * 60, 780), (60, 60)))
    #         self.window.blit(pygame.transform.scale(self.tower_base_img, (60, 60)), (self.number_of_tower * 60, 780))
    #         self.window.blit(pygame.transform.scale(self.tower_head_img, (60, 60)), (self.number_of_tower * 60, 780))
    #     pygame.display.update()
    #     while chosen:
    #         event_list = pygame.event.get()
    #         mouse_tower = pygame.mouse.get_pos()
    #         for events in event_list:
    #             if events.type == pygame.MOUSEBUTTONUP:
    #                 if 780 <= mouse_tower[1] <= 840:  # if clicked on HUD
    #                     chosen = False  # toggle place tower off / break loop
    #                 elif money < self.price:
    #                     error_message = font.render('keine Kohle mehr bro', True, (255, 0, 0))
    #                     self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
    #                     pygame.display.update()
    #                     chosen = False
    #                     break
    #                 else:  # if clicked on map
    #                     mouse_landscape = mouse_tower
    #                     mouse_tower = list(mouse_tower)  # hier musss noch das Bild zentriert werden
    #                     position_x = (mouse_tower[0] % 60)
    #                     mouse_tower[0] -= ((position_x + 30) - 60)
    #                     position_y = (mouse_tower[1] % 60)
    #                     mouse_tower[1] -= ((position_y + 30) - 60)
    #                     mouse_tower = tuple(mouse_tower)
    #                     width, heigth = pygame.display.get_window_size()
    #                     pos_x = math.ceil((mouse_landscape[0] / width) * 20) - 1
    #                     pos_y = math.ceil((mouse_landscape[1] / heigth) * 14) - 1
    #                     if 2 <= landscape[pos_y][pos_x] <= 4:  # check if tower on sand
    #                         error_message = font.render('Error! Turm nicht auf Sand plazierbar!', True, (255, 0, 0))
    #                         self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
    #                         pygame.display.update()
    #                     elif landscape[pos_y][pos_x] == 1:  # check if tower in water
    #                         error_message = font.render('Error! Turm nicht im Wasser plazierbar!', True,
    #                                                     (255, 0, 0))
    #                         self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
    #                         pygame.display.update()
    #                     elif mouse_tower not in self.position:  # check if tower is already on position
    #                         self.position.append(mouse_tower)
    #                         towers += 1
    #                         pygame.draw.lines(self.window, (0, 255, 0), True, (
    #                             (mouse_tower[0] - (self.range - 55), mouse_tower[1] - (self.range - 55)),
    #                             (mouse_tower[0] - (self.range - 55), mouse_tower[1] + (self.range - 55)),
    #                             (mouse_tower[0] + (self.range - 55), mouse_tower[1] + (self.range - 55)),
    #                             (mouse_tower[0] + (self.range - 55), mouse_tower[1] - (self.range - 55))), 3)
    #                         self.draw_towers()
    #                         money = money - self.price
    #                         pygame.display.update()
    #             elif events.type == pygame.KEYUP:
    #                 if events.key == pygame.K_ESCAPE:  # Esc. is pressed
    #                     chosen = False  # toggle place tower off / break loop
    #             game.quit_game(events, False)
    #     return money, towers

    def draw_towers(self):
        self.window.blit(pygame.transform.scale(self.tower_base_img, (self.width, self.height)),
                         (self.position[0] - 30, self.position[1] - 30))
        self.window.blit(pygame.transform.scale(self.tower_head_img, (self.width, self.height)),
                         (self.position[0] - 30, self.position[1] - 30))

    def draw_range(self):
        pygame.draw.lines(self.window, (0, 255, 0), True, (
            (self.position[0] - (self.range - 55), self.position[1] - (self.range - 55)),
            (self.position[0] - (self.range - 55), self.position[1] + (self.range - 55)),
            (self.position[0] + (self.range - 55), self.position[1] + (self.range - 55)),
            (self.position[0] + (self.range - 55), self.position[1] - (self.range - 55))), 3)
        self.draw_towers()

    # def sell(self, event, mouse, round_started, money):
    #     mouse_tower = mouse
    #     mouse_tower = list(mouse_tower)
    #     position_x = (mouse_tower[0] % 60)
    #     mouse_tower[0] -= ((position_x + 30) - 60)
    #     position_y = (mouse_tower[1] % 60)
    #     mouse_tower[1] -= ((position_y + 30) - 60)
    #     mouse_tower = tuple(mouse_tower)
    #     if event.type == pygame.MOUSEBUTTONDOWN and not round_started and mouse_tower in self.position and event.button == 3:
    #         sell = pygame.font.SysFont('Comic Sans MS', 20)
    #         message_sell = sell.render('SELL', True, (255, 0, 0))
    #         pygame.draw.rect(self.window, (65, 100, 190), ((mouse_tower[0], mouse_tower[1] + 5), (50, 20)))
    #         self.window.blit(message_sell, (mouse_tower[0], mouse_tower[1]))
    #         pygame.display.update()
    #         chosen = True
    #         while chosen:
    #             event_list = pygame.event.get()
    #             mouse_tower_2 = pygame.mouse.get_pos()
    #             for events in event_list:
    #                 if events.type == pygame.MOUSEBUTTONUP and events.button == 1:
    #                     if 780 <= mouse_tower_2[1] <= 840:  # if clicked on HUD
    #                         chosen = False  # toggle place tower off / break loop
    #                         break
    #                     elif mouse_tower[0] <= mouse_tower_2[0] <= mouse_tower[0] + 50 and mouse_tower[1] + 5 <= \
    #                             mouse_tower_2[1] <= mouse_tower[1] + 20:
    #                         cross = pygame.image.load("Assets/cross.png")
    #                         self.window.blit(pygame.transform.scale(cross, (60, 60)),
    #                                          (mouse_tower[0] - 30, mouse_tower[1] - 30))
    #                         index_mouse_tower = self.position.index(mouse_tower)
    #                         self.position.pop(index_mouse_tower)
    #                         pygame.display.update()
    #                         money = money + self.sell_cost
    #                         chosen = False
    #                         break
    #                 elif events.type == pygame.KEYUP:
    #                     if events.key == pygame.K_ESCAPE:  # Esc. is pressed
    #                         chosen = False  # toggle place tower off / break loop
    #                         break
    #                 game.quit_game(events, False)
    #     return money

    def projectile(self, pos_enemy: tuple[int, int], enemy_is_alive: bool):
        if self.enemy_in_range(pos_enemy) and enemy_is_alive:
            pygame.draw.line(self.window, (255, 0, 0, 0.5), self.position, (pos_enemy[0] + 30, pos_enemy[1] + 30), 5)

    def enemy_in_range(self, pos_enemy: tuple[int, int]) -> bool:
        if self.position[0] + self.range >= pos_enemy[0] >= self.position[0] - self.range and self.position[1] + self.range >= pos_enemy[
            1] >= self.position[1] - self.range:
            return True
        else:
            return False

    def shoot(self) -> int:
        return self.damage

    def animate(self):
        pass

    def tower_target(self, pos_enemies: list) -> tuple[bool, int, int]:
        damage = 0
        for enemy in range(len(pos_enemies)):
            if self.enemy_in_range(pos_enemies[enemy]):
                damage += self.shoot()
                self.tower_has_target = True
            if damage != 0:
                return True, enemy, damage
        else:
            self.tower_has_target = False
            return False, 0, damage  # need to return int if no target is selected

    def get_position(self) -> tuple[int, int]:
        return self.position
