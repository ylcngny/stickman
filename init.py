from CircleHandler import CircleHandler, AnimateCircleHandler
from globs import *
import sys

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
    CircleHandler().draw(black, headCenter, headRadius)  # Head
    CircleHandler().draw(white, leftEyeCenter, eyeRadius)  # Left eye
    CircleHandler().draw(white, rightEyeCenter, eyeRadius)  # Right eye
    CircleHandler().draw(black, mouthCenter, mouthRadius)  # Mouth

    # animation
    AnimateCircleHandler().animate(black, leftEyeCenter, eyeRadius)  # Left eye blink
    AnimateCircleHandler().animate(black, rightEyeCenter, eyeRadius)  # Right eye blink
    AnimateCircleHandler().animate(black, mouthCenter, mouthRadius)  # Half open mouth


# Quit Pygame
pygame.quit()
sys.exit()
