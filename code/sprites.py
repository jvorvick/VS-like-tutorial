from settings import *
from math import atan2, degrees

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)
        self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups, all_sprites):
        # player connection
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(0,1)

        # sprite setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join('images', 'gun', 'gun.png'))
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center = self.player.rect.center + self.player_direction * self.distance)

        # bullet setup
        self.all_sprites = all_sprites

    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()

    def rotate_gun(self):
        angle = degrees(atan2(self.player_direction.x, self.player_direction.y)) - 90
        if self.player_direction.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
            self.image = pygame.transform.flip(self.image, False, True)

    def fire_gun(self):
        Bullet(self.player_direction, self.rect.center, self.rect.width, self.all_sprites)

    def update(self, _):
        self.get_direction()
        angle = self.rotate_gun()
        self.rect.center = self.player.rect.center + self.player_direction * self.distance
        if pygame.mouse.get_just_pressed()[0]:
            self.fire_gun()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, direction, pos, gun_width, groups):
        super().__init__(groups)
        self.bullet_surf = pygame.image.load(join('images', 'gun', 'bullet.png')).convert_alpha()
        self.image = self.bullet_surf
        self.direction = direction
        self.speed = 400
        self.angle = degrees(atan2(self.direction.x, self.direction.y)) - 90
        self.rect = self.image.get_frect(center = pos + self.direction * (gun_width / 2))

    def update(self, dt):
        self.image = pygame.transform.rotozoom(self.bullet_surf, self.angle, 1)
        self.rect.center += self.direction * self.speed * dt