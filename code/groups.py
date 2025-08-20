from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()  

    def draw(self, target_pos):
       
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)

    def ysort(self):
        ysort = []
        for sprite in self:
            ysort.append(sprite)
            self.remove(sprite)
        ysort.sort(key=lambda sprite : sprite.rect.centery)
        for y in ysort:
            self.add(y)

class GroundTiles(AllSprites):
    def __init__(self):
        super().__init__()