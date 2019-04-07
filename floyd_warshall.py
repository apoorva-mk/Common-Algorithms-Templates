class Graph:
	def __init__(self):
		self.adjlist = []
		self.adjmat = []
		self.array=[]
		self.v=0
		self.e=0

	def create(self):
		self.v = int(input("Enter number of vertices: "))
		self.e = int(input("Enter number of edges: "))
		for i in range(self.v):
			self.adjlist.append([])
			

		for i in range(self.v):
			temp = []
			for j in range(self.v):
				temp.append(0)

			self.adjmat.append(temp)

		self.array = [[[ 1000000 for i in range(self.v)] for j in range(self.v) ] for k in range(self.v)]

		for i in range(self.e):
			edge=input().split()
			self.adjlist[int(edge[0])].append(int(edge[1]))
			self.adjmat[int(edge[0])][int(edge[1])] = int(edge[2])
			self.adjlist[int(edge[1])].append(int(edge[0]))
			self.adjmat[int(edge[1])][int(edge[0])] = int(edge[2])


	def Floyd_warshall(self):
		#initialising
		for i in range(self.v):
			for j in range(self.v):
				if i==j:
					self.array[i][j][0] = 0

				elif self.adjmat[i][j]==0:
					self.array[i][j][0] = 100000

				else:
					self.array[i][j][0] = self.adjmat[i][j]


		for i in range(self.v):
			for j in range(self.v):
				for k in range(1,self.v):
					self.array[i][j][k] = min(self.array[i][j][k-1], (self.array[i][k][k-1]+self.array[k][j][k-1]) )
					

		print("")
		for i in range(self.v):
			for j in range(self.v):
				print(self.array[i][j][1]," ",end= " ")

			print("")



G = Graph()
G.create()
G.Floyd_warshall()
