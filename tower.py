import pygame
from game import Game


class Tower:
    def __init__(self, window):
        self.window = window
        self.height = 60
        self.width = 60
        self.price = [0]
        self.sell_cost = [1]
        self.tower_base_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Base.png')
        self.tower_head_img = pygame.image.load('assets/Towers&Projectiles/Tower_1/Tower_1_Head.png')
        self.range = 200
        self.positions = []

    def place(self, event):
        mouse = pygame.mouse.get_pos()
        font = pygame.font.Font('freesansbold.ttf', 32)
        if event.type == pygame.MOUSEBUTTONUP and 0 <= mouse[0] <= 60 and 780 <= mouse[1] <= 840:
            chosen = True
            while chosen:
                event_list = pygame.event.get()
                mouse_tower = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP:
                        pygame.display.update()
                        mouse_tower = list(mouse_tower)  # hier musss noch das Bild zentriert werden
                        position_x = (mouse_tower[0] % 60)
                        mouse_tower[0] -= ((position_x + 30) - 60)
                        position_y = (mouse_tower[1] % 60)
                        mouse_tower[1] -= ((position_y + 30) - 60)
                        mouse_tower = tuple(mouse_tower)
                        if mouse_tower not in self.positions:
                            self.positions.append(mouse_tower)
                            chosen = False
                        else:
                            error_message = font.render('Error! Turm hier nicht platzierbar !!!', True, (255, 0, 0))
                            self.window.blit(error_message, (mouse_tower[0] - 100, mouse_tower[1] - 32))
                    elif events.type == pygame.KEYUP:
                        if events.key == pygame.K_ESCAPE:               # Esc. is pressed
                            chosen = False                              # break loop
                    Game.quit_game(self, events, False)

    def draw_towers(self):
        for tower in self.positions:
            self.window.blit(pygame.transform.scale(self.tower_base_img, (self.width, self.height)),
                             (tower[0] - 30, tower[1] - 30))
            self.window.blit(pygame.transform.scale(self.tower_head_img, (self.width, self.height)),
                             (tower[0] - 30, tower[1] - 30))
            pygame.display.update()

    def sell(self):
        pass

    def shoot(self):
        bullets = []
        for bullet in bullets:
            if bullet.x < self.width and bullet.y > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

    def animate(self):
        pass
