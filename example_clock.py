import ILI9341 as TFT
from pyA20.gpio import connector
import time
from PIL import ImageFont

DC = connector.gpio1p26

disp = TFT.ILI9341(DC)  # Do not configure RST
disp.begin()
disp.clear((0, 0, 0))
draw = disp.draw()

# Load default font.
timeFont = ImageFont.truetype("times.ttf", size=64)
dayFont = ImageFont.truetype("times.ttf", size=22)

while 1:
    disp.clear((0, 0, 0))
    # Draw time
    timeText = time.strftime("%H:%M:%S", time.localtime())
    timeWidth, timeHeight = draw.textsize(timeText, font=timeFont)
    dayText = time.strftime("%Y-%m-%d %A, %b", time.localtime())
    dayWidth, dayHeight = draw.textsize(dayText, font=dayFont)
    draw.text(((disp.width-timeWidth)/2,50), timeText, font=timeFont, fill=(255,255,255))
    draw.text(((disp.width-dayWidth)/2,110), dayText, font=dayFont, fill=(150,150,150))
    disp.display()
    time.sleep(0.2)