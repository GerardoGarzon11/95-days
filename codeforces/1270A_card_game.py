for tc in range(0, int(input())):
	n, k1, k2 = map(int, input().split())
	p1_cards = list(map(int, input().split()))
	p2_cards = list(map(int, input().split()))
	
	if max(p1_cards) > max(p2_cards):
		print("YES")
	else:
		print("NO")