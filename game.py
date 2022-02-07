import pygame


class Game:
    def __init__(self):
        self.width = 680
        self.height = 680
        self.window = pygame.display.set_mode((self.width, self.height))

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()


new_game = Game()
new_game.run()



