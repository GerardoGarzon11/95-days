from string import ascii_uppercase as alphabet

n, k = map(int, input().split())

s = input()

letter_count = [s.count(alphabet[i]) for i in range(0,k)]

print(min(letter_count) * k)