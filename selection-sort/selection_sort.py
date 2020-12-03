"""
Selection sort
"""

def selection_sort(list):
    """
    Selection sort

    Args:
        list ([type]): [it will contain all elements]
    """
    for i in range(len(list)):
        smallest_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest_index]:
                smallest_index = j
        if i != smallest_index:
            temporal_element = list[i]
            list[i] = list[smallest_index]
            list[smallest_index] = temporal_element
    return print(list)

l = [1, 8, 6, 2, 7, 5, 3, 4, 9, 10]
selection_sort(l)

ll = [8, 5, 64, 33, 2, 2, 1]
selection_sort(ll)