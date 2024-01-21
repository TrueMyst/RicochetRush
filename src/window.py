import sys
import math
import pygame
import random
import helper
import constant

from components import BouncingBall, ProgressBar
from colors import GruvboxBright, GruvboxSoft

WIDTH = 900
HEIGHT = 600

def game(screen):
    pygame.display.set_caption("⛹️  RicochetRush")

    oswald = pygame.font.Font("../assets/Oswald-Bold.ttf", 230)
    w, h = screen.get_width(), screen.get_height()

    print(w, h)

    score = 1
    speed = 1
    bouncy = []
    star_xy = helper.generate_stars_cords(WIDTH, HEIGHT)

    # Main game loop
    while True:
        screen.fill(GruvboxSoft().dark1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        font_surf = oswald.render(f"{score}", True, GruvboxSoft().dark2)
        font_rect = font_surf.get_rect()
        font_rect.center = int(WIDTH/2), int(HEIGHT/2)

        screen.blit(font_surf, font_rect)

        # Progress Bar
        progressbar = ProgressBar(13, score, 15, GruvboxSoft().dark2, 25, screen)
        progressbar.draw()

        # Track Mouse
        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, GruvboxSoft().white, mouse_position, constant.MOUSE_RADIUS)

        # Check collisions & generates stars
        if helper.check_collisions(mouse_position, star_xy, constant.STAR_RADIUS):
            score += 1
            star_xy = helper.generate_stars_cords(WIDTH, HEIGHT)

            if score != 0 and score % 3 == 0:
                speed += 1
                x, y = helper.generate_bouncy_cords(WIDTH, HEIGHT)
                vx, vy = speed + 2, speed + 1
                color = GruvboxSoft().choose()

                bouncy.append(BouncingBall(x, y, vx, vy, constant.BOUNCE_RADIUS, color, WIDTH, HEIGHT, screen))
        
        # For each bouncy ball
        # Update their position and draw them in their respective class:)
        for ball in bouncy:
            ball.update_position()
            ball.draw()

            if helper.check_collisions(mouse_position, ball.position(), constant.BOUNCE_RADIUS):
                print(score)
                pygame.quit()
                sys.exit()

        pygame.draw.circle(screen, GruvboxBright().yellow, star_xy, constant.STAR_RADIUS)

        # Updates the whole screen & controls the FPS
        pygame.display.update()
        pygame.time.Clock().tick(60)

def menu(screen):
    # Setting screen display
    pygame.display.set_caption("⛹️  RicochetRush")
    clock = pygame.time.Clock()

    oswald = pygame.font.Font("../assets/Oswald-Bold.ttf", 85)
    oswald_45 = pygame.font.Font("../assets/Oswald-Bold.ttf", 45)

    logo = oswald.render("RicochetRush", True, GruvboxBright().blue)
    logo_RECT = logo.get_rect()

    caption = oswald_45.render("PRESS SPACE TO START!", True, GruvboxBright().light2)
    caption_RECT = caption.get_rect()

    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    bouncy = []

    for _ in range(75):
        x, y = random.randint(10, WIDTH - 10), random.randint(10, HEIGHT-10) 
        bright, soft = GruvboxBright().choose(), GruvboxSoft().choose()
        color = random.choice([bright, soft])
        
        vx, vy = random.randint(4, 7), random.randint(4, 7)

        bouncy.append(BouncingBall(x, y, vx, vy, 5, color, WIDTH, HEIGHT, screen))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (event.type == pygame.MOUSEBUTTONDOWN):
                game(screen)
            
        screen.fill(GruvboxBright().dark1) 

        ticks = pygame.time.get_ticks()
        oscillation = 15 * math.sin(ticks / 1000 * 2 * math.pi)

        for ball in bouncy:
            ball.update_position()
            ball.draw()
        
        logo_RECT.center =  int(WIDTH/2), 225 + int(oscillation)
        caption_RECT.center = int(WIDTH/2), 50 + int(HEIGHT/2)

        screen.blit(logo, logo_RECT)
        screen.blit(caption, caption_RECT) if helper.blink(450, ticks) else False

        pygame.display.flip()
        clock.tick(60)
