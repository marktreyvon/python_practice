# 顺序栈
# class stack:
#     num = -1
#     arr = []
#     p = -1
#     def __init__(self,n = 0):
#         self.num = n
#         self.p = -1
#         if n <= 0:
#             return
#         else:
#             for i in range(0,n):
#                 self.arr.append(-1)
#     def show(self):
#         print('num； ',self.num,'  now:  ',self.p)
#         print(self.arr)
#     def push(self,e):
#         if self.p == -1:
#             self.arr[0] = e
#         else:
#             self.arr[self.p+1] = e
#         self.p += 1
#         print('add : ',e)
#     def pop(self):
#         print('del : ',self.arr[self.p])
#         self.arr[self.p] = -1
#         self.p -= 1

#  利用python特性的版本：
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
        print('add : ',e)
    def pop(self):
        print('del : ',self.arr[-1])
        # self.arr[self.p] = -1
        # self.p -= 1
        self.arr.pop(-1)


a = [1,2,3,4,5,6,7,8,9]
s = stack()
s.show()
n = len(a)
for i in range(0,n):
    s.push(a[n-1-i])
    if i == 3 or i == 8:
        s.pop()
    else:
        pass
s.show()

# 栈比较简单就这样吧。顺序栈和链式栈差不多，就不实现了。