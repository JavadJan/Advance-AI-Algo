from typing import Any

def callLimit(limit: int):
    """Decorator to limit the number of times a function can be called"""
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwargs: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print(f"Error: {function} called too many times")

        return limit_function

    return callLimiter



def main():
	pass

if __name__ == "__main__":
	main()