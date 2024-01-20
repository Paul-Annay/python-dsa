from queue import Queue

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
    
    def bfs(self, root):
        visited = [False] * self.vertices
        parent = [None] * self.vertices
        queue = Queue()
        print(visited)
        queue.put(root)
        visited[root] = True
        parent[root] = -1

        # print(current_node)
        while not queue.empty():
            current_node = queue.get()
            # print(current_node, end=" ")
            adjacents = self.adjacency_list[current_node]
            for v in adjacents:
                if not visited[v]:
                    queue.put(v)
                    visited[v] = True
                    parent[v] = current_node
        

        return parent
    
    def dfs(self, root):
        visited = [False] * self.vertices
        parent = [None] * self.vertices

        parent[root] = -1
        return self.dfs_traversal(root, visited, parent)
    
    def dfs_traversal(self, root, visited, parent):
        visited[root] = True
        # print(root, end = " ")

        adjancents = self.adjacency_list[root]
        for v in adjancents:
            if not visited[v]:
                parent[v] = root
                self.dfs_traversal(v, visited, parent)

        return parent



    

    def traversal_path(self, parent_array, start, end):
        path_string = ""
        while end != -1:
            path_string += " > " + str(end)
            end = parent_array[end]
        # path_string +=  " > " + str(0)
        return path_string[::-1]

    def __str__(self):
        return f"""
        matrix: {self.adjacency_matrix}
        list: {self.adjacency_list}
        """





