"""
	https://codeforces.com/problemset/problem/1038/A
	Input:
		n	length of string
		k	max number of letters of the latin alphabet
			where A = 1 and Z = 26
		s 	string
	Output
			length of largest good subsequence of s
"""

from string import ascii_uppercase as alphabet

n, k = map(int, input().split())

s = input()

letter_count = [s.count(alphabet[i]) for i in range(0,k)]

print(min(letter_count) * k)