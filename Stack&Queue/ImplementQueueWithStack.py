class Queue : 

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue (self, element):

        self.stack1.append(element)

        
    def dequeue (self) : 

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        last_element = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        print(last_element)
        

    def top(self):
        print(self.stack1[0])

    def size(self):
        print(len(self.stack1))


queue_instance = Queue()

queue_instance.enqueue(2)
queue_instance.enqueue(4)
queue_instance.enqueue(6)
queue_instance.size() # 3


queue_instance.dequeue()
queue_instance.size() # 2
queue_instance.top() # 4
