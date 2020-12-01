"""
Stack LIFO Last In First Out
"""
class Stack:
    """
    The class Stack contains a private class called _Node
    """
    class _Node:
        """
        Constructor of this class
        """
        def __init__(self, value):
            self.value = value
            self.next_node = None
    

    def __init__(self):
        """
        Constructor
        """
        self.head = None
        self.queue = None
        self.size = 0
    

    def __str__(self):
        """
        It shows the elements of the list
        """
        array = []
        current_node = self.head

        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
        return str(array) + " Size: " + str(self.size)
    

    def push(self, value):
        """
        It adds an element at the beginning of the list
        It is the same as prepend in the linked list

        Args:
            value ([type]): [given value]
        """
        new_node = self._Node(value)
        if self.head == None or self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1
    

    def pop(self):
        """
        It deletes the first element of the list
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

stack = Stack()

stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
stack.push('E')

stack.pop()
print(stack)