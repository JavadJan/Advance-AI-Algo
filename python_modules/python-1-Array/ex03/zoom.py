import numpy as np


def ft_zoom(arr: np.array) -> np.array:
    """ zoom and resize the images """
    try:
        zoom = arr[200:600, 300:700]
        return zoom

    except Exception as e:
        print(f"Error during zoom: {e}")
        return None
