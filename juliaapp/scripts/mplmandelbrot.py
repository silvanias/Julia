import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


def pltrender(slug):
    input_color = str(slug)
    rgb_color = colors.to_rgb("#" + input_color)
    rgb_color = tuple(255*x for x in rgb_color)
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)
    membership = is_stable(c, num_iterations=20)

    # Create RGB array with the same shape as membership
    height, width = membership.shape
    rgb_array = np.zeros((height, width, 3), dtype=np.uint8)

    # Set RGB values based on membership
    rgb_array[membership, :] = [rgb_color[0], rgb_color[1], rgb_color[2]]
    # For points not in the set
    rgb_array[~membership, :] = [40, 40, 47] 

    plt.imshow(rgb_array, vmin=0, vmax=255)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html
    plt.axis("off")
    plt.tight_layout(h_pad=0, w_pad=0)
    return plt.plot()
