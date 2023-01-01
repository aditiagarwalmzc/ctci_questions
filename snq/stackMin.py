from queue import Empty


class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        self.top += 1

        if not self.minStack:
            self.minStack.append(value)
        elif value < self.minStack[-1]:
            self.minStack.append(value)

    def pop(self):
        popped_val = self.stack[self.top]
        self.stack.pop()
        self.top -= 1

        if popped_val == self.minStack[-1]:
            self.minStack.pop()

    def min(self):
        return self.minStack[-1]

    def display(self):
        print(self.stack)

a = Stack()

a.push(9)
a.push(2)
a.push(1)
a.push(1)
a.push(4)
a.pop()
print(a.min())
a.display()

