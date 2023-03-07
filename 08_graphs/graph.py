class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        '''
        Prints out the entire graph.
        '''
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        '''
        Parameters:
        vertex: Desired vertex to add.

        Adds a single vertex.
        '''
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        '''
        Parameters: 
        v1: Vertex to add an edge to.
        v2: Vertex to add an edge to.

        Adds an edge between two vertices.
        '''
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        '''
        Parameters: 
        v1: Vertex to add an edge to.
        v2: Vertex to add an edge to.

        Remove edge between two vertices.
        '''
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                print("Error, value not found.")
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
