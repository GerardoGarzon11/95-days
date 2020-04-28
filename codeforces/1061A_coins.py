n, S = map(int, input().split())

# coins = [1, 2, 3... n]
# S = amount

print(S // n if S % n == 0 else (S // n) + 1)