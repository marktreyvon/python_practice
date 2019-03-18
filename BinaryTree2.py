# 线索二叉树略，以下为二叉搜索树增删改查
# 二叉树、递归与非递归遍历

# 主要难点在于二叉搜索树的两种删除上。需要考虑的条件很多，是否删除的是根节点，要删除的节点有几个子节点，
# 合并或者复制的时候寻找的删除节点的左（右）子树的最大（小）节点的子节点情况还需要考虑，正经的过程倒是不难。

# AVL树即平衡二叉树是一种特殊的二叉搜索树，其主要特色在于插入与删除时需要考虑各子树的平衡因子
# 插入有四种情况，删除有三种，大二课堂上不要求代码实现，这里也就偷懒不写了

class stack:
    arr = []
    def show(self):
        if len(self.arr):
            print('num； ', len(self.arr), '  now:  ', self.arr[-1])
        else:
            print('num； ',len(self.arr))
        print('arr:  ',self.arr)
    def push(self,e):
        self.arr.append(e)
    def pop(self):
        return self.arr.pop(-1)

class node:
    value = 0
    l = 0
    r = 0
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
    def add(self,p):
        compare = self
        while 1:
            if p.value < compare.value:
                if compare.l:
                    compare = compare.l
                    continue
                else:
                    compare.l = p
                    break
            else:
                if compare.r:
                    compare = compare.r
                    continue
                else:
                    compare.r = p
                    break
    def find(self,p):
        if self.value == p:
            return self
        compare = self
        while 1:
            if compare.value > p:
                if not compare.l:
                    return 0
                else:
                    compare = compare.l
                    continue
            elif compare.value == p:
                return compare
            else:
                if not compare.r:
                    return 0
                else:
                    compare = compare.r
                    continue
#递归实现返回节点的父节点:
    def find_parent(self,p):
        if self.value == p.value:
            return 0
        if self.l:
            if self.l.value == p.value:
                return self
            else:
                lback = self.l.find_parent(p)
                if lback:
                    return lback
        if self.r:
            if self.r.value == p.value:
                return self
            else:
                rback = self.r.find_parent(p)
                if rback:
                    return rback
#合并删除
    def del_merge(self,p):
        if not self.find(p):
            print('not found')
            return
        p = self.find(p)
        par = self.find_parent(p)
        # 删除的是根节点：
        if par:
            dir_par = 0
            if p.value == par.l.value:
                dir_par = 1
            if not p.l and not p.r:
                if dir_par == 1:
                    par.l = 0
                else:
                    par.r = 0
                print('del : ', p.value)
                return self
            elif not p.l and p.r:
                if dir_par == 1:
                    par.l = p.r
                else:
                    par.r = p.r
                print('del : ', p.value)
                return self
            elif not p.r and p.l:
                if dir_par == 1:
                    par.l = p.l
                else:
                    par.r = p.r
                print('del : ', p.value)
                return self
            # 有双子节点的情况：
            else:
                print('del : ', p.value)
                pchild = p.l
                while pchild.r:
                    pchild = pchild.r
                pchild.r = p.r
                if dir_par:
                    par.l = p.l
                else:
                    par.r = p.l
                return self
        else:
            if not p.l and not p.r:
                print('del : ', p.value)
                return 0
            elif not p.l and p.r:
                print('del : ', p.value)
                return p.r
            elif not p.r and p.l:
                print('del : ', p.value)
                return p.l
            # 有双子节点的情况：
            else:
                print('del : ', p.value)
                pchild = p.l
                while pchild.r:
                    pchild = pchild.r
                pchild.r = p.r
                return p.l
    def del_copy(self,p):
        if not self.find(p):
            print('not found')
            return
        p = self.find(p)
        par = self.find_parent(p)
        uncle = p.l
        if uncle.r:
            while uncle.r.r:
                uncle = uncle.r
        child = uncle.r
        uncle.r = child.l
        child.r = p.r
        child.l = p.l
        # 删除的不是根节点：
        if par:
            dir_par = 0
            if p.value == par.l.value:
                dir_par = 1
            if dir_par:
                par.l = child
            else:
                par.r = child
            return self
        else:
            return child

# 例子见大工数据结构教材P106图3-22a
print('begin')
a0 = node(400)
a1 = node(122)
a2 = node(450)
a3 = node(99)
a4 = node(250)
a5 = node(500)
a6 = node(110)
a7 = node(200)
a8 = node(300)
a9 = node(105)
a10 = node(330)
a0.add(a1)
a0.add(a2)
a0.add(a3)
a0.add(a4)
a0.add(a5)
a0.add(a6)
a0.add(a7)
a0.add(a8)
a0.add(a9)
a0.add(a10)
print('中序：')
a0.ldr_r(a0)
print()
a0=a0.del_copy(122)
print('中序：')
a0.ldr_r(a0)
print()
# print('前序：')
# a0.dlr_r(a0)
# print()
# print(a0.find(111))
# print()
# print(a0.find_parent(node(330)).value)

