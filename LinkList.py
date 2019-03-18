class node:
    name = ''
    code = -1
    age = -1
    next = -1
    def __init__(self):
        self.age = -1
        self.code = -1
        self.name = -1
    def link(self,ne=-1):
        self.next = ne
    def init(self,age,code,name):
        self.name = name
        self.age = age
        self.code = code

class link:
    first = -1
    num = -1
    end = -1
    now = -1
    def __init__(self,fir):
        self.num = 1
        self.end = fir
        self.first = fir
        self.now = self.first
    def tonext(self):
        print(self.now.code,end=' to ')
        self.now = self.now.next
        print(self.now.code)
    def show(self):
        print('num = ',self.num,'  now:',self.now.code)
        print('first:', self.first.code, '  end:', self.end.code)
    def add(self,ne):
        self.end.link(ne)
        self.end = self.end.next
        self.num += 1
        print(self.end.code, ' is added ')
a1 = node()
a1.init(12,'001','mike')
a2 = node()
a2.init(12,'002','mary')
a3 = node()
a3.init(12,'003','jack')
a = link(a1)
a.add(a2)
a.add(a3)
a.show()