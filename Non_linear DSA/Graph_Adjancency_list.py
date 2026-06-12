class Graph:
    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.dict_adj_list = {}          # self.adj_list = {v:[] for v in range(vertex_count)}
        for val in range(vertex_count):
            self.dict_adj_list[val] = []
        return
    
    def valid_vertex(self,vertex):
        return 0 <= vertex < self.vertex_count

    def add_edge(self,vertex1, vertex2,weight=1):
        if self.valid_vertex(vertex1) and self.valid_vertex(vertex2):
            if not any(vertex2 == vertex for vertex,w in self.dict_adj_list[vertex1]):
                self.dict_adj_list[vertex1].append((vertex2,weight))
                self.dict_adj_list[vertex2].append((vertex1,weight))
                return
        
    def has_edge(self,vertex1,vertex2):
        if self.valid_vertex(vertex1) and self.valid_vertex(vertex2):
            return any(vertex2 == v for v,weight in self.dict_adj_list[vertex1])
        return False
    
    def remove_edge(self,vertex1,vertex2):
        if self.has_edge(vertex1,vertex2):
            self.dict_adj_list[vertex1] = [(vertex,weight) for vertex,weight in self.dict_adj_list[vertex1] if  vertex!= vertex2]
            self.dict_adj_list[vertex2] = [(vertex,weight) for vertex,weight in self.dict_adj_list[vertex2] if vertex != vertex1]
            return 
        
    def print_adj_list(self):
        for key, value in self.dict_adj_list.items():
            print(f"V{key} : {value}")
        return
    
g1 = Graph(4)
g1.add_edge(0,2,5)
g1.add_edge(0,1,5)
g1.add_edge(1,2,5)
g1.add_edge(2,3,5)
g1.add_edge(0,3,5)
g1.remove_edge(0,3)
print(g1.has_edge(0,3))
g1.print_adj_list()