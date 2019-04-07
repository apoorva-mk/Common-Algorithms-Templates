import math
import heapq

class Vertex:
	def __init__(self,num):
		self.prev = None

		if num != 0:
			self.cost = 100000

		else:
			self.cost = 0

		self.v = num

	def __lt__(self,other):
		if self.cost < other.cost:
			return True

		return False


class Graph:
	def __init__(self):
		self.adjlist = []
		self.adjmat = []
		self.vertices = []
		self.mstvertices = []
		self.edges = []
		self.v=0
		self.e=0


	def create(self):
		self.v = int(input("Enter number of vertices: "))
		self.e = int(input("Enter number of edges: "))
		for i in range(self.v):
			V = Vertex(i)
			self.adjlist.append([])
			self.vertices.append(V)
			self.mstvertices.append(0)

		for i in range(self.v):
			temp = []
			for j in range(self.v):
				temp.append(0)

			self.adjmat.append(temp)

		for i in range(self.e):
			edge=input().split()
			self.adjlist[int(edge[0])].append(int(edge[1]))
			self.adjmat[int(edge[0])][int(edge[1])] = int(edge[2])
			self.adjlist[int(edge[1])].append(int(edge[0]))
			self.adjmat[int(edge[1])][int(edge[0])] = int(edge[2])

		print("adjlist:\n",self.adjlist)
		print("adjmat:\n",self.adjmat)


	def Prim(self):
		heapq.heapify(self.vertices)
		self.mstvertices[0] = 1

		while len(self.vertices) != 0:
			v = heapq.heappop(self.vertices)
			if v.prev != None:
				self.edges.append([v.prev,v.v])
			self.mstvertices[v.v] = 1

			for uu in self.adjlist[v.v]:
				if self.mstvertices[uu] == 0:
					for u in self.vertices:
						if u.v == uu:
							if u.cost > self.adjmat[v.v][u.v]:
								u.cost = self.adjmat[v.v][u.v]
								u.prev = v.v
								heapq.heapify(self.vertices)


		print("The MST edges are: ", self.edges)

G = Graph()
G.create()
G.Prim()







