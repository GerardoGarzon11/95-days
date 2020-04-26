# telephone number = 11 digits
# first digit is 8
# s (str) of length (n)

for tc in range(0, int(input())):
	n = int(input())
	s = input()

	if n < 8:
		print("NO")
	elif s.find('8') + 10 < n and s.find('8') != -1 :
		print("YES")
	else:
		print("NO")