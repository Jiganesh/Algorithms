#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		
		N = len(matrix)
		
		
		def replacer(matrix, current, new):
			
			for i in range (N):
				for j in range(N):
					if matrix[i][j]==current:
						matrix[i][j]=new
						
		  
		replacer(matrix, -1, float("inf"))
		
		for via in range (N):
			for i in range (N):
				for j in range(N):
					
					matrix[i][j] = min( matrix[i][via] + matrix[via][j], matrix[i][j])
					
		
		replacer(matrix, float("inf"), -1)
		
		return matrix