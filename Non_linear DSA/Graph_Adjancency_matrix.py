class Graph:
    def __init__(self, vertex_count = None):
        self.vertex_count = vertex_count
        self.adj_matrix =[]
        for val in range(vertex_count):
            row =[0]*vertex_count
            self.adj_matrix.append(row)

    def is_valid_vertex(self,vertex):
        if 0 <= vertex < self.vertex_count:
            return True
        return False   
    
    def add_edge(self,vertex1,vertex2, weight = 1):
        if self.is_valid_vertex(vertex1) and self.is_valid_vertex(vertex2) :
            self.adj_matrix[vertex1][vertex2] = weight
            self.adj_matrix[vertex2][vertex1] = weight
            return

    def remove_edge(self,vertex1,vertex2):
        if self.has_edge(vertex1,vertex2):
              self.adj_matrix[vertex1][vertex2] = 0
              self.adj_matrix[vertex2][vertex1] = 0
              return
    
    def has_edge(self,vertex1, vertex2):
        if self.is_valid_vertex(vertex1) and self.is_valid_vertex(vertex2) :
           if self.adj_matrix[vertex1][vertex2] != 0:
            return True
        return False
    
    def print_adj_matrix(self):
        for val in range(self.vertex_count):
            print(self.adj_matrix[val])
        return
    
    def get_adjacent_vertices(self,vertex):
        if self.is_valid_vertex(vertex):
            index = 0
            vertices = []
            for val in self.adj_matrix[vertex]:
                if val >= 1:
                    vertices.append(index)
                index += 1
            return vertices
                


g1 = Graph(4)
g1.add_edge(1,0)
g1.add_edge(2,3)
g1.add_edge(0,2)
g1.add_edge(1,2)
g1.remove_edge(2,3)
print(g1.has_edge(1,2))
print(g1.get_adjacent_vertices(1))
g1.print_adj_matrix()