from __future__ import print_function
from PIL import Image, ImageDraw
import StringIO

BAR_BOTTOMX = 95
BAR_BOTTOMY = 187
BAR_TOPX_MAX = 105
BAR_TOPY_MAX = 22

def draw_rocket(percentage=0, flask=False):
    img = Image.open('sad-rocket.png')
#    img = Image.open('rocket.jpg')
#    image.show()

    percentage_diff = 100 - percentage
    print('percentage_diff', percentage_diff)

    pixel_range = BAR_BOTTOMY - BAR_TOPY_MAX
    percentage_height = ((pixel_range / 100.0) * percentage)
    print('percentage height:', percentage_height)

    bar_topy = BAR_BOTTOMY - percentage_height
    print('bar_topy', bar_topy)

    blank_image = img
    img_draw = ImageDraw.Draw(blank_image)
    img_draw.rectangle((95, 187, 105, bar_topy), outline='blue', fill='blue')

    if flask:
        img_io = StringIO.StringIO()
        blank_image.save(img_io, 'PNG', quality=100)
        return img_io
    else:
        return blank_image

if __name__ == '__main__':
    image = draw_rocket()
    image.show()
