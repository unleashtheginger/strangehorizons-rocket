from flask import Flask
from PIL import Image, ImageDraw

app = Flask(__name__)


@app.route('/rocket/')
def draw_rocket():
    im = Image.open("hopper.jpg")

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)
    del draw

    # write to stdout
    im.save(sys.stdout, "PNG")

@app.route('/')
def index():
    return 'Yo, it\'s working!'

if __name__ == "__main__":
    app.run()
