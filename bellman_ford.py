import math

class Graph:
	def __init__(self):
		self.adjparentlist = []
		self.adjmat = []
		self.bellmanford = []
		self.v=0
		self.e=0

	def create(self):
		self.v=int(input("Enter number of vertices: "))

		for i in range(self.v):
			self.adjparentlist.append([])

		self.e=int(input("Enter number of edges: "))

		for i in range(self.v):
			temp = []

			for j in range(self.v):
				temp.append(0)

			self.adjmat.append(temp)

		
		for i in range(self.v):
			temp2 = []

			for j in range(self.v+1):
				temp2.append(0)

			self.bellmanford.append(temp2)

		#print(self.bellmanford)

		for i in range(self.e):
			edge=input().split()
			self.adjparentlist[int(edge[1])].append(int(edge[0]))
			self.adjmat[int(edge[0])][int(edge[1])] = int(edge[2])


		# print(self.adjparentlist)
		# print(self.adjmat)
		# print(self.bellmanford)

	def Bellman_Ford(self,src):
		for i in range(self.v):
			if i==src:
				self.bellmanford[i][0] = 0

			else:
				self.bellmanford[i][0] = math.inf

		for i in range(1,self.v+1):
			for j in range(self.v):
				if j==src:
					self.bellmanford[j][i]=0

				else:
					for v in self.adjparentlist[j]:
						if self.bellmanford[v][i-1]!=math.inf:
							if( self.bellmanford[j][i-1] > self.bellmanford[v][i-1]+self.adjmat[v][j]):
								self.bellmanford[j][i] = self.bellmanford[v][i-1]+self.adjmat[v][j]

						elif self.bellmanford[j][i-1]==math.inf:
							self.bellmanford[j][i]=math.inf

		for i in range(self.v):
			for j in range(self.v+1):
				print(self.bellmanford[i][j]," ",end=" ")
			print("")




G = Graph()
G.create()
G.Bellman_Ford(0)