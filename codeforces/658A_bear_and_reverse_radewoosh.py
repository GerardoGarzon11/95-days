n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

# submitting the i-th problem at time x
# gives max(0, pi - c * x)

l_time, l_score = 0, 0
r_time, r_score = 0, 0

for pi in range(0, len(p)):
	l_time += t[pi]
	l_score += max(0, p[pi] - (l_time * c))

	r_time += t[-1 - pi]
	r_score += max(0, p[-1 - pi] - (r_time * c))

print("Limak" if l_score > r_score else "Tie" if l_score == r_score else "Radewoosh")
