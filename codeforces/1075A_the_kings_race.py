# length of the side of the chess field
n = int(input())
# coordinates of the cell where the coin fell
x, y = map(int, input().split())

# 1 diagonal movement
# white/black diagonal movement
wdm = min(x,y) - 1 
bdm = n - max(x,y)

current_white = [1 + wdm, 1 + wdm]
current_black = [n - bdm, n - bdm]

# 2 straight (horizontal or vertical) movement
# white/black straight movement
if current_white[0] != x:
	# move current_white[0]
	wsm = x - current_white[0]
elif current_white[1] != y:
	# move_current_white[1]
	wsm = y - current_white[1]
else:
	wsm = 0

if current_black[0] != x:
	# move current_white[0]
	bsm = current_black[0] - x
elif current_black[1] != y:
	# move_current_white[1]
	bsm = current_black[1] - y
else:
	bsm = 0

#print(wdm + wsm, bdm + bsm)

twm = wdm + wsm
tbm = bdm + bsm

print("White" if twm <= tbm else "Black")