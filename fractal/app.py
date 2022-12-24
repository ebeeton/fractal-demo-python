#!/usr/bin/env python3
""" Fractal generation demo. Copyright (C) 2021 Evan Beeton. """
from io import BytesIO
import logging
import time
from flask import Flask, Response, render_template
from PIL import Image
from config import Config
from fractal_form import FractalForm
from image import ImageRGB24
import mandelbrot
from parameters import FractalParameters

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    """ Default route. """
    form = FractalForm()
    return render_template('index.html', form=form)


@app.route('/mandelbrot/', methods=['POST'])
def plot_mandelbrot():
    """ Plots the Mandelbrot set. """
    form = FractalForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)

    params = FractalParameters(max_iter=form.max_iter.data)
    size = (form.width.data, form.height.data)
    img = ImageRGB24(size)

    logging.info(params)
    start = time.time()

    # Plot the set.
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
    logging.basicConfig(level=logging.INFO)
    app.run(debug=False, host='0.0.0.0')
