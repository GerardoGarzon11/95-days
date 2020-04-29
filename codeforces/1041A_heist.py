remaining_keyboards = int(input())

a = sorted(list(map(int, input().split())))

min_ = sum(a[x+1] - a[x] -1  for x in range(0, len(a) - 1))

print(min_)
