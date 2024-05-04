class Solution:
    def tarjans_algorithm(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # Create Undirected Graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        
        timer, bridges = 0, []

        time_of_insertion = [0] * n
        lower_time_of_insertion = [0] * n


        def dfs(parent, node, timer):
            # Set time_of_insertion and lower_time_of_insertion will be initial same as time_of_insertion
            time_of_insertion[node] = lower_time_of_insertion[node] = timer

            visited[node] = True # Mark node as visited

            for adjacent in graph[node]:
                timer += 1 # increase timer
                if adjacent == parent : continue # if adjacent is parent = ignore

                if visited[adjacent] == False:
                    dfs(node, adjacent, timer)
                    lower_time_of_insertion[node] = min(
                        lower_time_of_insertion[node],
                        lower_time_of_insertion[adjacent]
                    )
                    # If time_of_insertion of node is less than lower_time_of_insertion of adjacent
                    # then that edges is a bridge
                    if time_of_insertion[node] < lower_time_of_insertion[adjacent] :
                        bridges.append([node, adjacent])

                else:
                    lower_time_of_insertion[node] = min(
                        lower_time_of_insertion[node], 
                        lower_time_of_insertion[adjacent]
                    )

        dfs (-1, 0, 0) # dfs (parent, node, timer)

        return bridges

