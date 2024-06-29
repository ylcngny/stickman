import pygame
import time
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
red = (255, 0, 0)

# Define stickman head and components
headCenter = (400, 150)
headRadius = 60

eyeRadius = 10
leftEyeCenter = (headCenter[0] - 30, headCenter[1] -5)
rightEyeCenter = (headCenter[0] + 30, headCenter[1]-5)

mouthRadius = 20
mouthCenter = (headCenter[0], headCenter[1] + 10)
