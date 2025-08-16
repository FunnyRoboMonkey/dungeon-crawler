import pygame, sys
from pygame.locals import *
from level import *
from player import *

pygame.init()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (255,0,0)
images = {"w": "images/tiles/wall31.gif", "f": "images/tiles/floor23.gif", "e": "images/tiles/door31.gif", "s": "images/tiles/door32.gif"}
player = Player("images/player/kangadillo.gif", (640,450), True)

#var to keep track of levels
levels = []
level_num = 0
current_level = None

def change_level(change):
    global level_num, current_level
    if change == 1:
        if level_num == len(levels) - 1:

            levels.append(RandomLevel(player, images))
        level_num += 1
        current_level = levels[level_num]
        player.up_level(current_level)
    elif change == -1:
        if level_num > 0:
            level_num -= 1
        current_level = levels[level_num]
        player.back_level(current_level)


def main():

    global screen, level_num, current_level
    levels.append(RandomLevel(player, images))
    current_level = levels[level_num]
    player.level = current_level

    player.up_level(current_level)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
                elif event.key == K_q:
                       sys.exit()
                elif event.key == K_UP:
                    player.change_y(-32)
                elif event.key == K_DOWN:
                    player.change_y(32)
                elif event.key == K_LEFT:
                    player.change_x(-32)
                elif event.key == K_RIGHT:
                    player.change_x(32)
        screen.fill(color)
        current_level.draw(screen)
        pygame.display.flip()
        change_level(player.update())






if __name__ == "__main__":
    main()