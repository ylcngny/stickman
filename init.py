import pygame
import sys
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
head_center = (400, 200)
head_radius = 40
eye_radius = 5
mouth_radius = 10

# Animation parameters
blink_duration = 0.1  # Duration of each blink
talk_duration = 0.5  # Duration of each talking cycle

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Draw stickman head with eyes and mouth
    pygame.draw.circle(screen, black, head_center, head_radius)  # Head
    pygame.draw.circle(screen, blue, (head_center[0] - 15, head_center[1] - 10), eye_radius)  # Left eye
    pygame.draw.circle(screen, blue, (head_center[0] + 15, head_center[1] - 10), eye_radius)  # Right eye
    pygame.draw.circle(screen, black, (head_center[0], head_center[1] + 10), mouth_radius)  # Mouth

    # Blinking animation
    pygame.display.flip()
    time.sleep(blink_duration)

    pygame.draw.circle(screen, white, (head_center[0] - 15, head_center[1] - 10), eye_radius)  # Left eye (close)
    pygame.draw.circle(screen, white, (head_center[0] + 15, head_center[1] - 10), eye_radius)  # Right eye (close)
    pygame.display.flip()
    time.sleep(blink_duration)

    # Talking animation (mouth movement)
    pygame.draw.circle(screen, white, (head_center[0], head_center[1] + 10), mouth_radius)  # Clear mouth
    pygame.display.flip()
    time.sleep(talk_duration / 2)

    pygame.draw.circle(screen, black, (head_center[0], head_center[1] + 5), mouth_radius)  # Half open mouth
    pygame.display.flip()
    time.sleep(talk_duration / 2)

# Quit Pygame
pygame.quit()
sys.exit()
