from collections import defaultdict
from itertools import combinations

with open("input (22).txt", "r") as file:
    connections = [line.strip() for line in file]

graph = defaultdict(set)
for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

def is_clique(nodes, graph):
    for a, b in combinations(nodes, 2):
        if b not in graph[a]:
            return False
    return True

largest_clique = []
for node in graph:
    neighbors = graph[node] | {node}
    for size in range(len(neighbors), 1, -1):
        for subset in combinations(neighbors, size):
            if is_clique(subset, graph) and len(subset) > len(largest_clique):
                largest_clique = subset

password = ",".join(sorted(largest_clique))
print(password)