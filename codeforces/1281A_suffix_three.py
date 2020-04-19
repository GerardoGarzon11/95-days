t = int(input())

for tc in range(0, t):
	str_ = input()

	if str_[-2:] == 'po':
		print("FILIPINO")
	elif str_[-4:] == 'desu' or str_[-4:] == 'masu':
		print("JAPANESE")
	elif str_[-5:] == 'mnida':
		print("KOREAN")
