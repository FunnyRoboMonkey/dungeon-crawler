import pygame
import random
class Tile(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
class Chest(Tile):
    def __init__(self, image, pos):
        super().__init__(image, pos)
    def give_bonus(self, player):
        xpBonus = random.randint(1,5)
        player.xp += xpBonus
        num = random.randint(1, 3)
        self.kill()
        if num == 1:
            inc = random.randint(3, 7)
            player.health += inc
            return "+{} Health Bonus".format(inc)
        elif num == 2:
            inc = random.randint(1, 3)
            player.attack_damage += inc
            return "+{} Attack Bonus".format(inc)
        elif num == 3:
            player.defense += 1
            return "+1 Damage Bonus"
class Lightning(Tile):
    def __init__(self, image, pos):
        super().__init__(image, pos)
    def neg_effect(self, player):
        num = random.randint(1, 2)
        self.kill()
        if num == 1:
            inc = random.randint(3, 7)
            player.health -= inc
            return "-{} Health ".format(inc)
        elif num == 2:
            inc = random.randint(1, 3)
            player.defense -= inc
            return "-{} Defense".format(inc)
class Door(Tile):
    def __init__(self, image, pos):
        super().__init__(image, pos)
        locked = True