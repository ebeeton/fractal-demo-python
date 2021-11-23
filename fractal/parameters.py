""" Parameters used to generate fractals. """
from dataclasses import dataclass

@dataclass
class FractalParameters():
    """ Container for fractal generation parameters. """
    max_iter : int = 1000
    minx : float = -2
    maxx : float = 0.47
    miny : float = -1.12
    maxy : float = 1.12
