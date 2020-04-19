# math

n, m, a = input().split()

n = int(n)
m = int(m)
a = int(a)

side_1 = m // a if m % a == 0 else (m // a) + 1
side_2 = n // a if n % a == 0 else (n // a) + 1

print(side_1 * side_2)
