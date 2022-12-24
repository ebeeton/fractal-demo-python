""" Plots the Mandelbrot set to an RGB image. """
import logging
import multiprocessing as mp
from scale import scale
from image import ImageRGB24
from parameters import FractalParameters
import mandelbrot

logger = logging.getLogger()


def init_process(data, img, params):
    """ Initialize the worker process' parameters. """
    mandelbrot.data = data
    mandelbrot.img = img
    mandelbrot.params = params


def _get_pixel(c: complex) -> int:
    """ Given a pixel as a point on the complex plane, returns 0 if the pixel
    is (probably) in the Mandelbrot set, or the number of iterations performed
    before escaping.
    """
    z = complex(0)
    for i in range(0, mandelbrot.params.max_iter):
        # https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set
        # "Because no complex number with a real or imaginary part greater
        # than 2 can be part of the set, a common bailout is to escape when
        # either coefficient exceeds 2."
        if abs(z) > 2:
            # Not in the set.
            return i
        z = z * z + c
    # "Probably" in the set.
    return 0


def _plot_line(line: int):
    """ Plots a single line of the Mandelbrot set. """
    # Imaginary part is the current line (Y coordinate) scaled to the
    # Mandelbrot set range.
    imag = scale(line, 0, mandelbrot.img.lines, mandelbrot.params.miny,
                 mandelbrot.params.maxy)
    for pix in range(0, mandelbrot.img.bytes_per_line,
                     mandelbrot.img.bytes_per_pixel):
        # Real part is scaled as above, but for X coordinates.
        real = scale(pix, 0, mandelbrot.img.bytes_per_line,
                     mandelbrot.params.minx,
                     mandelbrot.params.maxx)
        iterations = _get_pixel(complex(real, imag))
        if iterations == 0:
            # Leave points in the set black.
            continue

        # Simple grayscale coloring.
        val = int(iterations / mandelbrot.params.max_iter * 255)
        index = line * mandelbrot.img.bytes_per_line + pix
        mandelbrot.data[index] = val
        mandelbrot.data[index + 1] = val
        mandelbrot.data[index + 2] = val


def plot(img: ImageRGB24, params: FractalParameters):
    """ Plots the Mandelbrot set. """
    # https://stackoverflow.com/a/1721911
    data = mp.Array('B', img.lines * img.bytes_per_line)
    with mp.Pool(initializer=init_process,
                 initargs=(data, img, params)) as pool:
        pool.map(_plot_line, range(0, img.lines))
    img.data = data
