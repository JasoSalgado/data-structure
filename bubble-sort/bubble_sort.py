"""
Bubble sort
"""

def bubble_sort(list):
    """
    Bubble sort 

    Args:
        list ([type]): [it will contain all elements]
    """
    # -1 start, 0 stop, -1 step
    for i in range(len(list) -1, 0, -1):
        change_done = True
        for j in range(i):
            if list[j] > list[j + 1]:
                # Temporal element will contain the remaining list
                temporal_element = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temporal_element
                change_done = False
        if change_done == True:
            break
    return print(list)


l = [1, 8, 6, 2, 7, 5, 3, 4, 9, 10]
bubble_sort(l)

ll = [8, 5, 64, 33, 2, 2, 1]
bubble_sort(ll)