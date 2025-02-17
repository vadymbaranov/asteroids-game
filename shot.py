import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "purple", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

