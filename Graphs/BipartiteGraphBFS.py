from collections import deque

class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		colors = [-1] * V
		
		def bipartite (node, color):
			
			queue = deque([(node, color)])
			colors[node] = color
			
			while queue:
				
				node , color = queue.popleft()
				
				for child in adj[node]:
					
					if colors[child] == -1:
						colors[child] = color^1
						queue.append((child, color^1))
					elif colors[child] == color:
						return False
						
			return True

		for i in range(V):
			if colors[i]==-1 and bipartite(i, 1)==False:
				return False
		return True
					