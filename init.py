from LipHandler import LipHandler

from CircleHandler import CircleHandler, AnimateCircleHandler
from LipHandler2 import LipPositionExtractor
from globs import *
import sys
from play import WAVPlayer

text = "Lets review the code and see if there are any improvements or adjustments that can be made"
myMap = LipHandler().getMap(text)
myMap = LipPositionExtractor().extract_lip_positions(text)
print(myMap)

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
    # AnimateCircleHandler().animate(black, leftEyeCenter, eyeRadius)  # Left eye blink
    # AnimateCircleHandler().animate(black, rightEyeCenter, eyeRadius)  # Right eye blink
    player = WAVPlayer('audio.wav')
    skipTime = 600 # there are silence at the beginning and at the end
    totalDur = player.get_duration()-(skipTime*2/1000)
    animDur = totalDur / len(myMap)
    print("totalDur", totalDur, "totalChar", len(myMap), "animDur", animDur)

    player.play(skip_time_ms=skipTime)
    # time.sleep(1)  # silence at the beginning

    # write
    font = pygame.font.Font(None, 25)  # None uses the default font, 74 is the font size
    text_surface = font.render(text, True, black)
    screen.blit(text_surface, (headCenter[0]-385, headCenter[1] + 60))

    for key in myMap:
        if key == "H":
            continue
        if key == "C":
            AnimateCircleHandler().animate(animDur, black, mouthCenter, mouthRadius)  # Half open mouth
        if key == "O":
            AnimateCircleHandler().animate(animDur, white, mouthCenter, mouthRadius)  # full open mouth

    # Quit Pygame
    pygame.quit()
    sys.exit()
