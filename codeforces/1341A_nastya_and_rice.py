for tc in range(0, int(input())):
	n, a, b, c, d = input().split()

	# 0 <= b < a <= 1000, 0 <= d < c <= 1000
	n, a, b, c, d = int(n), int(a), int(b), int(c), int(d)

	min_grains_weight = (a - b) * n
	max_grains_weight = (a + b) * n
	min_grain_bag = c - d
	max_grain_bag = c + d

	if min_grains_weight >= min_grain_bag and min_grains_weight <= max_grain_bag:
		print("Yes")
	elif max_grains_weight >= min_grain_bag and max_grains_weight <= max_grain_bag:
		print("Yes")
	elif min_grains_weight < min_grain_bag and max_grains_weight > max_grain_bag:
		print("Yes")
	else:
		print("No")