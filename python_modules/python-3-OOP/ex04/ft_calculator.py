class calculator:
    """calculator class that performs basic arithmetic operations on a arr of numbers"""
    # decorator
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dotproduct method calculates the dot product of two vectors"""
        dot = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {dot}")
        # decorator

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add_vec method adds two vectors"""
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vec is : {result}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """sous_vec method subtracts two vectors"""
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vec is : {result}")
	