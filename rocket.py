from __future__ import print_function
from copy import copy
from PIL import Image, ImageDraw, ImageFont
import StringIO
import cairo

BLACK = (0,0,0)
WHITE = (255, 255, 255)

# The bulb's widest point to the left is 50p5090# The bulb's widest point to the right 90px

#BAR_BOTTOMX = 95
BAR_BOTTOMX = 46
#BAR_BOTTOMY = 187
BAR_BOTTOMY = 211
BAR_TOPX_MAX = 92
BAR_TOPY_MAX = 25

def draw_box(percentage=0, flask=False):
    background = Image.open('fullbox.png')
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('./assets/SourceSansPro-Regular.ttf', 16)

    draw.text((0,0), 'Strange Horizons', (0,0,0), font=font)

    background = Image.new('RGBA', (145, 385), (255, 255, 255))
    text = Image.new('RGBA', background.size, (255, 255, 255, 0))

    fnt = ImageFont.truetype('./assets/FreeMono.ttf', 30)
    d = ImageDraw.Draw(text)

    text_string = str(percentage) + '%'
    d.text((10,10), text_string, font=fnt, fill=BLACK)

    background = Image.alpha_composite(background, text)

    if flask:
        img_io = StringIO.StringIO()
        background.save(img_io, 'PNG', quality=100)
        return img_io
    else:
        return background

    return background

def draw_rocket(percentage=0, flask=False):
#    img = Image.open('sad-rocket.png')
    foreground = Image.open('rocket.png')
    foreground = foreground.convert('RGBA')
    x, y, = foreground.size
    background = Image.new('RGBA', (x, y + 100), (255, 255, 255, 255))

    pixel_range = BAR_BOTTOMY - BAR_TOPY_MAX
    percentage_height = ((pixel_range / 100.0) * percentage)

    bar_topy = BAR_BOTTOMY - percentage_height

    img_draw = ImageDraw.Draw(background)
    img_draw.rectangle((BAR_BOTTOMX, BAR_BOTTOMY, BAR_TOPX_MAX, bar_topy),
                       outline='blue', fill='blue')

    text = Image.new('RGBA', background.size, (255, 255, 255, 0))
    font = ImageFont.truetype('./assets/SourceSansPro-Regular.ttf', 50)
    draw = ImageDraw.Draw(text)
    text_string = str(percentage) + '%'
    draw.text((20, 300), text_string, font=font, fill=BLACK)
    draw.text((20, 300), text_string, font=font, fill=BLACK)

    background = Image.alpha_composite(background, text)
    background.paste(foreground, (0, 0), foreground)

    if flask:
        img_io = StringIO.StringIO()
        background.save(img_io, 'PNG', quality=95)
        return img_io
    else:
        return background

if __name__ == '__main__':
#    image = draw_rocket()
#    image.show()
    image = draw_box(flask=False)
    image.show()
