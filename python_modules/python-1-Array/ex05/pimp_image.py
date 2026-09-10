import numpy as np

import matplotlib.pyplot as plt


fig, axes = plt.subplots(3, 2, figsize=(10, 15))

def Display(axes, arr, row, col, title):
    axes[row][col].imshow(arr, cmap="gray" if arr.ndim == 2 else None)
    axes[row][col].set_title(title)

def ft_invert(arr: np.array) -> np.array:
    """Inverts the color of the image received."""
    invert = 255 - arr
    Display(axes, invert, 0, 1, "Invert")
    return invert


def ft_red(arr: np.array) -> np.array:
    """Red the color of the image received."""
    red = arr.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    Display(axes, red, 1, 0, "Red")
    return red


def ft_green(arr: np.array) -> np.array:
    """Green the color of the image received."""
    green = arr.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    Display(axes, green, 1, 1, "Green")
    return green


def ft_blue(arr: np.array) -> np.array:
    """ Blue the color of the image received. """
    blue = arr.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    Display(axes, blue, 2, 0, "Blue")
    return blue


def ft_grey(arr: np.array) -> np.array:
    """ Gray the color of the image received. """
    gray = np.mean(arr, axis=2).astype(np.uint8)
    Display(axes, gray, 2, 1, "Gray")
    return gray
