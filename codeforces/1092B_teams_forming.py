number_of_students = int(input())
skills = sorted(list(map(int, input().split())))

min_problems = 0

for x in range(0, len(skills), 2):
	min_problems += skills[x + 1] - skills[x]

print(min_problems)