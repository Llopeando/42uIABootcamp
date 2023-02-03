import	sys
import	string

def	operations(number1, number2):
	print('Sum:         {}'.format(number1 + number2))
	print('Difference:  {}'.format(number1 - number2))
	print('Product:     {}'.format(number1 * number2))
	print('Quotient:    {}'.format(number1 / number2))
	print('Remainder:   {}'.format(number1 % number2))

def	main():
	if len(sys.argv) != 3:
		sys.exit("Incorrect number of arguments!")
	try:
		number1 = int(sys.argv[1])
		number2 = int(sys.argv[2])
		operations(number1, number2)
	except ValueError:
		sys.exit("Eres un pringao jaja salu2")

if	__name__ == "__main__":
	main()