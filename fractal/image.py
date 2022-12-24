""" Image data class. """
from dataclasses import dataclass


@dataclass
class ImageRGB24:
    """ A 24-bit per pixel RGB image. """
    data: bytearray
    lines: int
    bytes_per_line: int
    bytes_per_pixel: int = 3

    def __init__(self, size: tuple[int, int]):
        self.lines = size[1]
        self.bytes_per_line = size[0] * self.bytes_per_pixel
