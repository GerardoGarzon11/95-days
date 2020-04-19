polyhedron_guide = {
	"Tetrahedron": 4,
	"Cube": 6,
	"Octahedron": 8,
	"Dodecahedron": 12,
	"Icosahedron": 20
}

total_faces = 0

for i in range(0, int(input())):
	total_faces += polyhedron_guide[input()]

print(total_faces)
