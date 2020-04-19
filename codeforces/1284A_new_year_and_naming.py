n, m = map(int, input().split())

n_strings, m_strings = input().split(), input().split()

for q in range(0, int(input())):
	y = int(input())

	yn = (y % n) - 1
	ym = (y % m) - 1

	print(n_strings[yn]+m_strings[ym])
