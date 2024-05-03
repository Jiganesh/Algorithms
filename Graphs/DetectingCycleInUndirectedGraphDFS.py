from typing import List
class Solution:
	#Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		visited = [False] * V
		
		def detect_cycle(parent , node):
			
			visited[node] =True

			for child in adj[node]:
				if visited[child] == False:
					if detect_cycle(node, child)==True:
						return True
				elif child != parent :  # If node is visited and it is not parent then there exist a cycle
					return True
					
			return False
						
				
		   
		for node in range (V):
			if visited[node] ==False and detect_cycle(-1, node)==True:
				return True
		return False