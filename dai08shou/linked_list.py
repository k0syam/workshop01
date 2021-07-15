# linked_list.py
class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = Cell(None)
 
    def insert(self, value):
        front = self.head
        rear = front.next
        while rear and value > rear.value:
            front = rear
            rear = rear.next
        cell = Cell(value)
        cell.next = rear
        front.next = cell
 
    def delete(self, value):
        front = self.head
        rear = front.next
        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next
        if not rear:
            print("[*] Data not found")
            return
        front.next = rear.next
        rear = None
 
    def show(self):
        tmp = self.head.next
        while tmp:
            print(tmp.value)
            tmp = tmp.next
 
l = LinkedList()
print(l.head.value)
print('insert 3, 5, 1...')
l.insert(3)
l.insert(5)
l.insert(1)
print('print data')
l.show()
print('delete 3...')
l.delete(3)
print('print data')
l.show()