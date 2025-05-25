class Node :

    def __init__(self, val = -1 ):
        self.val = val 
        self.next = None


class QueueWithLinkedList : 

    def __init__(self, head = None):
        self.head = self.rear = head
        

    def enqueue (self, val):
        node = Node(val)
        if self.rear:
            self.rear.next = node
            self.rear = self.rear.next
        else:
            self.head = self.rear = node

    def dequeue (self):
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
        


queue_instance = QueueWithLinkedList()

queue_instance.enqueue(2)
queue_instance.enqueue(4)
queue_instance.enqueue(6)


queue_instance.print() # 2 4 6

queue_instance.dequeue()
queue_instance.top()

queue_instance.print() # 4 6

