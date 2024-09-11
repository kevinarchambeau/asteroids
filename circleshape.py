import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collision(self, other_object) -> bool:
        distance = self.position.distance_to(other_object.position)
        overlap_range = self.radius + other_object.radius
        if distance <= overlap_range:
            return True
        return False
