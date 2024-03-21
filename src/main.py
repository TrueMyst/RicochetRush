import pygame
from sys import exit
from window import menu

# Initialize Pygame
pygame.init()

# Setting screen display
width, height = 900, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    menu(screen)

    # Display work
    pygame.display.update()

    # Control the frame rate
    dt = pygame.time.Clock().tick(60)
