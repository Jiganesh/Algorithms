from collections import deque;

class StackUsingQueue:

    def __init__(self):
        self.queue = deque([])

    def push (self, val):
        length = len(self.queue)
        self.queue.append(val)

        for i in range (length):
            self.queue.append(self.queue.popleft())


    def pop (self):
        self.queue.popleft()


    def top (self):
        print(self.queue[0])


    def size (self):
        print(len(self.queue))
        

stack_instance = StackUsingQueue()

stack_instance.push(2)
stack_instance.push(4)
stack_instance.push(6)
stack_instance.size() # 3


stack_instance.pop()
stack_instance.size() # 2
stack_instance.top() # 4
