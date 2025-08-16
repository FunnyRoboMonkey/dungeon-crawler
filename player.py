import pygame, random
from tiles import Tile
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, path, pos, facing_r):
        super().__init__()
        self.path = path
        self.facing_r = facing_r
        self.image = pygame.image.load(self.path)
        desired_width = 32
        desired_height = 32
        self.image = pygame.transform.scale(self.image, (desired_width, desired_height))
        if not self.facing_r:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.movement = [0,0]
        self.inventory = {}
        self.health = 100
        self.attack_damage = 5
        self.defense = 1
        self.facing = "R"
        self.alive = True
        self.xp = 0
        self.level = None
    def update(self):
        self.rect.move_ip(self.movement)
        if len(pygame.sprite.spritecollide(self, self.level.walls, False)):
            if pygame.sprite.collide_rect(self, self.level.exit): #and self.level.unlocked
                return 1
            elif pygame.sprite.collide_rect(self, self.level.start):
                return -1
            else:
                self.movement[0]*= -1
                self.movement[1]*= -1
            self.rect.move_ip(self.movement)
        self.movement[0] = 0
        self.movement[1] = 0
    def up_level(self, level):
        self.movement = [0,0]
        self.level = level
        self.rect.topleft = level.start_pos
    def back_level(self, level):
        self.movement = [0,0]
        self.level = level
        self.rect.topleft = level.end_pos
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def change_x(self, change):
        self.movement[0] = change
    def change_y(self, change):
        self.movement[1] = change