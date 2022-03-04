def fastSelect(Arr, k):
    n = len(Arr)
    
    if k> 0 and k <= n:
        
        set_of_median = []
        arr_less_k = []
        arr_eq_k = []
        arr_more_k = []
        i = 0
        
        while i < n // 5:
            median = findMedian(Arr, 5 * i, 5)
            set_of_median.append(median)
            i += 1
            
        if 5 * i < n:
            median = findMedian(Arr, 5 * i, n % 5)
            set_of_median.append(median)

        if len(set_of_median) == 1:
            pivot = set_of_median[0]
        elif len(set_of_median) > 1:
            pivot = fastSelect(set_of_median, len(set_of_median) // 2)
        
        for element in Arr:
            if element < pivot:
                arr_less_k.append(element)
            elif element > pivot:
                arr_more_k.append(element)
            else:
                arr_eq_k.append(element)
                
        if k <= len(arr_less_k):
            return fastSelect(arr_less_k, k)
        elif k > len(arr_less_k) + len(arr_eq_k):
            return fastSelect(arr_more_k, k - (len(arr_less_k) + len(arr_eq_k)))
        else:
            return pivot
    

def findMedian(Arr, start, size):
    my_list = []
    
    for i in range(start, start + size):
        my_list.append(Arr[i])
        
    my_list.sort()
    return my_list[size // 2]


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99