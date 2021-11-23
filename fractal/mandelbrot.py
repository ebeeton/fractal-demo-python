""" Plots the Mandelbrot set to an RGB image. """
from scale import scale
from image import ImageRGB24
from parameters import FractalParameters

def _get_pixel(params : FractalParameters, c : complex) -> int:
    """ Given a pixel as a point on the complex plane, returns 0 if the pixel
    is (probably) in the Mandelbrot set, or the number of iterations performed
    before escaping.
    """
    z = complex(0)
    for i in range(0, params.max_iter):
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

def _plot_line(img : ImageRGB24, params : FractalParameters, line : int):
    """ Plots a single line of the Mandelbrot set. """
    # Imaginary part is the current line (Y coordinate) scaled to the
    # Mandelbrot set range.
    imag = scale(line, 0, img.lines, params.miny, params.maxy)
    for pix in range(0, img.bytes_per_line, img.bytes_per_pixel):
        # Real part is scaled as above, but for X coordinates.
        real = scale(pix, 0, img.bytes_per_line, params.minx, params.maxx)
        iterations = _get_pixel(params, complex(real, imag))
        if iterations == 0:
            # Leave points in the set black.
            continue

        # Simple grayscale coloring.
        val = int(iterations / params.max_iter * 255)
        index = line * img.bytes_per_line + pix
        img.data[index] = val
        img.data[index + 1] = val
        img.data[index + 2] = val

def plot(img : ImageRGB24, params : FractalParameters):
    """ Plots the Mandelbrot set. """
    for line in range(0, img.lines):
        _plot_line(img, params, line)
