import random
import pygame


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

#Physics stuff
GRAVITY = 9.8
SPEED = 1

class Ball:
   def __init__(self, x, y, radius, color, dx=None, dy=None):
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color 
      self.dx = dx if dx is not None else random.randint(-5, 5)
      self.dy = dy if dy is not None else 0
      self.prev_time = pygame.time.get_ticks() / 1000

      def move(self):
         curr_time = pygame.time.get_ticks() / 1000
         delta_time = curr_time - self.prev_time

         self.dy += GRAVITY * delta_time

         self.x += self.dx * delta_time
         self.y += self.dy * delta_time

         if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.dx = -self.dx
         if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.dy = -self.dy * 0.8  # Slightly reduce the vertical speed on bounce

        # Update previous time
         self.prev_time = curr_time

      def draw(self, screen):
         pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
         

    

    