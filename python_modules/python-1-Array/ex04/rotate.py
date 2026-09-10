import numpy as np


def transpose(arr : np.array)->np.array:
	""" roate the image with 90 degree, because in the subject has been written 90 degree """
	h = arr.shape[0]
	w = arr.shape[0]
	result = []
	for i in range(h):
		row = []
		for j in range(w):
			row.append(arr[i][j][0])   # take the single channel
		result.append(row)

	return result


def rotate(arr:np.array):
	""" Manually start from last row """
	h = arr.shape[0]
	w = arr.shape[1]
	rotated = []

	for y in range(h - 1, -1, -1):
		row = []
		for x in range(w):
			row.append(arr[x][y])
		rotated.append(row)

	return rotated
