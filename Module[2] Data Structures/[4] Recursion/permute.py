import copy                                           # `copy` module

list1 = [0, 1, 2]
list2 = [7, 8, 9]                                     
compoundList1 = [list1, list2]                        # create a compound object


'''ASSIGNMENT OPERATION - Points a new reference to the existing object.'''
compoundList2 = compoundList1

# id() - returns the identity of the object passed
print(id(compoundList1) == id(compoundList2))          # True - compoundList2 is the same object as compoundList1
print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


'''SHALLOW COPY'''
compoundList2 = copy.copy(compoundList1)

print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
print(id(compoundList1[0]) == id(compoundList2[0]))    # True - compoundList2[0] is the same object as compoundList1[0]


'''DEEP COPY'''
compoundList2 = copy.deepcopy(compoundList1)

print(id(compoundList1) == id(compoundList2))          # False - compoundList2 is now a new object
print(id(compoundList1[0]) == id(compoundList2[0]))    # False - compoundList2[0] is now a new object

# Code

import copy

def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    
    final_comp_list = []
    
    if len(inputList) == 0:
        final_comp_list.append([])
    
    else:
        first_element = inputList[0]
        after_first   = inputList[1:]
        sub_permute   = permute(after_first)
        
        for listEntry in sub_permute:
            
            for i in range(len(listEntry) + 1):
                
                copyList = copy.deepcopy(listEntry)
                copyList.insert(i, first_element)
                final_comp_list.append(copyList)

    return final_comp_list


# Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")