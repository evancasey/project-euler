def run():
	x = 0
	y = 1
	sum = 0
	while y < 4000000:
		new = x + y
		x = y
		y = new
		if y %2 == 0:
			sum = sum + y

	print sum

if __name__ == "__main__":
	run()	