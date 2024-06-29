from CircleHandler import CircleHandler, AnimateCircleHandler
from LipHandler2 import LipPositionExtractor
from globs import *
import sys
from play import WAVPlayer
from voice.voice import VoiceHandler

text = "Please provide the answers to these questions so I can create a web page tailored to your preferences"
VoiceHandler().create(text)
myMap = LipPositionExtractor().extract_lip_positions(text)
print(myMap)

player = WAVPlayer('./voice/voice.wav')
skipTime = 600  # there are silence at the beginning and at the end
totalDur = player.get_duration() - (skipTime * 2 / 1000)
animDur = totalDur / len(myMap)
print("totalDur", totalDur, "totalChar", len(myMap), "animDur", animDur)

player.play(skip_time_ms=skipTime)

# Main loop
running = True
c = 0
while running:
    c += 1
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
    # CircleHandler().draw(black, mouthCenter, mouthRadius)  # Mouth

    # animation
    # AnimateCircleHandler().animate(black, leftEyeCenter, eyeRadius)  # Left eye blink
    # AnimateCircleHandler().animate(black, rightEyeCenter, eyeRadius)  # Right eye blink

    # write
    font = pygame.font.Font(None, 25)  # None uses the default font, 74 is the font size
    text_surface = font.render(text, True, black)
    screen.blit(text_surface, (headCenter[0]-385, headCenter[1] + 60))

    key = myMap[c]
    if key == "C":
        AnimateCircleHandler().animate(animDur, black, mouthCenter, mouthRadius)
    if key == "O":
        AnimateCircleHandler().animate(animDur, white, mouthCenter, mouthRadius)  # Half open mouth
    if key == "H":
        AnimateCircleHandler().animate(animDur, white, mouthCenter, mouthRadius/2)  # full open mouth

    if c >= len(myMap)-1:
        # Quit Pygame
        pygame.quit()
        sys.exit()
