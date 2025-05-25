class Node :

    def __init__(self, val = -1 ):
        self.val = val 
        self.next = None


class StackWithLinkedList : 

    def __init__(self, head = None):
        self.head = head
        

    def push (self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def pop (self):
        node = self.head
        self.head = self.head.next if self.head.next else None
        return node.val


    def top (self):
        return self.head.val

    def print(self):
        curr = self.head
        while curr:
            print(curr.val , end=" ")
            curr = curr.next
        print()
        

stack_instance = StackWithLinkedList()

stack_instance.push(2)
stack_instance.push(4)
stack_instance.push(6)


stack_instance.print() # 2 4 6

stack_instance.pop()
stack_instance.top()

stack_instance.print() # 4 6

