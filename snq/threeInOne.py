# 4 stacks instead of 3
class ThreeStacks:
    def __init__(self, cap):
        cap = cap * 4
        self.items = [None]*cap
        self.start = [0, cap//4, 2*(cap//4), 3*(cap//4)]

    def push(self, stackNo, value):
        self.items[self.start[stackNo]] = value
        self.start[stackNo] += 1

    def pop(self, stackNo):
         top = self.start[stackNo] - 1
         item = self.items[top]
         self.items[top] = None
         self.start[stackNo] += 1
         return item
    
    def peek(self, stackNo):
        top = self.start[stackNo] - 1
        item = self.items[top]
        return item
    
    def display(self):
        print(self.items)

a = ThreeStacks(3)
a.push(1, 'a')
a.pop(1)
a.display()