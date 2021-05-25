class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class SLinkedList:
    def __init__(self, node):
        self.head = node
        
    def print_list(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.val)
            temp_node = temp_node.next
            
            
first = Node("One")
s_list = SLinkedList(first)

second = Node("Two")
third = Node("Three")
fourth = Node("Four")

first.next = second
second.next = third
third.next = fourth

s_list.print_list()

'''
Output:
One
Two
Three
Four

'''
