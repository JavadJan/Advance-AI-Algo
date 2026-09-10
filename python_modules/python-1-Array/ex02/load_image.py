import numpy as np
from PIL import Image

# load image
def ft_load(path: str) -> np.array: 
	img = Image.open(path)
	lst = np.array(img)
	print(f"The shape of image is: {lst.shape}")
	return lst

def main():
	ft_load()

if __name__ == "__main__":
	main()