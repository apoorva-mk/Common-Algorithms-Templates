import math
import heapq
from disjoint_set_adt import disjoint_adt
from disjoint_set_adt import Node

class Edge:
	def __init__(self,i,j,wt):
		self.start = i
		self.end = j
		self.len = wt

	def __lt__(self,other):
		if self.len < other.len:
			return True

		return False


class Graph:
	def __init__(self):
		self.adjlist = []
		self.adjmat = []
		self.edges = []
		self.mstedges = []
		self.mst = disjoint_adt()
		self.v=0
		self.e=0


	def create(self):
		self.v = int(input("Enter number of vertices: "))
		self.e = int(input("Enter number of edges: "))
		for i in range(self.v):
			N = Node(i)
			self.mst.makeSet(N)
			self.adjlist.append([])
			

		for i in range(self.v):
			temp = []
			for j in range(self.v):
				temp.append(0)

			self.adjmat.append(temp)

		for i in range(self.e):
			edge=input().split()
			e = Edge( int(edge[0]) , int(edge[1]) , int(edge[2]) )
			self.edges.append(e) 
			self.adjlist[int(edge[0])].append(int(edge[1]))
			self.adjmat[int(edge[0])][int(edge[1])] = int(edge[2])
			self.adjlist[int(edge[1])].append(int(edge[0]))
			self.adjmat[int(edge[1])][int(edge[0])] = int(edge[2])


	def Kruskal(self):
		self.edges.sort()

		for e in self.edges:
			type(self.mst.nodes[e.start])
			if self.mst.findSet(self.mst.nodes[e.start]) != self.mst.findSet(self.mst.nodes[e.end]):
				self.mst.union(self.mst.nodes[e.start],self.mst.nodes[e.end])
				self.mstedges.append([e.start,e.end])

		print("MST: ",self.mstedges)


G = Graph()
G.create()
G.Kruskal()



