class SetOfStacks:
    def __init__(self, cap):
        self.stacks = []
        self.cap = cap

    def push(self, val):
        if not(self.stacks):
            self.stacks.append([val])
        else:
            if len(self.stacks[-1]) >= self.cap:
                self.stacks.append([val])
            else:
                self.stacks[-1].append(val)
    
    def pop(self):
        if not self.stacks:
            raise ValueError("Stack is empty, can't pop mf")
        else:
            if len(self.stacks[-1]) == 1:
                self.stacks[-1].pop()
                self.stacks.pop()
            else:
                self.stacks[-1].pop()

    def popAt(self, index):
        if not self.stacks:
            raise ValueError("Stack is empty, can't pop mf")
        else:
            if len(self.stacks[index]) == 1:
                self.stacks[index].pop()
                self.stacks.remove([])
            else:
                self.stacks[index].pop()
    
    def display(self):
        print(self.stacks)


a = SetOfStacks(3)
a.push("a")
a.push("b")
a.push("c")
a.push("d")
a.push("e")
a.push("f")
a.push("g")
a.push("h")
a.popAt(1)
a.popAt(1)

a.popAt(1)
a.display()