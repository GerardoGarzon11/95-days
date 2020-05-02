month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())

max_day = d - 1 + month_days[m-1]

print(max_day // 7 if max_day % 7 == 0 else (max_day // 7) + 1)