def get_rules(filename):
	with open(filename) as f:
		rules = f.read()

	return rules


def get_input():
	n = int(input("What number do you choose?: "))

	return n


def three_five(n):
	acc = 0
	for i in range(n):
		if (i % 3) == 0 or (i % 5) == 0:
			acc += i

	return acc

def main():
	print(get_rules("Rules.txt"))
	print(three_five(get_input()))


if __name__ == '__main__':
	main()
