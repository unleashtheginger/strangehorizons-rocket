from flask import Flask, send_file
from PIL import Image, ImageDraw
import rocket

app = Flask(__name__)

@app.route('/rocket/')
@app.route('/rocket/<int:percentage>')
def draw_rocket(percentage=50):
    img_io = rocket.draw_rocket(percentage, flask=True)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/')
def index():
    return 'Yo, it\'s working!'

if __name__ == "__main__":
    app.run()
