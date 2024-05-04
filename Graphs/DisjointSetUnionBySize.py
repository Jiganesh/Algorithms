class DisjointSet():
    def __init__(self, number_of_node) -> None:
        self.parent = [i for i in range(number_of_node)]
        self.size = [1] * number_of_node


    def findParent(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
        

    def unionBySize(self, u, v):

        ult_u = self.findParent(u)
        ult_v = self.findParent(v)

        if ult_u == ult_v : return 

        if self.size[ult_u]> self.size[ult_v]:
            self.parent[ult_v] = ult_u
            self.size[ult_u]+= self.size[ult_v]
        else:
            self.parent[ult_u] = ult_v
            self.size[ult_v]+= self.size[ult_u]