n, a, b = map(int, input().split())

a_likes = list(map(int,input().split()))
b_likes = list(map(int,input().split()))


end = " "
for apple in range(1, n + 1):
	end = '' if apple == n else ' '
	if apple in a_likes:
		print(1, end=end)
	elif apple in b_likes:
		print(2, end=end)