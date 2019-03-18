# 堆的增删改查初始化
# 堆是完全二叉树的一种特殊情况，既然是完全二叉树，就能用数组来实现

#写是写完了，难是真的不难。核心在于如何上下级节点的交换值，增删初始化都用到了，这里封装成了transform函数+递归来实现，实在是懒得想好点的方法了。
def transform(arr,p):
    num = len(arr)
    lastbranch = num//2-1
    if p > lastbranch:
        return
    if p == lastbranch and num%2==0:
        (arr[p],arr[p*2+1]) = (arr[p],arr[p*2+1]) if arr[p]>arr[p*2+1] else (arr[p*2+1],arr[p])
        return
    if arr[p] < arr[p * 2 + 1]:
        arr[p], arr[p * 2 + 1] = arr[p * 2 + 1], arr[p]
        transform(arr,p*2+1)
    if arr[p] < arr[p * 2 + 2]:
        arr[p], arr[p * 2 + 2] = arr[p * 2 + 2], arr[p]
        transform(arr, p * 2 + 2)

class heap:
    arr = []

    def __init__(self,a):
        num = len(a)
        lastbranch = num//2-1
        for i in range(lastbranch,-1,-1):
            transform(a,i)
            # print('trans:',5-i,a)
        self.arr = a
    def add(self,p):
        self.arr.append(p)
        for i in range(len(self.arr)//2-1,-1,-1):
            transform(self.arr,i)
    def delete(self,p):
        num = len(self.arr)
        pos = self.arr.index(p)
        (self.arr[pos],self.arr[-1]) = (self.arr[-1],self.arr[pos])
        del self.arr[-1]
        lastbranch = num // 2 - 1
        for i in range(lastbranch, -1, -1):
            transform(self.arr, i)
            # print('trans:',5-i,a)

        pass
    def find(self,p):
        pass

a = [20,12,35,15,10,80,30,17,2,1]
print(a)
h = heap(a)
print('a: ',a)
print('heap',h.arr)
h.add(16)
print(h.arr)
h.delete(16)
print(h.arr)
h.delete(17)
print(h.arr)