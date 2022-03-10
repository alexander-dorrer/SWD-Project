import pygame


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
        if event.type == pygame.MOUSEBUTTONUP and 0 <= mouse[0] <= 60 and 780 <= mouse[1] <= 840:
            chosen = True
            while chosen:
                event_list = pygame.event.get()
                mouse_tower = pygame.mouse.get_pos()
                for events in event_list:
                    if events.type == pygame.MOUSEBUTTONUP:
                        pygame.display.update()
                        self.positions.append(mouse_tower)
                        chosen = False

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


class Projectile(object):   # Why object?

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
