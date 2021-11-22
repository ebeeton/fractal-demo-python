""" Plots the Mandelbrot set to an RGB image. """
import logging
from scale import scale

class Mandelbrot():
    """ Mandelbrot set plotter. """
    bytes_per_pixel = 3
    minx = -2
    maxx = 0.47
    miny = -1.12
    maxy = 1.12

    logger = logging.getLogger(__name__)

    def __init__(self, size, max_iter):
        self.lines = size[1]
        self.bytes_per_line = size[0] * self.bytes_per_pixel
        self.img = bytearray(self.lines * self.bytes_per_line)
        self.max_iter = max_iter
        self.logger.info('Lines: %d bytes per line: %d.',
                         self.lines,
                         self.bytes_per_line)

    def get_pixel(self, c):
        """ Gets an RGB value given the pixel as a complex number. """
        z = complex(0)
        for i in range(0, self.max_iter):
            # https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set
            # "Because no complex number with a real or imaginary part greater
            # than 2 can be part of the set, a common bailout is to escape when
            # either coefficient exceeds 2."
            if abs(z) > 2:
                # Not in the set.
                return int(i / self.max_iter * 255)
            z = z * z + c
        # "Probably" in the set.
        return 0

    def plot_line(self, line):
        """ Plots a single line of the Mandelbrot set. """
        # Imaginary part is the current line (Y coordinate) scaled to the
        # Mandelbrot set range.
        imag = scale(line, 0, self.lines, self.miny, self.maxy)
        for pix in range(0, self.bytes_per_line, self.bytes_per_pixel):
            # Real part is scaled as above, but for X coordinates.
            real = scale(pix, 0, self.bytes_per_line, self.minx, self.maxx)
            val = self.get_pixel(complex(real, imag))
            #self.img[line * self.bytes_per_line + pix] = 255
            index = line * self.bytes_per_line + pix
            self.img[index] = val
            self.img[index + 1] = val
            self.img[index + 2] = val

    def plot(self):
        """ Plots the Mandelbrot set. """
        for line in range(0, self.lines):
            self.plot_line(line)

        return bytes(self.img)
