s = input()

qaq = 0

for i in range(0, len(s)):
	# find an A
	if s[i] == 'A':
		# find Qs before A
		before = s[:i].count('Q')
		# find Qs after A
		after = s[i+1:].count('Q')
		# add before * after to qaq
		qaq += before * after

print(qaq)