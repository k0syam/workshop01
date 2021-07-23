class Heap:
    def __init__(self):
        self.h=[]
    
    #挿入
    def push(self,x):
        self.h.append(x)
        self.i=len(self.h)-1
        while self.i > 0:
            self.p=(self.i-1)//2

            if self.h[self.p] >= x:
                break
            self.h[self.i]=self.h[self.p]
            self.i=self.p
        self.h[self.i]=x

    def top(self):
        if len(self.h):
            return self.h[0]
        else:
            return -1
    
    def pop(self):
        if not len(self.h):
            return
        

