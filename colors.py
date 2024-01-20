import pygame
import random

class GruvboxSoft():
    def __init__(self):
        self.dark0 =   pygame.Color('#1d2021') 
        self.dark1 =   pygame.Color('#282828')
        self.dark2 =   pygame.Color('#3c3836')

        self.light0 =  pygame.Color('#ebdbb2')
        self.light1 =  pygame.Color('#d5c4a1')
        self.light2 =  pygame.Color('#bdae93')

        self.black =   pygame.Color('#393939')
        self.red =     pygame.Color('#ea6962')
        self.green =   pygame.Color('#a9b665')
        self.yellow =  pygame.Color('#e0a454')
        self.blue =    pygame.Color('#7daea3')
        self.magenta = pygame.Color('#d3869b')
        self.cyan =    pygame.Color('#89b482')
        self.orange =  pygame.Color('#fe8019')
        self.white =   pygame.Color('#d4be98')
        
        self.all = [self.red, self.green, self.yellow, self.blue, self.magenta, self.cyan, self.orange]

    def choose(self):
        return random.choice(self.all)

class GruvboxBright():
    def __init__(self):
        self.dark0 =   pygame.Color('#1d2021') 
        self.dark1 =   pygame.Color('#282828')
        self.dark2 =   pygame.Color('#3c3836')

        self.light0 =  pygame.Color('#ebdbb2')
        self.light1 =  pygame.Color('#d5c4a1')
        self.light2 =  pygame.Color('#bdae93')

        self.black =   pygame.Color('#393939')
        self.red =     pygame.Color('#ea6962')
        self.green =   pygame.Color('#a9b665')
        self.yellow =  pygame.Color('#e0a454')
        self.blue =    pygame.Color('#7daea3')
        self.magenta = pygame.Color('#d3869b')
        self.cyan =    pygame.Color('#89b482')
        self.orange =  pygame.Color('#d65d0e')
        self.white =   pygame.Color('#d4be98')

        self.all = [self.red, self.green, self.yellow, self.blue, self.magenta, self.cyan, self.orange]

    def choose(self):
        return random.choice(self.all)

