import sys
import math
import pygame
import random
import helper

from constant import *
from components import BouncingBall, ProgressBar
from colors import GruvboxBright, GruvboxSoft


def game(screen):
    pygame.display.set_caption("⛹️  RicochetRush")

    oswald = pygame.font.Font("../assets/Oswald-Bold.ttf", 230)
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game(screen)
                elif event.key == pygame.K_q:
                    menu(screen)

        font_surf = oswald.render(f"{score}", True, GruvboxSoft().dark2)
        font_rect = font_surf.get_rect()
        font_rect.center = int(WIDTH / 2), int(HEIGHT / 2)

        screen.blit(font_surf, font_rect)

        # Progress Bar
        progressbar = ProgressBar(13, score, 15, GruvboxSoft().dark2, 25, screen)
        progressbar.draw()

        # Track Mouse
        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(screen, GruvboxSoft().white, mouse_position, MOUSE_RADIUS)

        # Check collisions & generates stars
        if helper.check_collisions(mouse_position, star_xy, STAR_RADIUS):
            score += 1
            star_xy = helper.generate_stars_cords(WIDTH, HEIGHT)

            if score != 0 and score % 3 == 0:
                speed += 1

                x, y = helper.generate_bouncy_cords(WIDTH, HEIGHT)

                ve = random.choice([True, False])
                vx, vy = speed + 2, speed + 1

                # If ve negative change flip the velocity
                vx = vx if ve else -vx
                vy = vy if ve else -vy

                color = GruvboxSoft().choose()

                bouncy.append(
                    BouncingBall(
                        x, y, vx, vy, BOUNCE_RADIUS, color, WIDTH, HEIGHT, screen
                    )
                )

        # For each bouncy ball
        # Update their position
        # draw them in their respective class:)
        for ball in bouncy:
            ball.update_position()
            ball.draw()

            if helper.check_collisions(mouse_position, ball.position(), BOUNCE_RADIUS):
                print(score)
                menu(screen)

        pygame.draw.circle(screen, GruvboxBright().yellow, star_xy, STAR_RADIUS)

        # Updates the whole screen & controls the FPS
        pygame.display.update()
        pygame.time.Clock().tick(60)


def menu(screen):
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

    for _ in range(60):
        x, y = random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10)
        bright, soft = GruvboxBright().choose(), GruvboxSoft().choose()
        color = random.choice([bright, soft])

        # Returns positive or negative
        ve = random.choice([True, False])

        # Picks a random velocity
        vx, vy = random.randint(4, 8), random.randint(4, 8)

        # If ve negative change flip the velocity
        vx = vx if ve else -vx
        vy = vy if ve else -vy

        bouncy.append(BouncingBall(x, y, vx, vy, 4, color, WIDTH, HEIGHT, screen))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                event.type == pygame.MOUSEBUTTONDOWN
            ):
                game(screen)

        screen.fill(GruvboxBright().dark1)

        ticks = pygame.time.get_ticks()
        oscillation = 15 * math.sin(ticks / 1000 * 2 * math.pi)

        for ball in bouncy:
            ball.update_position()
            ball.draw()

        logo_RECT.center = int(WIDTH / 2), 200 + int(oscillation)
        caption_RECT.center = int(WIDTH / 2), 50 + int(HEIGHT / 2)

        screen.blit(logo, logo_RECT)
        screen.blit(caption, caption_RECT) if helper.blink(475, ticks) else False

        pygame.display.flip()
        clock.tick(60)
