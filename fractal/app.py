#!/usr/bin/env python3
""" Fractal generation demo. Copyright (C) 2021 Evan Beeton. """
from io import BytesIO
from flask import Flask, Response
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    """ Default route. """
    return '<p>Hello, world!</p>'

@app.route('/image')
def image():
    """ Draws a test image. """
    size = (320, 240)
    buf = bytearray(size[0] * size[1] * 3)
    for i in range(0, len(buf), 3):
        buf[i] = 255

    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.frombuffer
    mode = 'RGB'
    img = Image.frombuffer(mode, size, bytes(buf), 'raw', mode, 0, 1)
    img_bytes = BytesIO()
    img.save(img_bytes, 'PNG')
    img_bytes.seek(0)
    return Response(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.logger.setLevel("INFO")
    app.run(debug=False, host='0.0.0.0')
