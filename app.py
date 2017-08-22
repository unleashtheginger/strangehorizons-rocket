from flask import Flask, send_file
from PIL import Image, ImageDraw
import rocket

app = Flask(__name__)


@app.route('/rocket')
def draw_rocket():
    img_io = rocket.draw_rocket(flask=True)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/')
def index():
    return 'Yo, it\'s working!'

if __name__ == "__main__":
    app.run()
