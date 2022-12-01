import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 150)
pixels[0] = (255, 0, 0)

for x in range(9):
    pixels[x] = (255, 0, 0)
    time.sleep(1)

# pixels.fill((0, 255, 0))