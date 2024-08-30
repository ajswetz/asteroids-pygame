import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            #Already a small asteroid - no further splitting required
            return
        else:
            #Asteroid is med or large - need to split into two smaller asteroids
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            current_position = list(self.position)
            
            vector1 = self.velocity.rotate(random_angle)
            asteroid1 = Asteroid(current_position[0], current_position[1], new_radius)
            asteroid1.velocity = vector1 * 1.2
            
            vector2 = self.velocity.rotate(-random_angle)
            asteroid2 = Asteroid(current_position[0], current_position[1], new_radius)            
            asteroid2.velocity = vector2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt