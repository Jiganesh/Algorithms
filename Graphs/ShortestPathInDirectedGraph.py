class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        # Create Graph
        
        graph = defaultdict(list)
        visited = [0] * n
        
        for u, v, w in edges:
            graph[u].append((v, w))
            
        
        
        topological_order = []
        
        def topo_sort(node):
            
            visited[node] = 1
            
            for child, weight in graph[node]:
                if visited[child]==0:
                    topo_sort(child)
            
            topological_order.append(node)
            
        for i in range (n):
            if visited[i] == 0:
                topo_sort(i)
                
      
        distance = [float("inf") for i in range(n)]
        distance[0] = 0
        
        while topological_order :
            node = topological_order.pop()
            for child , weight in graph[node]:
                distance[child] = min(distance[child] , weight + distance[node])
                
        return [-1 if i == float("inf") else i for i in distance]
        
            