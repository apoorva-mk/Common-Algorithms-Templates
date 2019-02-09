import queue 
  
class Graph:
    def __init__(self,n):
        self.adjlist=[]
        self.v=n
        self.dist=[]
        for i in range(self.v):
            self.adjlist.append([])
            self.dist.append(-1)

    def connect(self,x,y):
        self.adjlist[x].append(y)
        self.adjlist[y].append(x)

    def find_all_distances(self,s):
        L = queue.Queue(maxsize=self.v) 
        L.put(s)
        self.dist[s]=0

        while((L.empty())==False):
            u=L.get()
            curr=curr+1
            for v in self.adjlist[u]:
                if self.dist[v]==-1:
                    self.dist[v]=self.dist[u]+1
                    L.put(v)

