import pygame
import random

def generate_stars_cords(width, height):
    x = random.randint(150, width - 150)
    y = random.randint(150, height - 150)

    return x, y 

def check_collisions(circle1, circle2, target_radius):
    distance = pygame.math.Vector2(circle1[0] - circle2[0], circle1[1] - circle2[1]).length()
    return 2 * target_radius > distance

def generate_bouncy_cords(width, height):
    top = random.randint(25, 75)
    bottom = random.randint(height - 75, height - 25)

    left = random.randint(24, 75)
    right = random.randint(width - 75, width - 25)

    x = random.choice([left, right])
    y = random.choice([top, bottom])
    
    return x, y

def blink(blink_speed, current_time):
    visible = (current_time // blink_speed) % 2 == 0
    return visible
