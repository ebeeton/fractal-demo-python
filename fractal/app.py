#!/usr/bin/env python3
""" Fractal generation demo. Copyright (C) 2021 Evan Beeton. """
from io import BytesIO
import logging
import time
from flask import Flask, Response
from PIL import Image
from image import ImageRGB24
import mandelbrot
from parameters import FractalParameters

app = Flask(__name__)

@app.route('/')
def index():
    """ Default route. """
    return '<p>Hello, world!</p>'

@app.route('/image')
def test_image():
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

@app.route('/mandelbrot')
def draw_mandelbrot():
    """ Draws the Mandelbrot set. """
    start = time.time()

    size = (800, 800)
    img = ImageRGB24(size)
    params = FractalParameters()
    mandelbrot.plot(img, params)

    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.frombuffer
    mode = 'RGB'
    img = Image.frombuffer(mode, size, bytes(img.data), 'raw', mode, 0, 1)
    img_bytes = BytesIO()
    img.save(img_bytes, 'PNG')
    img_bytes.seek(0)

    end = time.time()
    app.logger.info("Render took %.2f sec.", end - start)
    return Response(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    app.run(debug=False, host='0.0.0.0')
