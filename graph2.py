# 单源最短路径 ： Dijkstra
# 顶点对之间最短路径 ：Floyd

class stack:
    def __init__(self):
        self.arr = []
    def push(self,p):
        self.arr.append(p)
    def pop(self):
        return self.arr.pop(0)
    def isempty(self):
        return 1 if len(self.arr)==0 else 0
class graph:
    def __init__(self,n):
        self.arr = []
        self.flag = []
        self.pointNum = n
        self.edge = 0
        self.maxValue = 8888
        for i in range(0,n):
            temp = []
            self.flag.append(0)
            for j in range(0,n):
                temp.append(self.maxValue)
            self.arr.append(temp)

    def setEdge(self,fro,to,value):
        self.arr[fro][to] = value

    def delEdge(self,fro,to):
        self.arr[fro][to] = 0
        self.arr[to][fro] = 0

    def show(self):
        for i in range(0,self.pointNum):
            for j in range(0,self.pointNum):
                print("{:^5d}".format(self.arr[i][j]),end=' ')
            print()
        # print('flag: ',self.flag)

    def resetFlag(self):
        for i in range(0,self.pointNum):
            self.flag[i] = 0

    def Dijkstra(self,s):
        # init
        newNode = [s]       # 已确定路径顶点集合
        pathLength = []     # 路径值
        frontNode = []      # 前驱结点
        allNode = []        # 所有节点
        for i in range(self.pointNum):
            allNode.append(i)
            frontNode.append(-1)
            pathLength.append(self.maxValue)
        pathLength[0] = 0
        # 循环：当所有节点路径都确定时退出
        while len(newNode) != len(allNode):
            # 找到最小边
            u = -1
            v = -1
            val = self.maxValue
            for i in range(self.pointNum):
                for j in range(self.pointNum):
                    if i in newNode and j not in newNode and self.arr[i][j] < val:
                        (u,v,val) = (i,j,self.arr[i][j])
            # 根据最小边更新状态
            if pathLength[u] + val < pathLength[v]:
                pathLength[v] = pathLength[u] + val
                frontNode[v] = u
                newNode.append(v)
        # 输出结果
        print(pathLength)
        for i in range(self.pointNum):
            if i != s:
                findPath(s,i,frontNode)

    def Floyd(self):
        # init
        adj = self.arr.copy()
        front = []
        print('former path :')
        for i in range(self.pointNum):
            x = []
            for j in range(self.pointNum):
                if i == j:
                    adj[i][j] = 0
                x.append(i)
            front.append(x)
            print(adj[i])
        # 三层循环迭代更新最短路径
        # 需要注意的是是对adj[j][k] 进行l次迭代，即里面的两层循环代表二维矩阵，最外层的循环表示进行l次
        for l in range(self.pointNum):
            for j in range(self.pointNum):
                for k in range(self.pointNum):
                    if adj[j][l] + adj[l][k] < adj[j][k] :
                        adj[j][k] = adj[j][l] + adj[l][k]
                        front[j][k] = l
        # output the result
        for i in range(0, self.pointNum):
            for j in range(0, self.pointNum):
                print("{:^5d}".format(adj[i][j]), end=' ')
            print()

def findPath(s,u,arr):
    p = u
    path = [u]
    while p != s:
        path.append(arr[p])
        p = arr[p]
    # path.append(p)
    path.reverse()
    print(path)

# dijkstra
g = graph(6)
g.setEdge(0,1,12)
g.setEdge(1,2,5)
g.setEdge(2,3,50)
g.setEdge(4,3,20)
g.setEdge(4,5,60)
g.setEdge(0,5,100)
g.setEdge(0,4,30)
g.setEdge(0,2,10)
g.setEdge(3,5,10)
#
# g.show()
# g.Dijkstra(0)

# floyd

h = graph(3)
h.setEdge(0,1,5)
h.setEdge(1,0,2)
h.setEdge(0,2,10)
h.setEdge(2,0,9)
h.setEdge(1,2,13)
h.setEdge(2,1,6)

h.show()
h.Floyd()