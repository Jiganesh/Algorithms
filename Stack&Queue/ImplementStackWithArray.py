class Stack : 

    def __init__(self):
        self.stack = []
        self.last = -1
        self.length = 0

    def push (self, element):
        self.last = element
        self.length += 1
        self.stack.append(element)

    def pop (self) : 
        self.length-=1
        element = self.stack.pop()
        self.last = -1 if self.length == 0 else self.stack[-1]
        return element

    def top(self):
        print(self.last)

    def size(self):
        print(self.length)




stack_instance = Stack()

stack_instance.push(2)
stack_instance.push(4)
stack_instance.push(6)
stack_instance.size() # 3


stack_instance.pop()
stack_instance.size() # 2
stack_instance.top() # 4
