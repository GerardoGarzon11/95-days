def findPythagoreanTriplet(result):
	for a in range(1, result + 1):
		for b in range(a, result + 1 - a):
			if 1000 - a - b > 0:
				c = 1000 - a - b
				if c*c == a*a + b*b:
					print(a * b * c)

findPythagoreanTriplet(1000)
