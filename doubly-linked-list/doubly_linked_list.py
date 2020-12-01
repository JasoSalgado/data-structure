"""
It points to its next node and another property that points to its previous node
"""
class DoubleLinkedList:
    # Internal class
    class _Node:
        # Constructor
        def __init__(self, value):
            self.value = value
            self.former_node = None
            self.next_node = None


    def __init__(self):
        self.head = None
        self.queue = None
        self.size = 0


    def __str__(self):
        # It shows elements of the linked list
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node.value)
            current_node = current_node.next_node
        return str(array) + " Size: " + str(self.size)
        

    def prepend(self, value):
        """Insert an element at the beginning

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
            self.head = new_node
        self.size += 1

    
    def append(self, value):
        """Insert an element at the end

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
            self.queue = new_node
        self.size += 1


    def shift(self):
        """It deletes the first element of the linked list
        """
        if self.size == 0:
            self.head = None
            self.queue = None
        elif self.head != None:
            deleted_node = self.head
            self.head = deleted_node.next_node
            # We clean the deleted_node
            deleted_node.next_node = None
            self.size -= 1
            return print(deleted_node.value)
        else:
            return None


    def pop(self):

        if self.size == 0:
            self.head = None
            self.queue = None
        else:
            deleted_node = self.queue
            self.queue = deleted_node.former_node
            self.queue.next_node = None
            deleted_node.former_node = None
            self.size -= 1
            return print(deleted_node.value)


    def get(self, index):
        """It gets a node through the given index

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
            aux_index = int(self.size / 2)
            if index <= aux_index:
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
        """It updates the node´s value

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
        """It adds an element from any location in the linked list through a given index

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
            self.size +=1
        else:
            return None


    def remove(self, index):
        """It deletes an element from any location in the linked list through a given index

        Args:
            index ([type]): [it is the reference]
        """
        if index == 0:
            # It deletes the first element
            return self.shift()
        elif index == self.size - 1:
            # It deletes the last element
            return self.pop()
        elif not index >= self.size or index < 0:
            # We get the index
            deleted_node = self.get(index)
            former_nodes = deleted_node.former_node
            next_nodes = deleted_node.next_node
            former_nodes.next_node = next_nodes
            next_nodes.former_node = former_nodes
            # We clean the pointers
            deleted_node.former_node = None
            deleted_node.next_node = None
            self.size -= 1
            return deleted_node
        else:
            return None


    def reverse(self):
        """It reverts the nodes of the linked list
        """
        reverted_nodes = None
        current_node = self.head
        self.queue = current_node
        while current_node != None:
            reverted_nodes = current_node.former_node
            current_node.former_node = current_node.next_node
            current_node.next_node = reverted_nodes
            current_node = current_node.former_node
        self.head = reverted_nodes.former_node


# Instance
dll = DoubleLinkedList()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')

dll.reverse()

print(dll)