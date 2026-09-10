import argparse, sys

if(len(sys.argv) != 2):
	print("AssertionError: more than one argument is provided")
	sys.exit(1)

#def parse_int(value):
#	try:
#		return int(value)
#	except ValueError:
#		raise argparse.ArgumentError("AssertionError: argument is not an integer")



#parser = argparse.ArgumentParser(description="Check if a number is even or odd.")
#parser.add_argument("javad", type=parse_int)
#arg = parser.parse_args()
#if(arg.javad % 2 == 0):
#	print("I'am Even.")
#else:
#	print("I'am Odd.")



arg = sys.argv[1]

try:
    num = int(arg)
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit(1)

if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")