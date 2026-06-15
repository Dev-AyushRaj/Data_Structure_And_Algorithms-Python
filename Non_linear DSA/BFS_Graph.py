class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def add_vertex(self,vertex):
        self.queue.append(vertex)
        return
    
    def take_out_vertex(self):
        return self.queue.pop(0)

class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.dict_adj_list =  {vo : [] for vo in range(vertex_count)}

    def valid_vertex(self,vertex):
        return 0 <= vertex < self.vertex_count

    def add_edge(self,vertex1, vertex2,weight):
        if self.valid_vertex(vertex1) and self.valid_vertex(vertex2):
            if not self.has_edge(vertex1,vertex2):
                self.dict_adj_list[vertex1].append((vertex2,weight))
                self.dict_adj_list[vertex2].append((vertex1,weight))
                return


    def has_edge(self,vertex1, vertex2):
        if self.valid_vertex(vertex1) and self.valid_vertex(vertex2):
            return  any(vertex2 == v for v,w in self.dict_adj_list[vertex1])
        return False  
    

    def BFS(self,start):
        list = Queue()
        visit_list = [False]*self.vertex_count
        list.add_vertex(start)
        visit_list[start] = True

        while not list.is_empty():
            vertex = list.take_out_vertex()
            print(vertex, end=" ")
            for adj_vertex,w in self.dict_adj_list[vertex]:
                if not visit_list[adj_vertex]:
                    list.add_vertex(adj_vertex)
                    visit_list[adj_vertex] = True
        
    
                   

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
g1.print_adj_list()
g1.BFS(1)
