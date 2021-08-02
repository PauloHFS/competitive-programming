polyhedronsFaces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron    ": 20
}

n = int(input())
total = 0

for i in range(n):
    poly = input()
    total += polyhedronsFaces.get(poly)

print(total)