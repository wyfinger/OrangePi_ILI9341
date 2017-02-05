import ILI9341 as TFT
from pyA20.gpio import connector
import time
from PIL import Image

DC = connector.gpio1p26
RST = connector.gpio1p28

disp = TFT.ILI9341(DC, RST)
disp.begin()

image = Image.open('cat.jpg')

# Resize the image and rotate it so it's 240x320 pixels.
image = image.rotate(270).resize((240, 320))

# Draw the image on the display hardware.
start_time = time.time()
disp.display(image)
end_time = time.time()
print('Time to draw image: ' + str(end_time - start_time))
