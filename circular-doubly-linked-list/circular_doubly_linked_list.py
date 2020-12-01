"""
Circular doubly linked list
"""

class CircularDoublyLinkedList:
    """
    Create a private class
    """
    class _Node:
        def __init__(self, value):
            self.value = value
            self.former_node = None
            self.next_node = None
    

    def __init__(self):
        self.head = None
        self.queue = None
        self.size = 0


    def __str__(self):
        """
        It shows the elements in the linked list
        """
        array = []
        current_node = self.head
        aux_pivot = True
        counter = self.size

        while counter != 0:
            if aux_pivot != False or current_node != self.head:
                array.append(current_node.value)
                current_node = current_node.next_node
                aux_pivot = False
                counter -= 1
            else:
                break
        return str(array) + " Size: " + str(self.size)
    

    def prepend(self, value):
        """
        It adds an element in the first position of the linked list

        Args:
            value ([type]): [given value]
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            self.head.former_node = new_node
            new_node.next_node = self.head
            self.queue.next_node = new_node
            new_node.former_node = self.queue
            self.head = new_node
        self.size += 1
    

    def append(self, value):
        """
        It adds an element at the end of the linked list

        Args:
            value ([type]): [given value]
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            self.queue.next_node = new_node
            new_node.former_node = self.queue
            new_node.next_node = self.head
            self.head.former_node = new_node
            self.queue = new_node
        self.size += 1


    def shift(self):
        """
        It deletes the first element of the linked list
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.head
            self.head = deleted_node.next_node
            self.head.former_node = self.queue
            self.queue.next_node = self.head
            deleted_node.former_node = None
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)


    def pop(self):
        """
        It deletes the last element of the linked list
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.queue
            self.queue = deleted_node.former_node
            self.queue.next_node = self.head
            self.head.former_node = self.queue
            deleted_node.former_node = None
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)


    def get(self, index):
        """
        It gets an element from any location in the linked list

        Args:
            index ([type]): [it is the reference]
        """
        if index == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif index == 0:
            print(self.head.value)
            return self.head
        elif not index >= self.size or index < 0:
            balanced_index = int(self.size / 2)
            if index <= balanced_index:
                current_node = self.head
                counter = 0

                while counter != index:
                    current_node = current_node.next_node
                    counter += 1
                print(current_node.value)
                return current_node
            else:
                current_node = self.queue
                counter = self.size - 1

                while counter != index:
                    current_node = current_node.former_node
                    counter -= 1
                print(current_node.value)
                return current_node
        else:
            return None


    def update(self, index, value):
        """
        It updates an element in the linked list

        Args:
            index ([type]): [it is the reference]
            value ([type]): [given value]
        """
        objective_node = self.get(index)
        if objective_node != None:
            objective_node.value = value
        else:
            return None


    def insert(self, index, value):
        """
        It inserts and element in any location in the linked list

        Args:
            index ([type]): [it is the reference]
            value ([type]): [given value]
        """
        if index == self.size - 1:
            return self.append(value)
        elif not index >= self.size or index < 0:
            new_node = self._Node(value)
            former_nodes = self.get(index)
            next_nodes = former_nodes.next_node
            former_nodes.next_node = new_node
            new_node.former_node = former_nodes
            new_node.next_node = next_nodes
            next_nodes.former_node = new_node
            self.size += 1
        else:
            return None


    def remove(self, index):
        """
        It removes an element from any location in the linked list

        Args:
            index ([type]): [it is the reference]
        """
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif not index >= self.size or index < 0:
            deleted_node = self.get(index)
            former_nodes = deleted_node.former_node
            next_nodes = deleted_node.next_node
            former_nodes.next_node = next_nodes
            next_nodes.former_node = former_nodes
            deleted_node.former_node = None
            deleted_node.next_node = None
            self.size -= 1
            return deleted_node
        else:
            return None


    def reverse(self):
        """
        It reverts the linked list
        """
        reverted_nodes = None
        self.head.former_node = None
        self.queue.next_node = None
        current_node = self.head
        self.queue = current_node

        while current_node != None:
            reverted_nodes = current_node.former_node
            current_node.former_node = current_node.next_node
            current_node.next_node = reverted_nodes
            current_node = current_node.former_node
        self.head = reverted_nodes.former_node
        self.head.former_node = self.queue
        self.queue.next_node = self.head



dll = CircularDoublyLinkedList()
dll.append('a')
dll.append('b')
dll.append('c')
dll.append('d')

dll.reverse()

print(dll)