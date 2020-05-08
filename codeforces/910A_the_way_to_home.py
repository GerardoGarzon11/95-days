"""
	https://codeforces.com/problemset/problem/910/A
	Input
		n 	point that has to be reached
		d 	max length of jump
		s 	consisting of zeroes and ones
			0 = no lily flower
			1 = lily flower (frog can jump here)
	Output
		x 	min number of jumps needed to reach n
		-1	if n can't be reached
"""

n, d = map(int, input().split())
s = input()

# index 0
n -= 1

reachable = True
reached = False
jumps = 0
i = 0

while reachable and not reached:
	# can reach home now?
	if n <= i + d:
		reached = True
		jumps += 1
		break
	# are there reachable flowers?
	elif '1' not in s[i+1:i+d+1]:
		reachable = False
	# determine max jump
	else:
		jumps += 1
		# get farthest reachable lily (1)
		i += s[i+1:i+d+1].rfind('1') + 1

print(jumps if reached else -1)