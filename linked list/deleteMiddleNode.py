from requests import delete


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

    def delete_middle_node(self, n):
        temp = self.head
        while temp.next:
            if temp.next.value == n:
                temp.next = temp.next.next
            temp = temp.next
        return True

my_linked_list = LinkedList()
my_linked_list.append("a")
my_linked_list.append("b")
my_linked_list.append("c")
my_linked_list.append("d")
my_linked_list.append("e")
my_linked_list.append("f")
my_linked_list.delete_middle_node("c")
my_linked_list.print_list()