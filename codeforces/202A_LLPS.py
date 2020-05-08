"""
	https://codeforces.com/problemset/problem/202/A
	Input
		s	String consisting of lowercase english letters only
	Output
			Lexicographically largest palindromic subsequence
"""

s = list(input())

letters = sorted(set(s))

max_letter = letters[-1]

print(max_letter * s.count(max_letter))