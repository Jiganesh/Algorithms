#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        dfs_traversal_result = []
        visited = [False] * V
        
        def dfs_iterative(node):

            stack = [node]
            
            while stack :

                node = stack.pop()

                if visited[node] == False:
                    visited[node]=True
                    dfs_traversal_result.append(node)

                for child in adj[node][::-1]:
                    if visited[child]==False:
                        stack.append(child)
        
        dfs_iterative(0)
        
        return dfs_traversal_result
