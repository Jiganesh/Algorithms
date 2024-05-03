class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		colors = [-1] * V
		
		def bipartite (node, color):
			
			colors[node] = color
			
			for child in adj[node]:
				
				if colors[child] == -1: # if the child is not visited do dfs and set color
					if bipartite (child, color^1) == False: # if it is not bipartite return False
						return False
				elif child != node and colors[child] == color: # it is visited but color is not adjacent return False
					return False
			return True
			
		for i in range(V):
			if colors[i]==-1 and bipartite(i, 1)==False:
				return False
		return True