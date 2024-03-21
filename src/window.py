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
    oswald50 = pygame.font.Font("../assets/Oswald-Bold.ttf", 50)

    WIDTH, HEIGHT = screen.get_width(), screen.get_height()

    bouncy = []

    score = 0
    vx = vy = 3
    life_count = 3
    game_active = True
    deduct_life = False

    star_xy = helper.generate_stars_cords(WIDTH, HEIGHT)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game(screen)
                    elif event.key == pygame.K_m:
                        menu(screen)

            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r or pygame.K_SPACE:
                        game(screen)

                    elif event.key == pygame.K_m:
                        menu(screen)

                    elif event.key == pygame.K_e:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game(screen)

        screen.fill(GruvboxSoft().dark1)

        if game_active:
            ticks = pygame.time.get_ticks()

            # Write Score at the center of the screen
            scored = oswald.render(f"{score}", True, GruvboxSoft().dark2)
            scored_RECT = scored.get_rect()
            scored_RECT.center = int(WIDTH / 2), int(HEIGHT / 2)

            screen.blit(scored, scored_RECT)

            # Progress Bar
            progressbar = ProgressBar(
                width=WIDTH,
                height=13,
                score=score,
                color=GruvboxSoft().dark2,
                radius=15,
                screen=screen,
            )
            progressbar.draw()

            # Lives
            for i in range(life_count):
                lives_rect = pygame.Rect(20 + 50 * i, HEIGHT - 50, 30, 30)
                pygame.draw.rect(screen, GruvboxSoft().red, lives_rect)

            # Track Mouse
            mouse_xy = pygame.mouse.get_pos()
            pygame.draw.circle(screen, GruvboxSoft().white, mouse_xy, MOUSE_RADIUS)

            # Check collisions & generates stars
            if helper.check_collisions(mouse_xy, star_xy, STAR_RADIUS):
                score += 1
                star_xy = helper.generate_stars_cords(WIDTH, HEIGHT)

                if score != 0 and score % 3 == 0:
                    x, y = helper.generate_bouncy_cords(WIDTH, HEIGHT)
                    color = GruvboxSoft().choose()

                    bouncy.append(
                        BouncingBall(
                            x,
                            y,
                            vx,
                            vy,
                            BOUNCE_RADIUS,
                            color,
                            WIDTH,
                            HEIGHT,
                            screen,
                        )
                    )

                if score != 0 and score % 10 == 0:
                    vx += 1
                    vy += 1

                    # For each ball in bouncy check their velocity using ball.vx/vy
                    # If ball.vx is negative then we add negative velocity
                    # If it is positive we add positive velocity
                    for ball in bouncy:
                        ball.vx = vx if ball.vx > 0 else -vx
                        ball.vy = vy if ball.vy > 0 else -vy

            # For each bouncy ball, update their position and draw them in the screen
            for ball in bouncy:
                ball.update_position()
                ball.draw()

                if helper.check_collisions(mouse_xy, ball.position(), BOUNCE_RADIUS):
                    deduct_life = True
                    bouncy.remove(ball)
                    life_count -= 1 if deduct_life else 0
                    game_active = False if life_count <= 0 else True

            # Draw the star
            pygame.draw.circle(screen, GruvboxBright().yellow, star_xy, STAR_RADIUS)

        else:
            ticks = pygame.time.get_ticks()
            over = oswald50.render(
                f"Game Over! Your Score: {score}!", True, GruvboxSoft().yellow
            )
            over_RECT = over.get_rect()

            # y = 15 * sin(time / 1000 * frequency * pi)
            y = 15 * math.sin(ticks / 1000 * 2 * math.pi)
            over_RECT.center = (WIDTH / 2, HEIGHT / 2 + int(y))

            screen.blit(over, over_RECT)

        # Updates the whole screen & controls the FPS
        pygame.display.update()
        pygame.time.Clock().tick(60)


def menu(screen):
    pygame.display.set_caption("⛹️  RicochetRush")
    clock = pygame.time.Clock()

    oswald = helper.load_font("Bold", 90)
    oswald_40 = helper.load_font("Bold", 40)

    logo = oswald.render("RicochetRush", True, GruvboxBright().blue)
    logo_RECT = logo.get_rect()

    caption = oswald_40.render("PRESS SPACE TO START!", True, GruvboxBright().light2)
    caption_RECT = caption.get_rect()

    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    bouncy = []

    for _ in range(65):
        x, y = random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10)
        bright, soft = GruvboxBright().choose(), GruvboxSoft().choose()
        color = random.choice([bright, soft])

        # Returns positive or negative
        ve = random.choice([True, False])

        # Picks a random velocity
        vx, vy = random.randint(1, 3), random.randint(1, 3)

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

        logo_RECT.center = int(WIDTH / 2), -50 + int(HEIGHT / 2) + int(oscillation)
        caption_RECT.center = int(WIDTH / 2), 50 + int(HEIGHT / 2)

        screen.blit(logo, logo_RECT)
        screen.blit(caption, caption_RECT) if helper.blink(375, ticks) else False

        pygame.display.flip()
        clock.tick(60)
