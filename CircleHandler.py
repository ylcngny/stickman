from globs import *


class CircleHandler:
    def __init__(self):
        pass

    def draw(self, color, center, raius):
        pygame.draw.circle(screen, color, center, raius)


class AnimateCircleHandler:
    def __init__(self):
        pass

    def animate(self, color, center, radius):
        CircleHandler().draw(white, center, radius)  # Clear
        pygame.display.flip()
        blink_duration = 0.2  # Duration of each blink
        time.sleep(blink_duration)
        CircleHandler().draw(color, (center[0], center[1]+radius/2), radius)
        pygame.display.flip()
        time.sleep(blink_duration)

