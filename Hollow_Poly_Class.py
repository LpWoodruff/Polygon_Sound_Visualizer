import math
import pygame


class Hollow_poly_class:

    def __init__(self, surface, color, center, radius, sides, thickness=1):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.sides = sides
        self.thickness = thickness
     

    def get_sides(self):
        return self.sides


    def draw_hollow_polygon(self):
        points = []
        angle_step = 2 * math.pi / self.sides

        rotation_angle = math.pi / 2  # 90 degrees in radians

        for i in range(self.sides):
            angle = i * angle_step - rotation_angle
            x = self.center[0] + self.radius * math.cos(angle)
            y = self.center[1] + self.radius * math.sin(angle)
            points.append((x, y))
        pygame.draw.polygon(self.surface, self.color, points, width=self.thickness)