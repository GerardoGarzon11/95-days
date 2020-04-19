# brute force, dynamic programming, implementation, *1000

def solve(seq):
	dp = [1] * len(seq)

	for x in range(1, len(seq)):
		dp[x] = dp[x-1] + 1 if seq[x] >= seq[x-1] else dp[x]

	return max(dp)


# length of sequence
n = int(input())

# sequence of numbers
sequence = [int(x) for x in input().split()]

print(solve(sequence))
