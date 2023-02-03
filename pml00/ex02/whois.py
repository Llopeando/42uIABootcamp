import	sys

if (len(sys.argv) != 2):
	sys.exit("AssertionError: not enough arguments")
if not sys.argv[1].isnumeric():
	sys.exit("AssertionError: argument is not an integer")
num = int(sys.argv[1])

if num == 0:
	print("Im Zero!")
elif num % 2 == 1:
	print("Im an Odd number!")
elif num % 2 == 0:
	print("Im an Even number!")

