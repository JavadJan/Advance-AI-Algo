class calculator:
    """calculator class that performs basic arithmetic operations on a arr of numbers"""

    def __init__(self, numbers: [float]):
        self.numbers = numbers

    def __add__(self, other) -> [float]:
        """__add__ method adds a number to each element in the numbers arr"""
        self.numbers = [x + other for x in self.numbers]
        print(self.numbers)
        return self.numbers

    def __sub__(self, other) -> [float]:
        """__sub__ method subtracts a number from each element in the numbers arr"""
        self.numbers = [x - other for x in self.numbers]
        print(self.numbers)
        return self.numbers

    def __mul__(self, other) -> [float]:
        """__mul__ method multiplies each element in the numbers arr by a number"""
        self.numbers = [x * other for x in self.numbers]
        print(self.numbers)
        return self.numbers

    def __truediv__(self, other) -> [float]:
        """__truediv__ method divides each element in the numbers arr by a number"""
        if other == 0:
            raise ValueError("Cannot divide by zero")
        self.numbers = [x / other for x in self.numbers]
        print(self.numbers)
        return self.numbers
