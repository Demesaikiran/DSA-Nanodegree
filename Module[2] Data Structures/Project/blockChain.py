import datetime
import hashlib



class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = (str(self.data).encode('utf-8') + 
                    str(self.previous_hash).encode('utf-8') +
                    str(self.timestamp).encode('utf-8'))

        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return 'BlockHash: {}\nTimeStamp: {}\nData: {}\nPreviousHash: {}\n'.format(self.hash, self.timestamp, self.data, self.previous_hash)

class Node:
    def __init__ (self, data, previous_hash):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        self.tail = None


class BlockChain:
    def __init__(self):
        self.head = None
    
    def append(self, data = None):
        if data is None:
            print("Cannot store the empty block")
            return

        if not self.head:
            self.head = Node(data, None)
            self.tail = self.head 
        
        else:
            self.tail.next = Node(data, self.tail.block.hash)
            self.tail      = self.tail.next

    def __str__(self):
        if self.head is None:
            return "The Block chain is Empty"
        
        currentnode = self.head
        result = ""

        while currentnode:
            result      += str(currentnode.block)
            currentnode  = currentnode.next

        return result


"""TEST -1 """
test1 = BlockChain()
test1.append("info-1")
test1.append("info-2")
test1.append("info-3")
test1.append("info-4")
test1.append("info-5")

print(test1)
# Outputs 4 blocks

""" TEST - 2"""
test2 = BlockChain()
print(test2)
# OUTPUTS BLOCK CHAIN IS EMPTY

""" TEST - 3"""
test3 = BlockChain()
test3.append()
test3.append("Info-1")
print(test3)
#outputs only one block

""" TEST - 4 """
test4 = BlockChain()
test4.append("info-1")
print(test4.head.block.timestamp)
test4.append("info-2")
print(test4.head.block.timestamp)
