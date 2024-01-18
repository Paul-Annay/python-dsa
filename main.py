
left = [3, 7, 9] # this is a sorted array
right = [4, 8, 14] # this is another sorted array 

# merge 'left' and 'right'
# [3, 4, 7, 8, 9, 11]


def merge(left, right):
    array = [None] * (len(left) + len(right))
    i = 0 # to iterate over array
    j = 0 # to iterate over left
    k = 0 # to iterate over right

    while i < len(array) and j < len(left) and k < len(right):
        print(array[i], left[j], right[k])
        if left[j] < right[k]:
            array[i] = left[j]
            j += 1
        else:
            array[i] = right[k]
            k += 1
        i+=1

    while j < len(left) and i < len(array):
        array[i] = left[j]
        j += 1
        i += 1

    while k < len(right) and i < len(array):
        array[i] = right[k]
        k += 1
        i += 1
    
    return array
    