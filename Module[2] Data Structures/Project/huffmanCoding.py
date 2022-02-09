from platform import node
import sys
import time
from unittest import result

from numpy import char
from scipy.misc import electrocardiogram

class Node:
    def __init__(self, count, character = None) -> None:
        self.child_0 = None
        self.child_1 = None
        self.count = count
        self.character = character

    def __str__(self):
        return "(char: {}, count: {})".format(self.character, self.count)


def encode(data, encoding):
    encoded_data = data

    for character in encoding:
        encoded_data = encoded_data.replace(character, encoding[character])
    
    return encoded_data

def generate_huffman_code(node, code = ""):
    encoding = {}

    if node:
        if not (node.child_0 or node.child_1):
            if code == "":
                encoding.update({node.character: "0"})
            else:
                encoding.update({node.character: code})
        
        encoding.update(generate_huffman_code(node.child_0, code + '0'))
        encoding.update(generate_huffman_code(node.child_1, code + '1'))

    return encoding


def huffman_encoding(data):

    # Initialising the frequencis count
    frequency = {}

    for character in data:
        frequency[character] = frequency.get(character, 0) + 1
    
    if len(frequency) < 2:
        if data == "":
            return "0", Node(1, "")
        else:
            return encode(data, generate_huffman_code(Node(1, data[0]))), Node(1, data[0])

    # Node with count making with their associated characters

    nodes = {}

    for character in frequency:
        nodes[character] = Node(frequency[character], character)
    
    # Tree generation

    priority = 1
    node_0 = node_1 = parent_node = None

    while len(nodes) > 1:

        priority_inversion = True
        min_priority = None

        for character in nodes:
            if nodes[character].count == priority:
                if not node_0:
                    node_0 = nodes[character]
                elif not node_1:
                    node_1 = nodes[character]
            elif not min_priority or nodes[character].count < min_priority:
                min_priority = nodes[character].count

            if node_0 and node_1:
                parent_node = Node(node_0.count + node_1.count, node_0.character + node_0.character)

                parent_node.child_0 = node_0
                parent_node.child_1 = node_1

                nodes[parent_node.character] = parent_node
                nodes.pop(node_0.character)
                nodes.pop(node_1.character)

                node_0 = None
                node_1 = None

                priority_inversion = False
                break
        
        if priority_inversion:
            priority = min_priority

    resultTree = parent_node

    encoding = generate_huffman_code(resultTree)
    encoded_data = encode(data, encoding)

    return encoded_data, resultTree


def generate_reverse_huffman_code(node, code = ""):
    decoding = {}

    if node:
        if not (node.child_0 or node.child_1):
            if code == "":
                decoding.update({'0': node.character})
            else:
                decoding.update({code: node.character})

        decoding.update(generate_reverse_huffman_code(node.child_0, code + '0'))
        decoding.update(generate_reverse_huffman_code(node.child_1, code + '1'))

    return decoding


def huffman_decoding(data,tree):
    
    decoding = generate_reverse_huffman_code(tree)
    
    message = code = ""

    for character in data:
        code += character

        if code in decoding:
            message += decoding[code]
            code = ""
    
    return message

    

    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    """ TEST - 2"""

    a_great_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))