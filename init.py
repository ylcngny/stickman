import time

from CircleHandler import CircleHandler, AnimateCircleHandler
from globs import *
import sys
from play import WAVPlayer
# from voice.voice import VoiceHandler
# from LipHandler2 import LipPositionExtractor

text = "Lets review the code and see if there are any improvements or adjustments that can be made"
# VoiceHandler().create(text)
# myMap = LipPositionExtractor().extract_lip_positions(text)
myMap = [['Lets', ['C', 'O', 'C', 'H']], ['review', ['C', 'O', 'H', 'C', 'O']], ['the', ['H', 'O']], ['code', ['C', 'O', 'C']], ['and', ['O', 'C', 'C']], ['see', ['H', 'O']], ['if', ['O', 'H']], ['there', ['H', 'O', 'C']], ['are', ['O', 'C']], ['any', ['O', 'C', 'O']], ['improvements', ['O', 'C', 'C', 'C', 'O', 'H', 'C', 'O', 'C', 'C', 'H']], ['or', ['O', 'C']], ['adjustments', ['O', 'H', 'O', 'H', 'C', 'C', 'O', 'C', 'C', 'H']], ['that', ['H', 'O', 'C']], ['can', ['C', 'O', 'C']], ['be', ['C', 'O']], ['made', ['C', 'O', 'C']]]
print(myMap)

player = WAVPlayer('./voice/voice.wav')
skipTime = 400  # there are silence at the beginning and at the end
totalDur = player.get_duration() - (skipTime * 2 / 1000)
totalPhonemes = sum(len(item[1]) for item in myMap)
animDur = totalDur / totalPhonemes
print("totalDur", totalDur, "totalChar", totalPhonemes, "animDur", animDur)

player.play(skip_time_ms=skipTime)

# Main loop
running = True
c = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # animation
    # AnimateCircleHandler().animate(black, leftEyeCenter, eyeRadius)  # Left eye blink
    # AnimateCircleHandler().animate(black, rightEyeCenter, eyeRadius)  # Right eye blink

    posMap = myMap[c][1]
    for key in posMap:
        # Clear the screen
        screen.fill(white)
        # write
        word = myMap[c][0]
        font = pygame.font.Font(None, 25)  # None uses the default font
        text_surface = font.render(word, True, black)
        screen.blit(text_surface, (headCenter[0] - 25, headCenter[1] + 90))
        # animate
        AnimateCircleHandler().animate(key, animDur)
    c += 1

    if c >= len(myMap):
        time.sleep(5)
        # Quit Pygame
        pygame.quit()
        sys.exit()

