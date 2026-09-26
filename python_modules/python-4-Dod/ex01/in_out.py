def square(x: int | float) -> int | float:
	"""square function returns the square of a number"""
	return x * x


def pow(x: int | float) -> int | float:
	"""pow function returns x to the power of x"""
	return x ** x


def outer(x: int | float, function) -> object:
	count = x
	def inner() -> float:
		nonlocal count
		count = function(count)
		return count

	return inner

def main():
	pass	


if __name__ == "__main__":
	main()	

