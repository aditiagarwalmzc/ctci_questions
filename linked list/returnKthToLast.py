class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
        print("None")
    
    def kthToLast(self, k):
        temp = self.head
        for _ in range(self.length - k):
            temp = temp.next
        return temp.value
        
    def kthToLast_withoutLength(self, k):
        curr = self.head
        after = curr.next
        before = None

        while curr is not None:
            after = curr.next
            curr.next = before
            before = curr
            curr = after
        self.head = before

        temp = self.head
        for _ in range(1, k):
            temp = temp.next
        return temp.value


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.kthToLast_withoutLength(2))