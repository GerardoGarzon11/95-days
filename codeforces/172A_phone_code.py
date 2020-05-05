"""
	https://codeforces.com/problemset/problem/172/A
	Input
		n	number of friends
		sn	phone numbers
	Output
			number of digits in the city phone code
"""

# current longest possible city phone code
clpcpc = ''

for tc in range(0, int(input())):
	if tc == 0:
		clpcpc = list(input())
	else:
		next_phone_number = list(input())
		candidate = ''
		for l in range(0, len(clpcpc)):
			if clpcpc[l] == next_phone_number[l]:
				candidate += clpcpc[l]
			else:
				clpcpc = candidate
				break

print(len(clpcpc))