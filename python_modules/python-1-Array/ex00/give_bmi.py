import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ It takes a list of height and weight then it counts the bmi """
    height = np.array(height)
    weight = np.array(weight)
    if (len(height) != len(weight)):
        raise ValueError("height and weight lists must have the same length")

    for h in height:
        if not isinstance(h, (int, float)):
            raise ValueError("Error in type of element")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise ValueError("Error in type of element")

    return (weight / (height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:

    return [i > limit for i in bmi]


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except IndexError:
        print("not the same size or type")
        return


if __name__ == "__main__":
    main()
