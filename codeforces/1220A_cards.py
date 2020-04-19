# length of string
n = int(input())

# the string
s = input()

# only ones have n's
count_n = s.count('n')

# only zeros have z's
count_z = s.count('z')

res = (count_n * "1 ") + (count_z * "0 ")

print(res[0:-1])
