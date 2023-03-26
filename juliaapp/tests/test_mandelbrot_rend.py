import unittest
import numpy as np
import matplotlib.pyplot as plt
from juliaapp.scripts.mplmandelbrot import complex_matrix, is_stable, get_members, pltrender

class TestMandelbrot(unittest.TestCase):

    def test_pltrender(self):
        c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
        plt.imshow(is_stable(c, num_iterations=20), cmap="binary")
        plt.gca().set_aspect("equal")
        plt.axis("off")
        plt.tight_layout()
        self.assertEqual(plt.plot(), pltrender())
     

if __name__ == '__main__':
    unittest.main()