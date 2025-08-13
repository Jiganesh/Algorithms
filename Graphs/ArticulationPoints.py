#User function Template for python3


class Solution:
    
    def articulationPoints(self, V, adj):
        # code here
        
        visited = [False] * V
        time_of_insertion = [0] * V
        lowest_time_of_insertion = [0] * V

        articulation_points = set()
        
        def dfs(parent , node, timer):
            
            time_of_insertion [node] = timer
            lowest_time_of_insertion [node] = timer
            
            visited[node] = True
            childrens = 0
            
            for adjacent in adj[node]:
                timer +=1
                
                if adjacent == parent :
                    continue

                if visited[adjacent] == False:
                    dfs(node, adjacent, timer)
                    lowest_time_of_insertion[node] = min(lowest_time_of_insertion[node], lowest_time_of_insertion[adjacent])
                    childrens +=1
                    
                    # If the node cannot reach node before then that is articulation point hence >= 
                    if lowest_time_of_insertion[adjacent] >=  time_of_insertion[node] and parent != -1:
                        articulation_points.add(node)
                else:
                    lowest_time_of_insertion[node] = min(lowest_time_of_insertion[node], time_of_insertion[adjacent])
                    
            # Parent nodes can be articulation points if they have more than one children
            if (childrens > 1 and parent == -1):
                articulation_points.add(node)
                    
                    
        
        for node in range (V):
            if visited[node] == False:
                dfs(-1, node, 0)

        if articulation_points: 
            return sorted(articulation_points)
        
        return [-1]
                        
        