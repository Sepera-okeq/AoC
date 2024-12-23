from collections import defaultdict

with open("input (22).txt", "r") as file:
    connections = [line.strip() for line in file]

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

triangles = set()
for node in graph:
    neighbors = list(graph[node])
    for i in range(len(neighbors)):
        for j in range(i + 1, len(neighbors)):
            if neighbors[j] in graph[neighbors[i]]:
                triangle = tuple(sorted([node, neighbors[i], neighbors[j]]))
                triangles.add(triangle)

triangles_with_t = [triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)]

print(len(triangles_with_t))