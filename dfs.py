class Graph(object):
	def __init__(self):
		self.v = 0
		self.e=0
		self.adjlist=[]
		self.visited=[]

	def create(self):
		self.v=int(input("Enter number of vertices: "))
		self.e=int(input("Enter number of edges: "))

		for i in range(self.v):
			self.adjlist.append([])
			self.visited.append(0)

		print("Enter edges: ")
		for i in range(self.e):
			edge=input().split()
			self.adjlist[int(edge[0])].append(int(edge[1]))

	def dfs(self,v):
		if self.visited[v]==1:
			return 

		else:
			self.visited[v]=1
			for u in self.adjlist[v]:
				if self.visited[v]!=0:
					self.dfs(u)

		print(v)
					
		


G=Graph()
G.create()
G.dfs(0)



		
