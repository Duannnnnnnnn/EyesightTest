import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

def display_text(text, *args):

    if len(args) < 2:
        FONT_SIZE = 15
    elif len(args) == 2:
        FONT_SIZE = 10
    else:
        FONT_SIZE = 8

    disp = Adafruit_SSD1306.SSD1306_128_32(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height

    # 1 bit pixel
    image = Image.new('1', (width, height))
    # Create a new image (all black) with the binary mode

    draw = ImageDraw.Draw(image)
    # Create an object that can be used to draw in the given image

    font = ImageFont.truetype(r"/home/pi/Rpi_latest/lecture4_ultrasonic_OLED/oled/ARIALUNI.TTF", FONT_SIZE)

    try:
        print('Press ^C to terminate')
        while True:
            draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
            
            draw.text((0, 0), text, font = font, fill = 255)

            if len(args) > 0:
                for i, item in enumerate(args):
                    draw.text((0, (i + 1) * FONT_SIZE-1), item, font = font, fill = 255)

            disp.image(image)
            disp.display()
            time.sleep(0.2)

    except KeyboardInterrupt:
        print('terminated')

    finally:
        disp.clear()
        disp.display()

if __name__ == "__main__":
    # display_text('一二三四五六七八九', '一二三四五六七八九', '一二三四五六七八九', '一二三四五六七八九')
    display_text('你的度數是')
