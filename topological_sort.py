class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.v = 0
		self.e=0
		self.adjlist=[]
		self.adjparent=[]

	def create(self):
		self.v=int(input("Enter number of vertices: "))
		self.e=int(input("Enter number of vertices: "))
		for i in range(self.v):
			self.adjparent.append([])
			self.adjlist.append([])

		for i in range(self.e):
			edge=input().split()
			self.adjlist[int(edge[0])].append(int(edge[1]))
			self.adjparent[int(edge[1])].append(int(edge[0]))

	def Topological_sort(self):
		count=[0]*self.v
		S=[]
		

		for i in range(self.v):
			count[i]=len(self.adjparent[i])
			if count[i]==0:
				S.append(i)

		while len(S)!=0:
			u=S.pop()
			print(u)

			for v in self.adjlist[u]:
				count[v]=count[v]-1
				if count[v]==0:
					S.append(v)


G=Graph()
G.create()
G.Topological_sort()


		