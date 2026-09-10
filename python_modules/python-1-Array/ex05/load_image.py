import numpy as np
from PIL import Image
from pimp_image import axes, Display


def ft_load(path: str) -> np.array:
    """ Load image, from given path """
    try:
        img = Image.open(path)
        if img.format is None:
            raise OSError("File could not open")

        arr = np.array(img)
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        Display(axes, arr, 0, 0, "Original")
        return arr
    except Exception as err:
        print(err)
        return None


def main():
    arr = ft_load("landscape.jpg")




if __name__ == "__main__":
    main()
