# number of people who were asked to give their opinions
n = int(input())

# responses
q = input().split(" ")

print("HARD" if '1' in q else "EASY", end="")
