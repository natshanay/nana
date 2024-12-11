class Stack:
    stack = []
    pointer = -1

    def push(self,element):
        self.stack.append(element)
        self.pointer+=1
    def pop(self):
        if (self.pointer==-1):
            print("stack under flow")
        else:
            value = self.stack[self.pointer]
            self.stack = self.stack[:-1]
            self.pointer -=1
            return value
        
    def peek(self):
        if (self.pointer==-1):
            print ("stack underflow")
        else:
            return self.stack[self.pointer]
# stack = Stack()
# stack.push(5)
# stack.push(55)
# stack.push(535)
# stack.push(53)
# stack.push(15)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

# print(stack.peek())

class Q:
    queue = []
    front=rear = -1
    
    def enque(self,element):
        if (self.front==-1 and self.rear==-1):
            self.queue.append(element)
            self.front=self.rear=0
        else:
            self.queue.append(element)
            self.rear+=1
    def deque(self):
        if (self.front ==-1 and self.rear==-1):
            print("stack under flow")
        elif (self.front==self.rear):
            self.front = self.rear =-1
        else:
            self.rear+=1
    def peek(self):
        if (self.front ==-1 and self.rear==-1):
            print("stack under flow")
        else:
            return self.queue[self.front]
qu = Q()
qu.enque(6)
qu.deque()
print(qu.peek())
            