# Refering tHe snippet in https://engineeringnote.hateblo.jp/entry/python/algorithm-and-data-structures/linked_list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = Node(None)
 
    def insert(self, value):
        front = self.head
        rear = front.next
        while rear and value > rear.value:
            front = rear
            rear = rear.next
        Node = Node(value)
        Node.next = rear
        front.next = Node
 
    def print_list(self):
        tmp = self.head.next
        while tmp:
            print(tmp.value)
            tmp = tmp.next

names = ["yamamoto", "watanabe", "ito", "takahashi", "suzuki", "sato"]
linked_list = LinkedList()
for name in names:
    linked_list.insert(name)

# not worked so far...

