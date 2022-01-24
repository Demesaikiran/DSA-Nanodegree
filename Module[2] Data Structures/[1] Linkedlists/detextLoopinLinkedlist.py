class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start

def iscircular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
        linked_list(obj): Linked List to be checked
    Returns:
        bool: Return True if the linked list is circular, return False otherwise
    """
    slow_runner = linked_list.head
    fast_runner = slow_runner
    
    while slow_runner and fast_runner:
        slow_runner = slow_runner.next
        if fast_runner.next is not None:
            fast_runner = fast_runner.next.next
        else:
            return False
        if slow_runner == fast_runner:
            return True

    return False
    
    
# Test Cases

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print ("Pass" if iscircular(list_with_loop) else "Fail")                  # Pass
print ("Pass" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")   # Fail
print ("Pass" if iscircular(LinkedList([1])) else "Fail")                 # Fail
print ("Pass" if iscircular(small_loop) else "Fail")                      # Pass
print ("Pass" if iscircular(LinkedList([])) else "Fail")                  # Fail
