import heapq

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
       
        heap = [(0, S)]
        distance = [float("inf") for i in range(V)]
        distance[S] =0
        
        
        while heap:
            
            d, node = heapq.heappop(heap)

            
            for child, weight in adj[node]:

                if distance[child] >= weight + distance[node]:
                    distance[child] = weight + distance[node]
                    heapq.heappush(heap, (distance[child], child))
                    
        return distance
        
        