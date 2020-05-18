"""
	https://codeforces.com/problemset/problem/361/A
	Input
		n	number of rows and columns
		k 	sum
	Output
			beautiful table
"""

n, k = map(int, input().split())

# 1 generate numbers
row = [k // n] * n

# find difference between sum of row
# and k. then using diff, add as many 1s as necessary
diff = k - sum(row)

for x in range(0, diff):
	row[x] += 1

# print row, and move last element to first
# all rows now sum the same
for y in range(0, n):
	print(*row)
	row.insert(0, row.pop())