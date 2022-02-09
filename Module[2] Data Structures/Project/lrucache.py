
class Node(object):
    
    def __init__(self, data) -> None:
        self.data       = data 
        self.previous   = None
        self.next       = None

    def get_key(self):
        return self.data[0]

    def get_value(self):
        return self.data[1]


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = 0
        self.pageframe = {}
        self.head = None 
        self.tail = None
        if capacity < 0:
            print("The capacity given is INVALID")
            self.max_size = 0
            return
        self.max_size = capacity


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.max_size == 0:
            print("There is no operation possible as the cache is empty")
            return

        if key in self.pageframe:
            if self.pageframe[key].next:
                if self.pageframe[key].previous:
                    self.pageframe[key].previous.next = self.pageframe[key].previous
                else:
                    self.tail = self.pageframe[key].next
                
                self.pageframe[key].next.previous = self.pageframe[key].previous
                self.pageframe[key].previous      = self.head
                self.head.next                    = self.pageframe[key]
                self.head                         = self.pageframe[key]

            return self.pageframe[key].get_value()
        
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.max_size == 0:
            print("The Cache is empty... No operation is possible")
            return
        
        if key in self.pageframe:
            tempnode = self.pageframe[key]
            tempnode.data = (key, value)

            if tempnode.previous:
                tempnode.next.previous = tempnode.previous
            self.head.next = tempnode
            self.head = tempnode

            if self.tail == tempnode and tempnode.next is not None:
                del self.pageframe[self.tail.get_key()]
                self.tail = tempnode.next
            tempnode.next = None
            return
        
        if self.size == self.max_size:
            del self.pageframe[self.tail.get_key()]
            self.tail = self.tail.next
            self.size = 1
        
        tempnode = Node((key, value))
        if self.size == 0:
            self.head = self.tail = self.pageframe[key] = tempnode
            self.size += 1
            return

        tempnode.previous = self.head
        self.head.next = tempnode
        self.head = tempnode
        self.pageframe[key] = self.head
        self.size += 1

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(0)

our_cache.set(1,1)
our_cache.get(1)

our_cache = LRU_Cache(-1)
our_cache.set(1,1)
our_cache.get(1)
