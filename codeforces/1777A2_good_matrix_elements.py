# matrix dimensions
n = int(input())
 
matrix = []
 
for mr in range(0, n):
	matrix.append(list(map(int, input().split())))
 
# get middle row (no need for + 1 since index starts with 0)
# good matrix points
gmp = sum(matrix[(n//2)])
matrix[n//2] = [0] * n
 
# get middle column
gmp += sum([row[n//2] for row in matrix])
 
for x in range(0, n):
	matrix[x][n//2] = 0
 
# get main and secondary diagonal
# since all elements already counted for middle row
# and middle column are already 0
# there's no need to worry about [n/2][n/2] now
for y in range(0, n):
	gmp += matrix[y][y] + matrix[-1 - y][y]
 
print(gmp)