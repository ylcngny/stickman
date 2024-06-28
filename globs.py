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

# Define stickman head and components
headCenter = (400, 200)
headRadius = 40

eyeRadius = 5
leftEyeCenter = (headCenter[0] - 15, headCenter[1])
rightEyeCenter = (headCenter[0] + 15, headCenter[1])

mouthRadius = 10
mouthCenter = (headCenter[0], headCenter[1] + mouthRadius*2)
