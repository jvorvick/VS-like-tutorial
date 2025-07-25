from settings import *
from player import Player

# class Player(pygame.sprite.Sprite):
#     def __init__(self, groups):
#         super().__init__(groups)
#         self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
#         self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
#         self.direction = pygame.Vector2()
#         self.speed = 300

#     def update(self, dt):
#         keys = pygame.key.get_pressed()
#         self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
#         self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
#         self.direction = self.direction.normalize() if self.direction else self.direction
#         self.rect.center += self.direction * self.speed * dt

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((400,300), self.all_sprites)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

    # # general setup
    # pygame.init()
    # display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # pygame.display.set_caption('Vampire Savior')
    # running = True
    # clock = pygame.time.Clock()

    # # import

    # # sprites
    # all_sprites = pygame.sprite.Group()

    # player = Player(all_sprites)
    
    # while running:
    #     dt = clock.tick() / 1000
    #     # event loop
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
        
    #     # update
    #     all_sprites.update(dt)

    #     # draw the game
    #     display_surface.fill('#31662f')
    #     all_sprites.draw(display_surface)
    #     pygame.display.update()

    # pygame.quit()