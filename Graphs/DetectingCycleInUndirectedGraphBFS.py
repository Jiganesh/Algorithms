from typing import List
from collections import deque

class Solution:
	#Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		visited = [False] * V
		
		def detect_cycle(parent , node):
			
			queue = deque([(parent, node)])
			
			
			while queue:
				
				parent, node = queue.popleft()
				visited[node] = True
				
				for child in adj[node]:
					if child == parent:
						continue
					elif visited[child] == True:
						return True
					else:
						queue.append((node, child))
						
			return False

		for node in range (V):
			if visited[node] ==False and detect_cycle(-1, node)==True:
				return True
				
		return False

