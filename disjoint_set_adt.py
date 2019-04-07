class Node:
	def __init__(self,x):
		self.parent=self
		self.value=x
		self.rank=0

class disjoint_adt:
	def __init__(self):
		self.nodes=[]

	def findSet(self,x):
		if x.parent!=x:
			x.parent=self.findSet(x.parent)

		return x.parent

	def makeSet(self,x):
		#new=Node(x)
		self.nodes.append(x)


	def union(self,x,y):
		rx=self.findSet(x)
		ry=self.findSet(y)

		if(rx.rank>ry.rank):
			ry.parent=rx

		elif(rx.rank<ry.rank):
			rx.parent=ry

		else:
			ry.parent=rx
			rx.rank=rx.rank+1

	def printSet(self):
		for i in self.nodes:
			print (i.value,"->",i.parent.value)

ADT=disjoint_adt()
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
ADT.makeSet(a)
ADT.makeSet(b)
ADT.union(a,b)
ADT.makeSet(c)
ADT.union(b,c)
ADT.makeSet(d)
ADT.union(a,d)
print(ADT.findSet(d).value)
ADT.printSet()




