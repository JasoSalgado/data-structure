# Single linked list - Lista enlazada simple
# Jaso Salgado jaso_98@hotmail.com

class SingleLinkedList:
    """[Class _Node with its constructor]
    """
    class _Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None


    def __init__(self):
        self.head = None
        self.queue = None
        self.size = 0


    def __str__(self):
        """Shows elements of the linked list
        """
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
        return str(array) + " Size: " + str(self.size)

    def prepend(self, value):
        """
            Adds an element to the beginning of a list
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size += 1


    def append(self, value):
        """Adds an element to the end of the linked list

        Args:
            value ([type]): [value to give]
        """
        new_node = self._Node(value)
        if self.head == None and self.queue == None:
            self.head = new_node
            self.queue = new_node
        else:
            self.queue.next_node = new_node
            self.queue = new_node
        self.size += 1


    def shift(self):
        """Deletes the first element of the linked list
        """
        # We check if the array is empty with the following if
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.head
            self.head = deleted_node.next_node
            # We clean the node
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)


    def pop(self):
        """Deletes the last element of a linked list
        """
        # We check if the array is empty
        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            current_node = self.head
            new_queue = current_node
            while current_node.next_node != None:
                new_queue = current_node
                current_node = current_node.next_node
            self.queue = new_queue
            # We clean the queue
            self.queue.next_node = None
            self.size -= 1
            return print(current_node.value)


    def get(self, index):
        """Gets a node through an index

        Args:
            index ([type]): [It is the pointer]

        Returns:
            [type]: [None]
        """
        if index == self.size - 1:
            print(self.cola.valor)
            return self.queue
        elif index == 0:
            print(self.head.value)
            return self.head
        # We see if the number is in the middle
        elif not (index >= self.size or index < 0):
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
        """Updates the node´s value through an index

        Args:
            index ([type]): [it is the pointer]
            value ([type]): [value to give]

        Returns:
            [type]: [None]
        """
        objective_node = self.get(index)
        if objective_node != None:
            objective_node.value = value
        else:
            return None


    def insert(self, index, value):
        """Adds an element in any location in the linked list through its index

        Args:
            index ([type]): [it is an index]
            value ([type]): [A value to add]
        """
        if index == self.size - 1:
            return self.append(value)
        elif not (index >= self.size or index < 0):
            new_node = self._Node(value)
            former_nodes = self.get(index)
            next_nodes = former_nodes.next_node
            former_nodes.next_node = new_node
            new_node.next_node = next_nodes
            self.size += 1
        else:
            return None


    def remove(self, index):
        """Takes out an element from any location in the linked list through an index

        Args:
            index ([type]): [It is the reference]
        """
        if index == 0:
            return self.shift()
        elif index == self.size - 1:
            return self.pop()
        elif not (index >= self.size or index < 0):
            former_nodes = self.get(index - 1)
            removed_node = former_nodes.next_node
            former_nodes.next_node = removed_node.next_node
            removed_node.next_node = None
            self.size -= 1
            return removed_node
        else:
            return None


    def reverse(self):
        """Revert the linked list
        """
        reverted_nodes = None
        current_node = self.head
        self.queue = current_node
        while current_node != None:
            next_node = current_node.next_node
            current_node.next_node = reverted_nodes
            reverted_nodes = current_node
            current_node = next_node
        self.head = reverted_nodes
        return self.head


sll = SingleLinkedList()

sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')

sll.reverse()

print(sll)

