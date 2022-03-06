from cgi import test
from unittest import TestCase


def binary_search_recursive(array: list, target: int, start_index: int, end_index:int) -> int:
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index

    index_left_side = binary_search_recursive(array, target, start_index, mid_index - 1)
    index_right_side = binary_search_recursive(array, target, mid_index + 1, end_index)

    return max(index_left_side, index_right_side)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
        input_list(array), number(int): Input array to search and the target
    Returns:
        int: Index or -1
    """
    if len(input_list) == 0:
        return None
    return binary_search_recursive(array=input_list, target=number, start_index=0, end_index=len(input_list)-1)

def linear_search(input_list, number):
    if len(input_list) == 0:
        return None
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    if len(test_case[0]) == 0:
        print("Fail")
        return
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[3,4,5,6,7,9,1,2], 9])
test_function([[3,5,7,9,10,1], 100])
test_function([[]])