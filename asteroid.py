import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = self.velocity.rotate(angle) * 1.2

            second = Asteroid(self.position.x, self.position.y, new_radius)
            second.velocity = self.velocity.rotate(-angle) * 1.2
