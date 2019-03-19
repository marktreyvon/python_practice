# 图的实现：邻接矩阵存储法及其遍历，构造最小生成树的两种方法：Prim  Kruskal
# DFS采用递归，BFS非递归,遍历是否指定开始节点均可，这里的均为指定版本的
# g为P160 图4-12  gg为P163图4-15a
# Prim是一个加点的过程，而Kruskal是一个加边的过程。

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
        for i in range(0,n):
            temp = []
            self.flag.append(0)
            for j in range(0,n):
                temp.append(0)
            self.arr.append(temp)

    def setEdge(self,fro,to,value):
        self.arr[fro][to] = value
        self.arr[to][fro] = value

    def delEdge(self,fro,to):
        self.arr[fro][to] = 0
        self.arr[to][fro] = 0

    def show(self):
        for i in range(0,self.pointNum):
            print(self.arr[i])
        print('flag: ',self.flag)

    def resetFlag(self):
        for i in range(0,self.pointNum):
            self.flag[i] = 0

    def DFS_r(self,begin,re):
        if self.flag[begin]:
            return
        else:
            if begin == re:
                print('DFS: ',end='')
            print(begin,end=' ')
            self.flag[begin] = 1
            other = -1
            for i in range(0,self.pointNum):
                if self.arr[begin][i] and not self.flag[i]:
                    other = i
                    self.DFS_r(other,re)
            if sum(self.flag) == len(self.flag) and begin == re:
                self.resetFlag()
                print()

    def BFS(self,begin):
        print(end='BFS:')
        s = stack()
        s.push(begin)
        self.flag[begin] = 1
        while not s.isempty():
            temp = s.pop()
            print(temp,end=' ')
            for i in range(self.pointNum):
                if self.arr[temp][i] and not self.flag[i]:
                    self.flag[i] = 1
                    s.push(i)
        self.resetFlag()

    def prim(self):# 返回最后生成树的边的集合
        # init:
        temparr = self.arr.copy() # 临时存储所有边
        added = []  # 已经加入生成树的节点
        maxValue = 100  # 边权最大值，用于找到最小边，也可用堆实现
        storeEdge = []  #最后结果
        for i in range(self.pointNum):
            temp = []
            for j in range(self.pointNum):
                temp.append(0)
            storeEdge.append(temp)
        # find the smallest edge:
        firstPoint = maxValue
        firstFrom = -1
        firstTo = -1
        for i in range(self.pointNum):
            for j in range(self.pointNum):
                if self.arr[i][j]>0 and self.arr[i][j] < firstPoint:
                    firstPoint = self.arr[i][j]
                    firstFrom = i
                    firstTo = j
        storeEdge[firstFrom][firstTo] = firstPoint
        storeEdge[firstTo][firstFrom] = firstPoint
        added.append(firstFrom)
        added.append(firstTo)
        print('find:',firstFrom,'-',firstTo)
        # loop
        while len(added) != self.pointNum:
            # find the smallest edge whose point is added
            val = maxValue
            u = -1
            v = -1
            for i in range(self.pointNum):
                for j in range(self.pointNum):
                    if (i in added and j not in added or i not in added and j in added) and \
                            temparr[i][j] < val and temparr[i][j]:
                        u = i
                        v = j
                        val = temparr[i][j]
            print('find ',u,'-',v)
            temparr[u][v] = 0
            temparr[v][u] = 0
            storeEdge[u][v] = val
            storeEdge[v][u] = val
            if u in added and v not in added:
                added.append(v)
            elif v in added and u not in added:
                added.append(u)
        for i in range(self.pointNum):
            print(storeEdge[i])
        return storeEdge

    def kruskal(self):
        # sort the edge
        edge = []
        for i in range(self.pointNum):
            for j in range(self.pointNum):
                if [self.arr[i][j],i,j] not in edge and [self.arr[i][j],j,i] not in edge \
                        and self.arr[i][j]>0:
                    edge.append([self.arr[i][j],i,j])
        edge.sort()
        # construct ufset:
        point = []
        for i in range(self.pointNum):
            point.append([i])
        # print(point)
        storeEdge = []
        for i in range(len(edge)):
            if judge(point,edge[i][1],edge[i][2]):
                storeEdge.append(edge[i])
        for i in range(len(storeEdge)):
            print(storeEdge[i])


# judge u,v in same set
def judge(arr,u,v):
    uflag = -1
    vflag = -1
    for i in range(len(arr)):
        if u in arr[i]:
            uflag = arr[i]
        if v in arr[i]:
            vflag = arr[i]
    if uflag == vflag :
        return False
    else:
        t = uflag+vflag
        arr.remove(uflag)
        arr.remove(vflag)
        arr.append(t)
        return True

# 图的初始化
g = graph(8)
g.setEdge(0,1,1)
g.setEdge(0,2,2)
g.setEdge(2,6,1)
g.setEdge(2,5,3)
g.setEdge(1,3,3)
g.setEdge(1,4,5)
g.setEdge(3,7,4)
g.setEdge(4,7,4)
g.setEdge(5,6,2)

gg = graph(6)
gg.setEdge(0,1,6)
gg.setEdge(0,2,1)
gg.setEdge(0,3,5)
gg.setEdge(1,2,5)
gg.setEdge(2,3,5)
gg.setEdge(1,4,3)
gg.setEdge(2,4,6)
gg.setEdge(2,5,4)
gg.setEdge(3,5,2)
gg.setEdge(4,5,6)
# g.DFS_r(0,0)
# g.BFS(0)
# print()
# g.show()
gg.show()
# gg.prim()
gg.kruskal()