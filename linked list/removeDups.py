# 1 -> 2 -> 3 -> 2 -> 4 -> None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.length = 1
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
        while temp is not None:
            print(temp.value, end = " -> ")
            temp = temp.next
        print("None")

    def remove_dups(self):
        hash = {}
        hash[self.head.value] = 1
        prev = self.head
        current = self.head.next

        while current is not None:
            if current.value not in hash:
                hash[current.value] = 1
                current = current.next
                prev = prev.next
            else:
                prev.next = current.next
                current = current.next

        return True

    def remove_dups_without_temp_buffer(self):
        current = self.head
        runner = self.head

        while current is not None:
            while runner.next is not None:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return True
    
            
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(4)
ll.print_list()
ll.remove_dups_without_temp_buffer()
ll.print_list()
