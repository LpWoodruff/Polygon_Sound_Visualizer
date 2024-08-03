import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hollow Polygon Drawer")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

def draw_hollow_polygon(surface, color, center, radius, sides, thickness=1):
    """Draw a hollow polygon with a specified number of sides."""
    points = []
    angle_step = 2 * math.pi / sides
    for i in range(sides):
        angle = i * angle_step
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    pygame.draw.polygon(surface, color, points, width=thickness)

def main():
    sides = 3  # Start with a triangle
    radius = 100
    center = (width // 2, height // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    sides += 1
                elif event.key == pygame.K_DOWN:
                    sides = max(3, sides - 1)  # Minimum sides is 3 (triangle)

        # Clear screen
        screen.fill(white)

        # Draw the hollow polygon
        draw_hollow_polygon(screen, black, center, radius, sides, thickness=2)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()

