x, y, z = map(int, input().split())

step1 = x - y

if step1 > 0:
	print("+" if step1 - z > 0 else "?")
elif step1 == 0:
	print("0" if z == 0 else "?" )
else:
	print("-" if step1 + z < 0 else "?")