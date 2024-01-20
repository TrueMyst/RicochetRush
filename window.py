import sys
import math
import pygame
import random
import helper

from components import BouncingBall
from colors import GruvboxBright

def menu(screen):
    pygame.display.set_caption("⛹️  RicochetRush")
    clock = pygame.time.Clock()

    oswald = pygame.font.Font("./assets/Oswald-Bold.ttf", 85)
    oswald_45 = pygame.font.Font("./assets/Oswald-Bold.ttf", 45)

    logo = oswald.render("RicochetRush", True, GruvboxBright().blue)
    logo_RECT = logo.get_rect()

    caption = oswald_45.render("PRESS SPACE TO START!", True, GruvboxBright().light2)
    caption_RECT = caption.get_rect()

    width, height = screen.get_width(), screen.get_height()
    bouncy = []

    for _ in range(40):
        x, y = random.randint(10, width - 10), random.randint(10, height-10) 
        color = GruvboxBright().choose()
        bouncy.append(BouncingBall(x, y, 4, 2, 7, color, width, height, screen))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN):
                print("Hello World")
            
        screen.fill(GruvboxBright().dark1) 

        ticks = pygame.time.get_ticks()
        oscillation = 15 * math.sin(ticks / 1000 * 2 * math.pi)

        for ball in bouncy:
            ball.update_position()
            ball.draw()
        
        logo_RECT.center =  int(width/2), 225 + int(oscillation)
        caption_RECT.center = int(width/2), 50 + int(height/2)

        screen.blit(logo, logo_RECT)
        screen.blit(caption, caption_RECT) if helper.blink(450, ticks) else False

        pygame.display.flip()
        clock.tick(60)
