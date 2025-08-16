import pygame
from tiles import *
class Level(pygame.sprite.Sprite):
    def __init__(self,player):
        #def __init__(self, player):
        super().__init__()
        # groups
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()

        self.player = player
        self.start_pos = (0, 0)
        self.end_pos = (0,0)
        self.exit = None
        self.start = None

        #adittional functionality
        self.health = 5
        self.had_key = False
        self.enemies = pygame.sprite.Group()
        self.messages = pygame.sprite.Group()
        #self.player = player
        self.chest = Chest("images/chest.gif", (0, 0))
        self.lightning = Lightning("images/lightning.gif", (0, 0))
        self.walls.add(self.chest)
        self.start_pos = (0, 0)
        self.end_pos = (0, 0)
        self.exit = None
        self.start = None
    def draw(self, screen):
        self.floor.draw(screen)
        self.walls.draw(screen)
        self.player.draw(screen)






class RandomLevel(Level):
    def __init__(self, player, images):
        super().__init__(player)
        self.generate_level(images, 0.5, 2)
    
    def generate_level(self, images, mult, enemy_num):
        screen_info = pygame.display.Info()
        game_map = []
        # initialize entire map to walls
        for i in range((screen_info.current_w // 32) + 1):
            game_map.append(["w"] * ((screen_info.current_h // 32) + 1))
        # calculate amount of tiles to convert into floor tiles
        # print(game_map)
        fnum = int((len(game_map) * len(game_map[0])) * mult)
        # current number of floor tiles
        count = 0
        # starting tile for dungeon generation
        tile = [len(game_map) // 2, len(game_map[0]) // 2]
        while count < fnum:
            if game_map[tile[0]][tile[1]] != "f":
                game_map[tile[0]][tile[1]] = "f"
                count += 1
            move = random.randint(1, 4)
            if move == 1 and tile[0] > 1:  # move north
                tile[0] -= 1
            elif move == 2 and tile[0] < (len(game_map) - 3):  # move south
                tile[0] += 1
            elif move == 3 and tile[1] < (len(game_map[0]) - 3):  # move east
                tile[1] += 1
            elif move == 4 and tile[1] > 1:  # move west
                tile[1] -= 1
        def placePlayerandEntrance(self):
        
            #place player on rand floor tile

            px = random.randint(0,len(game_map)-1)
            py = random.randint(0,len(game_map[0])-1)
            while game_map[px][py] != 'f' :
                px = random.randint(0,len(game_map)-1)
                py = random.randint(0,len(game_map[0])-1)
            game_map[px][py] = "s"
            for x in range(-1,1):
                for y in range(-1,1):
                    if (x,y) != (0,0):
                        game_map[px+x][py+y] = "f"
            self.start_pos = (px+ 1, py)

            
        def placeExit(self):
            ex = random.randint(0,len(game_map)-1)
            ey = random.randint(0,len(game_map[0])-1)
            while game_map[ex][ey] != 'f' :
                ex = random.randint(0,len(game_map)-1)
                ey = random.randint(0,len(game_map[0])-1)
            game_map[ex][ey] = "e"
         # create tiles based on the contents of the map list
        placePlayerandEntrance(self)
        placeExit(self)
        global px, py
        for i in range(len(game_map)):  
            for j in range(len(game_map[i])):
                if game_map[i][j] == "w":
                    self.walls.add(Tile(images["w"], (i * 32, j * 32)))
                elif game_map[i][j] == "f":
                    self.floor.add(Tile(images["f"], (i * 32, j * 32)))
                elif game_map[i][j] == "e":
                    self.exit = Door(images["e"], (i*32, j*32))
                    self.end_pos = (i*32, j*32)
                    self.walls.add(self.exit)
                elif game_map[i][j] == "s":
                    self.start = Door(images["s"], (i*32, j*32))
                    self.start_pos = (i*32, j*32)
                    self.walls.add(self.start)
                

        
        
        

            # place exit
    
            #create tile objects based on the game_map array
            #place door tile on entrance + exit

            #add in enemies

