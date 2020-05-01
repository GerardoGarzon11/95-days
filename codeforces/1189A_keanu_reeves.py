# length of the string s
n = int(input())

s = input()

num_of_zeros, num_of_ones = s.count('0'), s.count('1')

if num_of_ones == num_of_zeros:
	print(2)
	print(s[0], s[1:])
else:
	print(1)
	print(s)