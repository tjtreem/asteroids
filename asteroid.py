from circleshape import CircleShape
import pygame
import random
import math
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity if velocity is not None else pygame.Vector2(0,0) 
        self.radius = radius
        self.vertices = []
        num_vertices = random.randint(7, 12)  # Between 7 and 12 points
        for i in range(num_vertices):
            angle = 2 * math.pi * i / num_vertices
            # Vary the radius a bit for each vertex
            distance = self.radius * random.uniform(0.75, 1.0)
            x_offset = math.cos(angle) * distance
            y_offset = math.sin(angle) * distance
            self.vertices.append((x_offset, y_offset))

    def collides_with(self, other):
        distance = pygame.math.Vector2(self.position - other.position).length()
        return distance < self.radius + other.radius
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
    
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
    
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, velocity2)

        # Return the new asteroids (they'll automatically be added to groups via containers)
        return [asteroid1, asteroid2]

    def draw(self, screen):
        points = []
        for vertex in self.vertices:
            point_x = self.position.x + vertex[0]
            point_y = self.position.y + vertex[1]
            points.append((point_x, point_y))
    
    # Draw the polygon
        pygame.draw.polygon(screen, "white", points, 2)  # 2 is the line width

    def update(self, dt):
        self.position += self.velocity * dt    
