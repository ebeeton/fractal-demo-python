import unittest

from fractal import scale

class TestScale(unittest.TestCase):
    minx = 0
    maxx = 1024
    minscalex = -2
    maxscalex = 0.47

    def test_min(self):
        """ Tests the minimum end of the scaling range. """
        result = scale.scale(0,
                             self.minx,
                             self.maxx,
                             self.minscalex,
                             self.maxscalex)

        self.assertAlmostEqual(result, -2)

    def test_max(self):
        """ Tests the maximum end of the scaling range. """
        result = scale.scale(1024,
                             self.minx,
                             self.maxx,
                             self.minscalex,
                             self.maxscalex)

        self.assertAlmostEqual(result, 0.47)
