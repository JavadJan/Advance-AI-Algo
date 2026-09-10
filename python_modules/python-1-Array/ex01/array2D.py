import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ take a matrix and slice the matrix with start and end """
    lst = np.array(family)
    print(f"My shape is : {lst.shape}")
    slc = lst[start:end]
    print(f"My new shape is : {slc.shape}")
    return slc.tolist()


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
