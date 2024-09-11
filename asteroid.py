import pygame
import random

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        medium = ASTEROID_MAX_RADIUS * .67
        small = ASTEROID_MAX_RADIUS * .34
        # roughly indicating asteroid size by color
        if self.radius >= medium:
            color = "red"
        elif self.radius >= small:
            color = "yellow"
        else:
            color = "blue"
        pygame.draw.circle(screen, color, self.position, self.radius, 2)

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
