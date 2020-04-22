for tc in range(0, int(input())):
	n = int(input()) # length of array, even number

	if (n // 2) % 2 != 0 or n % 2 != 0:
		print("NO")
	else:
		left_half = [x for x in range(2,n+1,2)]
		
		right_half = [l-1 for l in left_half[0:-1]]

		right_half.append(sum(left_half) - sum(right_half))

		full = [*left_half, *right_half]
		print("YES")
		print(' '.join(map(str,full)))
