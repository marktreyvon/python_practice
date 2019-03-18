# 二叉树、递归与非递归遍历
class stack:
    # num = -1
    arr = []
    # p = -1
    # def __init__(self):
    #     self.num = n
    #     self.p = -1
    #     if n <= 0:
    #         return
    #     else:
    #         for i in range(0,n):
    #             self.arr.append(-1)
    def show(self):
        if len(self.arr):
            print('num； ', len(self.arr), '  now:  ', self.arr[-1])
        else:
            print('num； ',len(self.arr))
        print('arr:  ',self.arr)
    def push(self,e):
        # if self.p == -1:
        #     # self.arr[0] = e
        #     self.arr.append(e)
        # else:
        #     self.arr[self.p+1] = e
        # self.p += 1
        self.arr.append(e)
        # print('add : ',e)
    def pop(self):
        # print('del : ',self.arr[-1])
        # self.arr[self.p] = -1
        # self.p -= 1
        return self.arr.pop(-1)

class node:
    value = 0
    l = 0
    r = 0
    # isl = 0
    # isr = 0
    def __init__(self,v):
        self.value = v
    def init(self,v):
        self.value = v
# 中序遍历 递归实现
    def ldr_r(self,s):
        if s.l:
            s.ldr_r(s.l)
        print(s.value,end='  ')
        if s.r:
            s.ldr_r(s.r)
# 前序遍历 递归实现
    def dlr_r(self,s):
        print(s.value,end='  ')
        if s.l:
            s.dlr_r(s.l)
        if s.r:
            s.dlr_r(s.r)
    def dlr_normal(self):
        print('前序非递归：',end='')
        s = stack()
        s.push(self)
        while s.arr:
            p = s.pop()
            print(p.value,end='-')
            if p.r:
                s.push(p.r)
            if p.l:
                s.push(p.l)
        print()

# 后序遍历
    def lrd(self):
        pass
    def add(self,n):
        pass
# 例子见大工数据结构教材P93
print('begin')
a0 = node('a')
a1 = node('b')
a2 = node('c')
a3 = node('d')
a4 = node('e')
a5 = node('f')
a6 = node('g')
a7 = node('h')
# a8 = node('')
a0.l = a1
a0.r = a2
a1.r = a3
a2.r = a4
a3.l = a5
a3.r = a6
a4.r = a7
a0.ldr_r(a0)
print()
a0.dlr_r(a0)
print()
a0.dlr_normal()

# 只写了前序遍历的非递归版本，中序后序其实原理都一样，就不重复了。关键在于利用栈。