import sys
import pygame

import helper
from components import BouncingBall, ProgressBar

from colors import GruvboxBright, GruvboxSoft

# Initialize Pygame
pygame.init()

# Setting screen display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RicochetRush')

# Constants
mouse_radius = 12
bounce_radius = 10
star_radius = 15

oswald = pygame.font.Font("./assets/Oswald-Bold.ttf", 230)
w, h = screen.get_width(), screen.get_height()

print(w, h)

score = 1
speed = 1
bouncy = []
star_xy = helper.generate_stars_cords(width, height)

# Main game loop
while True:
    screen.fill(pygame.Color("#282828"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    font_surf = oswald.render(f"{score}", True, GruvboxSoft().dark2)
    font_rect = font_surf.get_rect()
    font_rect.center = int(width/2), int(height/2)

    screen.blit(font_surf, font_rect)

    # Progress Bar
    progressbar = ProgressBar(13, score, 15, GruvboxSoft().dark2, 25, screen)
    progressbar.draw()

    # Track Mouse
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.circle(screen, GruvboxSoft().white, mouse_position, mouse_radius)

    # Check collisions & generates stars
    if helper.check_collisions(mouse_position, star_xy, star_radius):
        score += 1
        star_xy = helper.generate_stars_cords(width, height)

        if score != 0 and score % 3 == 0:
            speed += 1
            x, y = helper.generate_bouncy_cords(width, height)
            vx, vy = speed + 2, speed + 1
            color = GruvboxSoft().choose()

            bouncy.append(BouncingBall(x, y, vx, vy, bounce_radius, color, width, height, screen))
    
    # For each bouncy ball
    # Update their position and draw them in their respective class:)
    for ball in bouncy:
        ball.update_position()
        ball.draw()

        if helper.check_collisions(mouse_position, ball.position(), bounce_radius):
            print(score)
            pygame.quit()
            sys.exit()

    pygame.draw.circle(screen, GruvboxBright().yellow, star_xy, star_radius)

    # Updates the whole screen & controls the FPS
    pygame.display.update()
    pygame.time.Clock().tick(60)
