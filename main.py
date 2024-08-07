import pygame
import sys
from Hollow_Poly_Class import *
from Ball_Behavior import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PolySound")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

font_name = pygame.font.get_default_font()  # Use default font
font_size = 36
font = pygame.font.Font(font_name, font_size)

def draw_text(surface, text, position, font, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    surface.blit(text_surface, text_rect)

sides = 3  
radius = 300
center = (width // 2, height // 2)

def main():
    ball_number = 1
    main_poly = Hollow_poly_class(screen, 'red', center, radius, sides)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_poly.sides += 1
                elif event.key == pygame.K_DOWN:
                    main_poly.sides = max(3, main_poly.sides - 1) 
                elif event.key == pygame.K_LEFT:
                    ball_number = max(1, ball_number - 1)
                elif event.key == pygame.K_RIGHT:
                    ball_number += 1
    

        # Clear screen
        screen.fill(white)
        draw_text(screen, f"Sides: {main_poly.sides}", (width // 2, height - 50), font, "black")
        draw_text(screen, f"Balls: {ball_number}", (width/2, height - 750), font, 'black')
        
        # Draw Poly and balls
        main_poly.draw_hollow_polygon()

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(30)

if __name__ == "__main__":
    main()

