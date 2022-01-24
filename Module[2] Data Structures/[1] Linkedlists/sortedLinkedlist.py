# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)

class SortedLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        
        if self.head is None:
            self.head = Node(value)
            return
        
        elif self.head.value > value:
            tempnode = Node(value)
            tempnode.next = self.head
            self.head = tempnode
            return
        
        node = self.head
        
        while node.next is not None:
            if node.next.value > value:
                tempnode = Node(value)
                tempnode.next = node.next
                node.next = tempnode
                return
            node = node.next
            
        node.next = Node(value)
        return
                

# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print ("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print ("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print ("Pass" if (node.value == 4) else "Fail")


def sort(array):
    """
    Given an array of integers, use SortedLinkedList to sort them and return a sorted array.

    Args:
       array(array): Array of integers to be sorted
    Returns:
       array: Return sorted array
    """
    sortedlist = SortedLinkedList()
    
    for element in array:
        sortedlist.append(element)
    
    sortedarray = []
    
    node = sortedlist.head
    
    while node is not None:
        sortedarray.append(int(str(node.value)))
        node = node.next
        
    return sortedarray

# Test case
print ("Pass" if (sort([4, 8, 2, 1, -3, 1, 5]) == [-3, 1, 1, 2, 4, 5, 8]) else "Fail")