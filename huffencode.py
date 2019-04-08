import heapq

class Node:
	def __init__(self):
		self.frequency=None
		self.symbol=None
		self.left=None
		self.right=None

	def __lt__(self,other):
		return self.frequency < other.frequency

	def printtree(self,root):
		if root!=None:
			print(root.frequency)
			self.printtree(root.left)
			self.printtree(root.right)

		else: 
			return


class HuffmanEncoding:
	def __init__(self):
		self.cost=0
		self.codes={}

	def Huffman(self, S,F):
		leaves=[]
		

		for i in range(len(S)):	
			node = Node()
			node.frequency = F[i]
			node.symbol = S[i]
			leaves.append(node)

		heapq.heapify( leaves )

		for i in range(len(S)):
			print(leaves[i].frequency," ",leaves[i].symbol)

		for i in range(len(S)-1):
			t1 = heapq.heappop(leaves)
			t2 = heapq.heappop(leaves)
			node = Node()
			node.frequency = t1.frequency + t2.frequency
			node.symbol = None
			node.left = t1
			node.right = t2

			heapq.heappush(leaves, node)

		return heapq.heappop(leaves)


	def encode(self,root, code):
		if(root.symbol!=None):
			print(root.symbol,code)
			self.cost=self.cost+len(code)*root.frequency
			self.codes[root.symbol]=code

		else:
			self.encode(root.left,code+"1")
			self.encode(root.right,code+"0")


# H=HuffmanEncoding()
# symb = [ 'a', 'b', 'c', 'd', 'e', 'f']
# freq = [ 20, 12, 10, 8, 4, 3]
# root=Node()
# root=H.Huffman(symb,freq)
# H.encode(root,"")
# print("File size:",H.cost)
# print(H.codes)
