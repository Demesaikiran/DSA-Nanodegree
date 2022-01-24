# Helper Code

from os import link

from numpy import flip


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
        linked_list(obj): Linked List to be reversed
    Returns:
        obj: Reveresed Linked List
    """
    new_list = LinkedList()
    previous = None
    
    for value in linked_list:
        new_node = Node(value)
        new_node.next = previous
        previous = new_node
    
    new_list.head = previous
    return new_list
        
"""
Testing Code Below
"""

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
print(flipped.head.value)
print(list(flipped) == list([0,-3,1,5,2,4]))
print(list(reverse(flipped))==(list(llist)))
is_correct = (list(flipped) == list([0,-3,1,5,2,4])) and (list(llist) == list(reverse(flipped)))
print(is_correct)
print("Pass" if is_correct else "Fail")