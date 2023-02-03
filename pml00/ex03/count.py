import	sys
import	string

def	text_analyzer(text):
	'''This function analyzes a string passed as an argument.
	Then, it counts the upper-letters, lower-letters, punctuation makrs and spaces.
	And finally, it shows the final count values.
	'''
	argument_len = 0
	upper_count = 0
	lower_count = 0
	punctuation_count = 0
	spaces_count = 0

	if not text:
		text = input("There is no text!\nPlease, write some valid text here: ")
		print("✅ \033[1;37mNice! So this is your text info...\033[0m\n")
	for argument in text:
		argument_len += len(argument)
		upper_count += argument.isupper()
		lower_count += argument.islower()
		punctuation_count += argument in string.punctuation
		spaces_count += argument == ' '
	print("The text contains", argument_len, "character(s)\n-", upper_count, "upper letter(s)\n-", lower_count, "lower letter(s)\n-", punctuation_count, "punctuation mark(s)\n-", spaces_count, "space(s)")

def	main():
	if (len(sys.argv) != 2):
		sys.exit("AssertionError: not enough arguments")
	text_analyzer(sys.argv[1])

if __name__ == "__main__":
	main()