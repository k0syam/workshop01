MAX=10**5

class Stack:
    def __init__(self):
        self.top=0
        self.st=[0]*MAX
    
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top == MAX
    
    def push(self,x):
        if self.isFull():
            print('Error')
            return
        
        self.st[self.top] = x
        self.top += 1
    
    def pop(self):
        if self.isEmpty():
            print('Error')
            return -1
        self.top -= 1
        return self.st[self.top]

if __name__ == '__main__':
    s=Stack()
    s.push(3)
    s.push(5)
    s.push(7)

    print(s.pop())
    print(s.pop())

    s.push(9)
    print(s.pop())
    print(s.pop())