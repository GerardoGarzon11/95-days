fl = list(input())
sl = list(input())
s = input()

typed_in_second = ''

for char in s:
	if char != char.lower():
		isUpper = True
	else:
		isUpper = False

	char = char.lower()
	if char in fl:
		index = fl.index(char)
		typed_in_second += sl[index] if not isUpper else sl[index].upper()
	else:
		typed_in_second += char

print(typed_in_second)