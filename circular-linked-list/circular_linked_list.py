"""
Circular linked list
"""

class CircularLinkedList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
    

    def __init__(self):
        self.head = None
        self.queue = None
        self.size = 0
    

    def __str__(self):
        """It shows the elements of the linked list
        """
        array = []
        current_node = self.head
        aux_pivot = True
        counter = self.head

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
        """It add a new value at the beginning

        Args:
            value ([type]): [given value]
        """
        new_queue = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            new_node.next_node = self.head
            self.queue.next_node = new_node
            self.head = new_nod
        self.size += 1
    

    def append(self, value):
        """It adds an element at the end of the list

        Args:
            value ([type]): [given value]
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            self.queue.next_node = new_node
            new_node.next_node = self.head
            self.queue = new_node
        self.size += 1


    def shift(self):
        """It deletes the element of the beginning
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.head
            self.head = deleted_node.next_node
            self.queue.next_node = self.head
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)

    
    def pop(self):
        """It deletes the last element of the list
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            current_node = self.head
            new_queue = current_node
            counter = self.size

            while counter != 0:
                if current_node.next_node != self.head:
                    new_queue = current_node
                    current_node = current_node.next_node
                else:
                    break
            self.queue = new_queue
            self.queue.next_node = self.head
            self.size -= 1
            return print(current_node.value)


    def get(self, index):
        """It gets an element through an index

        Args:
            index ([type]): [it is the reference]
        """
        if index == self.size - 1:
            print(self.queue.value)
            return self.queue
        elif index == 0:
            return self.head
        elif not index >= self.size or index < 0:
            current_node = self.head
            counter = 0

            while counter != index:
                current_node = current_node.next_node
                counter += 1
            print(current_node.value)
            return current_node
        else:
            return None
    

    def update(self, index, value):
        """It updates the list

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
        """It adds an element in any location in the list

        Args:
            index ([type]): [it is the reference]
            value ([type]): [given value]
        """
        if index == self.size - 1:
            return self.append(value)
        elif not index >= self.size or index < 0:
            new_node = self._Node(value)
            former_nodes = self.get(index)
            next_nodes = next_nodes.next_node
            former_nodes.next_node = new_node
            new_node.next_node = next_nodes
            self.size += 1
        else:
            return None

    
    def remove(self, index):
        """It deletes an element through the index

        Args:
            index ([type]): [it is the reference]
        """
        if index == 0:
            # It deletes the first element
            return self.shift()
        elif index == self.size -1 :
            return self.pop()
        elif index >= self.size or index < 0:
            former_nodes = self.get(index - 1)
            deleted_node = former_nodes.next_node
            former_nodes.next_node = deleted_node.next_node
            deleted_node.next_node = None
            self.size -= 1
            return deleted_node
        else:
            return None

    
    def reverse(self):
        """It reverts the list
        """
        reverted_nodes = None
        current_node = self.head
        self.queue = current_node
        aux_pivot = True
        counter = self.size

        while counter != 0:
            if aux_pivot != False or current_node != self.head:
                next_node = current_node.next_node
                current_node.next_node = reverted_nodes
                current_node = next_node
                aux_pivot = False
                counter -= 1
            else:
                break
        self.head = reverted_nodes
        self.queue.next_node = self.head