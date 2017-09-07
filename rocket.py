from __future__ import print_function
from copy import copy
from PIL import Image, ImageDraw
import StringIO

# The bulb's widest point to the left is 50p5090# The bulb's widest point to the right 90px

#BAR_BOTTOMX = 95
BAR_BOTTOMX = 46
#BAR_BOTTOMY = 187
BAR_BOTTOMY = 211
BAR_TOPX_MAX = 92
BAR_TOPY_MAX = 25

def draw_rocket(percentage=0, flask=False):
#    img = Image.open('sad-rocket.png')
    foreground = Image.open('rocket.png')
    foreground = foreground.convert('RGBA')
    x, y, = foreground.size
    background = Image.new('RGBA', (x, y), (255, 255, 255, 255))

#    image.show()

    percentage_diff = 100 - percentage
#    print('percentage_diff', percentage_diff)

    pixel_range = BAR_BOTTOMY - BAR_TOPY_MAX
    percentage_height = ((pixel_range / 100.0) * percentage)
#    print('percentage height:', percentage_height)

    bar_topy = BAR_BOTTOMY - percentage_height
#    print('bar_topy', bar_topy)

    img_draw = ImageDraw.Draw(background)
    img_draw.rectangle((BAR_BOTTOMX, BAR_BOTTOMY, BAR_TOPX_MAX, bar_topy),
                       outline='blue', fill='blue')
    background.paste(foreground, (0, 0), foreground)

    if flask:
        img_io = StringIO.StringIO()
        background.save(img_io, 'PNG', quality=100)
        return img_io
    else:
        return background

if __name__ == '__main__':
    image = draw_rocket()
    image.show()
