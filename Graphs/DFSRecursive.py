#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        dfs_traversal_result = []
        visited = [False] * V
        
        def dfs_recursive(node):
            visited[node] = True
            dfs_traversal_result.append(node)
            
            for child in adj[node]:
                if visited[child] == False:
                    dfs_recursive(child)
                    
        dfs_recursive(0)
        
        return dfs_traversal_result
    
    