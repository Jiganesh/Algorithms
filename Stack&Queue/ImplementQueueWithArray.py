class Queue : 

    def __init__(self):
        self.queue = []
        self.last = -1
        self.length = 0

    def enqueue (self, element):
        self.last = element
        self.length += 1
        self.queue.append(element)

    def dequeue (self) : 
        self.length-=1
        element = self.queue.pop(0)
        self.last = -1 if self.length == 0 else self.queue[0]
        return element

    def top(self):
        print(self.last)

    def size(self):
        print(self.length)


queue_instance = Queue()

queue_instance.enqueue(2)
queue_instance.enqueue(4)
queue_instance.enqueue(6)
queue_instance.size() # 3


queue_instance.dequeue()
queue_instance.size() # 2
queue_instance.top() # 4
