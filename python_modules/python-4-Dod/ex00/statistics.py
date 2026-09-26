from typing import Any


def ft_statistics(*args: float, **kwargs: str) -> None:
    """ft_statistics function calculates the mean, median, and mode of a list of numbers"""
    if not args:
        print("ERROR")
        return
    numbers = list(args)
    operations = list(kwargs.values())
    for operation in operations:
        if operation == "mean":
            mean = sum(numbers) / len(numbers)
            print(f"Mean: {mean}")
        elif operation == "median":
            median = sorted(numbers)[len(numbers) // 2]
            print(f"Median: {median}")
        elif operation == "mode":
            mode = max(set(numbers), key=numbers.count)
            print(f"Mode: {mode}")
        elif operation == "quartile":
            sorted_numbers = sorted(numbers)
            q1 = sorted_numbers[len(sorted_numbers) // 4]
            q3 = sorted_numbers[len(sorted_numbers) * 3 // 4]
            print(f"Quartile: [{float(q1)}, {float(q3)}]")
        elif operation == "std":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            std_dev = variance ** 0.5
            print(f"Standard Deviation: {std_dev}")
        elif operation == "var":
            mean = sum(numbers) / len(numbers)
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            print(f"Variance: {variance}")
        else:
            print("ERROR")


def main():
    pass


if __name__ == "__main__":
    main()

# mean : 95.6
# median : 42
# quartile : [11.0, 64.0]
