class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def push(self, val):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while self.s2:
            self.s1.append(self.s2.pop())
    
    def pop(self):
        self.s1.pop()

    def display(self):
        print(self.s1)

a = Stack()
a.push("a")
a.push("b")
a.push("c")
a.push("d")
a.pop()
a.display()

