from data_structures.Graph import Graph

with open('./undirectedgraph.txt', 'r') as f:
    vertices = int(f.readline())
    graph = Graph(vertices)
    for line in f:
        u, v = tuple(map(int, line.split(" ")))
        graph.addUnDirectedEdge(u, v)


print(graph.adjacency_list)
parent = graph.dfs(2)

print(graph.traversal_path(parent, 2, 4))