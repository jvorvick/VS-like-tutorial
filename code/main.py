from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()
        # sprites
        
        
    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        objects_sort = []
        # entities_sort = []

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE,y * TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        # for obj in map.get_layer_by_name('Objects'):
        #     objects_sort.append(obj)
            
            
        # for obj in map.get_layer_by_name('Entities'):
        #     objects_sort.append(obj)

        # def sortFunc(e):
        #     return e.y

        # objects_sort.sort(key=sortFunc)
        
        # for obj in objects_sort:
        #     print(obj.name)
        #     if obj.name == 'Player':
        #         print(obj.y)
        #         self.player = Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)
        #     elif not obj.name:
        #         print(obj.y)
        #         CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))
             

        for obj in map.get_layer_by_name('Objects'):
            # print(obj.y)
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Entities'):
            # print(obj.y)
            if obj.name == 'Player':
                self.player = Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)


        


        

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            # for sprite in self.all_sprites:
            #     print(sprite.rect.y)
            # print(self.all_sprites)
            
            self.all_sprites.update(dt)
            

            # draw
            self.display_surface.fill('black')
            self.all_sprites.ysort()
            # for sprite in self.all_sprites.sprites():
            #     print('SPRITE', sprite.rect)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
