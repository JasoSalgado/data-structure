"""
Insertion sort
"""

def insertion_sort(list):
    """
    Insertion sort

    Args:
        list ([type]): [it will contain all elements]
    """
    # It starts in 1
    for i in range(1, len(list)):
        # if first element is higher than the second one, then change it
        while list[i - 1] > list[i] and i > 0:
            temporal_element = list[i]
            list[i] = list[i - 1]
            list[i - 1] = temporal_element
            i = i - 1
    return print(list)


l = [99, 10, 12, 5, 14, 20]
insertion_sort(l)

ll = [8, 5, 64, 33, 2, 2, 1]
insertion_sort(ll)