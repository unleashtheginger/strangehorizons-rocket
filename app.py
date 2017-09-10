from flask import Flask, send_file, request
from PIL import Image, ImageDraw
import rocket

app = Flask(__name__)

@app.route('/fullbox')
def draw_box(percentage=50):
    img_io = rocket.draw_box(percentage, flask=True)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/rocket/', methods=["POST"])
def draw_rocket(percentage=50):
@app.route('/rocket/<int:percentage>')
    target = float(request.form['target'])
    current = float(request.form['current'])

    if request.method == 'POST':
        percentage = int((100.0 / target) * current)

    img_io = rocket.draw_rocket(percentage, flask=True)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/rocket/', methods=["GET"])
@app.route('/')
def index():
    return '''<!doctype html>
    <title>Configure the Rocket!</title>
    <h1>Configure!</h1>
    <form method=post action='/rocket/'>
      <p>
    Target: <input type=text name=target value="16000">
</p>
<p>
    Current: <input type=text name=current value="5000">
</p>
<p>
         <input type=submit value=Upload>
</p>
    </form>
    '''
if __name__ == "__main__":
    app.run(debug=True)
