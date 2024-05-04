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
        
            
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        
        n = []
        for node, childrens in enumerate(adj):
            for child , weight in childrens:
                
                n.append((weight, child, node))
                
        n.sort()
        
        d = DisjointSet(V)
        summation = 0
        for weight, child , node in n:
            if d.findParent(child) != d.findParent(node):
                summation += weight
                d.unionBySize(child, node)
                
        return summation