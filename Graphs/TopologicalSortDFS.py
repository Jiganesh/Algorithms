class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        stack = []
        visited = [False] * V
        
        def topological_sort(node):
            
            visited [node] = True
            
            for child in adj[node]:
                if visited[child] == False:
                    topological_sort(child)
                    
            stack.append(node)

        for node in range(V):
            if visited[node] == False:
                topological_sort(node)
                
        return stack[::-1]