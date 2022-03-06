def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number in (0, 1)):
        return number

    left = 1
    right = (number) // 2

    while( left <= right ):
        mid = (left + right) // 2

        if mid ** 2 == number:
            return mid
        
        if mid ** 2 < number:
            left = mid + 1
            answer = mid

        else:
            right = mid - 1

    return answer

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")