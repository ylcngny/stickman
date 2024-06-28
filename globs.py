import pygame
pygame.init()
# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stickman Animation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Define stickman head and components
head_center = (400, 200)
head_radius = 40
eye_radius = 5
mouth_radius = 10
