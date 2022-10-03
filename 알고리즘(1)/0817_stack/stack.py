class Stack:

    def __init__(self, size):
        self.size = size
        self.data = [None]*self.size
        self.top = -1

    def __str__(self):
        return f'{self.data}'

    def push(self, value):
        if self.isFull():
            print('overflow')
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.isEmpty():
            print('underflow')
            return 0
        else:
            self.top -= 1
            return self.data[self.top+1]

    def isEmpty(self):
        # if self.top == -1:
        #     return True
        # else:
        #     return False
        return self.top == -1

    def isFull(self):
        return self.top+1 == self.size

    def peek(self):
        return self.data[self.top]


size = 10
stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.isEmpty())
print(stack.isFull())
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)
print(stack.isEmpty())
print(stack.isFull())
