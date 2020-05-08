"""
	https://codeforces.com/problemset/problem/899/A
"""

n = int(input())

people = list(map(int, input().split()))

ones = people.count(1)
twos = people.count(2)

if ones < twos:
	print(ones)
else:
	print(twos + (ones - twos) // 3)