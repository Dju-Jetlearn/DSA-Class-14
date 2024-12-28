class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range (V)]
    
    def addedge(self, a, b):
        self.adj[a].append(b)
        self.adj[b].append(a)

    def DFSutil(self, temp, a, visited):
        visited[a] = True
        temp.append(a)
        for i in self.adj[a]:
            if visited[i] == False:
                temp = self.DFSutil(temp, i, visited)
        return temp
    
    def connectedcomp(self):
        visited = []
        cc = []#results variable
        for i in range(self.V):
            visited.append(False) # makes all vertices false because you haven't visited them yet
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSutil(temp, v, visited))
        return cc

vert = Graph(5)
vert.addedge(0,1)
vert.addedge(2,3)
vert.addedge(3,4)
vert.addedge(2,4)

cc = vert.connectedcomp()#1 always put object name#(vert) in front of function name(connectedcomp) #2 means that all the results of connectcomp are put into cc

print("Below are the connected components in vert. Hope you have fun with them.")
print(cc)