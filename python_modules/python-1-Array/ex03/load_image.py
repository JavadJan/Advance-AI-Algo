from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from zoom import ft_zoom

def ft_load(path: str) -> np.array:
	""" load image and store into dic """
	try:
		img = Image.open(path)
		if img.format is None:
			raise OSError("File could not open")
        
		return img
	except Exception as e:
		print(f"Error loading image: {e}")
		return None


def print_info(arr: np.array):
    """ Print the details of the image """
    h, w = arr.shape[:2]
    channels = arr.shape[2] if arr.ndim == 3 else 1

    print("Size X:", w)
    print("Size Y:", h)
    print("Channels:", channels)
    print("Pixel content sample:", arr[0:5, 0:5])  # first 5×5 pixels



def ft_display(arr: np.array, title="Image"):
    plt.imshow(arr)
    plt.title(title)
    w, h = arr.shape[:2]
    plt.xlabel(f"X axis {w}")
    plt.ylabel(f"Y axis {h}")
    plt.show()

def convert_gray_scale(arr:np.array):
	gray = np.mean(arr, axis=2, keepdims=True).astype(np.uint8)
	return gray

def load_image(path: str):
	img = ft_load(path)
	arr = np.array(img)
	print("The shape of image is: ", arr.shape)
	print(arr[:4])
	#ft_display(arr, title=img.mode)
	if arr is not None:
		cropped = ft_zoom(arr)
		gray = convert_gray_scale(cropped)
		print(f"New shape after slicing{gray.shape}")
		print(gray)
		ft_display(gray, title= "Imgage")
		# resize back to original size
	print("Channels:", gray.shape[2] if gray.ndim == 3 else 1)


def main():
    """ main function to prevent """
    try:
        load_image("animal.jpeg")
    except IndexError:
        return


if __name__ == "__main__":
    main()
