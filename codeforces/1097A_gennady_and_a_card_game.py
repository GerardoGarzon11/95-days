card_in_table = input()

cards_in_hand = input().split()

yes = False

for card in cards_in_hand:
	if card[0] == card_in_table[0] or card[1] == card_in_table[1]:
		yes = not yes
		break

print("YES" if yes else "NO")
