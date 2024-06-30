from globs import *


class CircleHandler:
    def __init__(self):
        pass

    def draw(self, color, center, radius):
        pygame.draw.circle(screen, color, center, radius)


class AnimateCircleHandler:
    def __init__(self):
        pass

    def animate(self, posKey, animDur):
        self.drawRest()
        if posKey == "C":
            pygame.draw.line(screen, white, (mouthCenter[0] - mouthRadius, mouthCenter[1] + mouthRadius),
                             (mouthCenter[0] + mouthRadius, mouthCenter[1] + mouthRadius), 5)
        elif posKey == "O":
            self.animate2(white, mouthCenter, mouthRadius)
        elif posKey == "H":
            self.animate2(red, (mouthCenter[0], mouthCenter[1] + mouthRadius),
                          mouthRadius / 2)

        pygame.display.flip()
        time.sleep(animDur)

    def animate2(self, color, center, radius):
        CircleHandler().draw(color, (center[0], center[1] + radius), radius)
        # pygame.display.flip()
        # time.sleep(animDur)

    def drawRest(self):
        # Draw stickman head with eyes and mouth
        CircleHandler().draw(black, headCenter, headRadius)  # Head
        CircleHandler().draw(white, leftEyeCenter, eyeRadius)  # Left eye
        CircleHandler().draw(white, rightEyeCenter, eyeRadius)  # Right eye
        # CircleHandler().draw(black, mouthCenter, mouthRadius)  # Mouth

