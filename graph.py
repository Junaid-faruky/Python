class graph:
    def __init__ (self):
        self.graph = []
        
mat = [[1,1,1],[2,2,2],[3,3,3]]
print(mat[0])
print(mat[0][1])

for i in mat:
    for j in i:
        print(j, end = '  ')
    print ()
class graph:
    def __init__ (self):
        self.mat = []
        self.vertices = []
        
    def add_node(self,node):
        n = len(self.vertices)
        row = [0]*n
        self.mat.append(row)
        for each_row in self.mat:
            each_row.append(0)
    def add_edge(self,v1,v2):
        v1_index = self.vertices.index(v1)
        v2_index = self.vertices.index(v2)
        self.mat[v1][v2] = 1
        self.mat[v1][v2] = 1
        
graph1 = graph()
graph1.add_node('A')
graph1.add_node('B')
graph1.add_node('C')
print(graph1.mat)
graph1.add_edge('A','B')
graph1.add_edge('B','C')
print(graph1.mat)
