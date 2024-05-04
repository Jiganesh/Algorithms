#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        
        distance = [10**8 for i in range (V)]
        distance[S] = 0
        
        for interations in range (V):
            for u, v, weight in edges:
                if distance[u] != 10**8 and distance[v] > weight + distance[u]:
                    distance[v] = min(distance[v] , weight + distance[u])
                
                
        for u, v, weight in edges:
            if distance[u] != 10**8 and distance[v] > weight + distance[u]:
                return [-1]
                
        
        return distance
        
        