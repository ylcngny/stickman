from globs import *


class CircleHandler:
    def __init__(self):
        pass

    def draw(self, color, center, raius):
        pygame.draw.circle(screen, color, center, raius)


class AnimateCircleHandler:
    def __init__(self):
        pass

    def animate(self, animDur, color, center, radius):
        # CircleHandler().draw(white, center, radius)  # Clear
        # pygame.display.flip()
        # animDur = animDur/2
        # time.sleep(animDur)
        CircleHandler().draw(color, (center[0], center[1]+radius), radius)
        pygame.display.flip()
        time.sleep(animDur)

