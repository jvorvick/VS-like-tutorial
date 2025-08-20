from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

    def ysort(self):
        ysort = []
        for sprite in self:
            ysort.append(sprite)
            self.remove(sprite)
        def sortFunc(e):
            return e.rect.y
        # print(ysort)
        ysort.sort(key=sortFunc)
        for y in ysort:
            self.add(y)

        

    def draw(self, target_pos):
        # self.ysort()
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)