class DisjointSet():
    
    def __init__(self, number_of_nodes) -> None:
        
        self.rank = [0] * number_of_nodes
        self.parent = [i for i in range (number_of_nodes)]


    def findParent (self, node):

        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.findParent(self.parent[node])
            return self.parent[node]
        
    def unionByRank (self, u, v):

        ult_u = self.findParent(u)
        ult_v = self.findParent(v)

        if ult_u == ult_v : return

        if self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        elif self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        else:
            self.rank[ult_u]+=1
            self.parent[ult_v] = ult_u
        