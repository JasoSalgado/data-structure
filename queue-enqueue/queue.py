"""
Queue and Enqueue
"""

class Queue:
    class _Node:
        def __init__(self, value):
            """
            Constructor of the private class _Node

            Args:
                value ([type]): [given value]
            """
            self.value = value
            self.next_node = None
    

    def __init__(self):
        """
        Constructor of the class Queue
        """
        self.head = None
        self.queue = None
        self.size = 0
    

    def __str__(self):
        """
        It shows the elements in the list
        """
        array = []
        current_node = self.head

        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
        return str(array) + " Size: " + str(self.size)
    

    def enqueue(self, value):
        """
        It adds and element at the end of a list
        It is the same as append in the linked list

        Args:
            value ([type]): [given value]
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            self.queue.next_node = new_node
            self.queue = new_node
        self.size += 1
    

    def dequeue(self):
        """
        It deletes the first element of a list
        It is the same as shift in the linked list
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.head
            self.head = deleted_node.next_node
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)


queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')
queue.dequeue()

print(queue)