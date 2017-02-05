import ILI9341 as TFT
from pyA20.gpio import connector
import time
import random

DC = connector.gpio1p26

disp = TFT.ILI9341(DC)  # Do not configure RST
disp.begin()
disp.clear((0, 0, 0))
draw = disp.draw()

random.seed()
while 1:
    # Draw white line on random positions
    draw.line((random.randint(0, disp.width), random.randint(0, disp.height),
               random.randint(0, disp.width), random.randint(0, disp.height)),
              fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    time.sleep(0.3)
    disp.display()
