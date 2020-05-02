# n 	number of students
# k		ratio between number of certificates and the number of diplomas

n, k = map(int, input().split())

max_winners = n // 2

certificates = max_winners // (k + 1)

diplomas = certificates * k

not_winners = n - (certificates + diplomas)

print(certificates, diplomas, not_winners)