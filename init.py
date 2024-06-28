from CircleHandler import CircleHandler
from globs import *
import sys
import time

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
    CircleHandler().draw(black, head_center, head_radius)  # Head
    CircleHandler().draw(white, (head_center[0] - 15, head_center[1] - 10), eye_radius)  # Left eye
    CircleHandler().draw(white, (head_center[0] + 15, head_center[1] - 10), eye_radius)  # Right eye
    CircleHandler().draw(black, (head_center[0], head_center[1] + 10), mouth_radius)  # Mouth

    # Blinking animation
    pygame.display.flip()
    blink_duration = 0.1  # Duration of each blink
    time.sleep(blink_duration)

    CircleHandler().draw(black, (head_center[0] - 15, head_center[1] - eye_radius), eye_radius)  # Half open Left eye (close)
    CircleHandler().draw(black, (head_center[0] + 15, head_center[1] - eye_radius), eye_radius)  # Half open Right eye (close)
    pygame.display.flip()
    time.sleep(blink_duration)

    # Talking animation (mouth movement)
    CircleHandler().draw(white, (head_center[0], head_center[1] + mouth_radius), mouth_radius)  # Clear mouth
    pygame.display.flip()
    talk_duration = 0.5  # Duration of each talking cycle
    time.sleep(talk_duration / 2)

    CircleHandler().draw(black, (head_center[0], head_center[1] + mouth_radius/2), mouth_radius)  # Half open mouth
    pygame.display.flip()
    time.sleep(talk_duration / 2)

# Quit Pygame
pygame.quit()
sys.exit()
