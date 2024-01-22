import pygame


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
    def __init__(self, height, points, constant, color, radius, screen):
        self.height = height
        self.points = points
        self.constant = constant
        self.color = color
        self.radius = radius

        self.progress_width = self.constant * self.points
        self.progressbar = pygame.Rect((25, 25), (self.progress_width, self.height))

        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen, self.color, self.progressbar, border_radius=self.radius
        )
