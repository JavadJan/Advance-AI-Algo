import numpy as np
from PIL import Image
from rotate import rotate, transpose
import matplotlib.pyplot as plt


def ft_gray(arr: np.array) -> np.array:
    """ convert the picture to gray, I need it  because the subject asked """
    gray = np.mean(arr, axis=2, keepdims=True).astype(np.uint8)
    return gray


def ft_display(arr: np.array, title="Image"):
    """ display the image woth matplotlib """
    plt.imshow(arr)
    plt.title(title)
    w, h = arr.shape[:2]
    plt.xlabel(f"X axis {w}")
    plt.ylabel(f"Y axis {h}")
    plt.show()


def ft_zoom(arr: np.array) -> np.array:
    """ zoom and resize the images """
    try:
        zoom = arr[200:600, 300:700]
        return zoom

    except Exception as e:
        print(f"Error during zoom: {e}")
        return None


def load_image(path: str) -> np.array:
    """ Load the image with pillow in python """
    img = Image.open(path)
    if img.format is None:
        raise OSError("File could not open")

    zoom = ft_zoom(np.array(img))

    gray = ft_gray(zoom)
    print(f"The shape of image is: {gray.shape}")
    print(gray)

    tras = transpose(gray)
    arr = np.array(tras)

    print(f"New shape after Transpose: {arr.shape}")
    rot = rotate(arr)
    print(np.array(rot))
    
    ft_display(np.array(rot))


def main():
    """ Program for rotation the image """
    try:
        load_image("animal.jpeg")
    except Exception as er:
        print(er)
        return 1


if __name__ == "__main__":
    main()
