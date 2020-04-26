n = input()
s = input()

print(sum([x + 1 for x in range(0,len(s)) if int(s[x]) % 2 == 0]))