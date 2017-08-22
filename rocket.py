from PIL import Image, ImageDraw

BAR_BOTTOMX = 95
BAR_BOTTOMY = 187
BAR_TOPX_MAX = 105
BAR_TOPY_MAX = 22

def draw_rocket(percentage=0):
    img = Image.open('test-rocket.png')
#    image.show()

    bar_topy = 51
    blank_image = img
    img_draw = ImageDraw.Draw(blank_image)
    img_draw.rectangle((95, 187, 105, bar_topy), outline='blue', fill='blue')

    return blank_image

if __name__ == '__main__':
    image = draw_rocket()
    image.show()
