class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for x in range(vertices)]
        self.adjacency_matrix = [[None] * vertices for x in range(vertices)]

    def addDirectedEdge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_matrix[u][v] = 1

    def addUnDirectedEdge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1

    def __str__(self):
        return f"""
        matrix: {self.adjacency_matrix}
        list: {self.adjacency_list}
        """


with open('./input.txt', 'r') as f:
    vertices = int(f.readline())
    graph = Graph(vertices)
    for line in f:
        u, v = tuple(map(int, line.split(" ")))
        graph.addUnDirectedEdge(u, v)


print(graph)


