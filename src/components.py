import pygame
import colors

class BouncingBall:
    def __init__(self, x, y, vx, vy, radius, color, width, height, screen):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.radius = radius
        self.color = color

        self.width = width
        self.height = height

        self.screen = screen

    def speed_up(self):
        self.vx += 1
        self.vy += 1

    def update_position(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off screen edges
        if self.x - self.radius < 0 or self.x + self.radius > self.width:
            self.vx = -self.vx

        if self.y - self.radius < 0 or self.y + self.radius > self.height:
            self.vy = -self.vy

    def position(self):
        return self.x, self.y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class ProgressBar:
    def __init__(self, width, height, score, color, radius, screen):
        self.width = width - 100
        self.height = height

        self.score = score
        self.constant = int(width / 50)
        self.color = color
        self.radius = radius

        self.progress = 16 * self.score
        self.progressbar = pygame.Rect((25, 25), (self.progress, self.height))
        self.progressbar2 = pygame.Rect((25, 25), (16*50, self.height))
        self.progressbar.centerx = 450
        self.progressbar2.centerx = 450

        self.screen = screen

    def draw(self): 
        pygame.draw.rect(
            self.screen, self.color, self.progressbar, border_radius=self.radius
        )
