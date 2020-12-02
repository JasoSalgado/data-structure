"""
General tree 
It uses a circular list CSLL 
"""
class Tree:
    """
    Class CSLL
    """
    class Csll:
        """
        Public class
        """
        class Node:
            """
            Constructor
            """
            def __init__(self, value, father):
                self.value = value
                self.father = father
                self.child = None
                self.next_node = None
        

        def __init__(self):
            """
            Node´s constructor
            """
            self.head = None
            self.queue = None
            self.size = 0
        

        def append(self, value, father):
            """
            It adds an element

            Args:
                value ([type]): [given value]
                father ([type]): [it is the root]
            """
            new_node = self.Node(value, father)
            if self.head == None and self.queue == None:
                self.head = new_node
                self.queue = new_node
                self.queue.next_node = self.head
            else:
                self.queue.next_node = new_node
                new_node.next_node = self.head
                self.queue = new_node
            self.size += 1
        

    def __init__(self):
        """
        Csll´s constructor
        """
        self.root = None
        self.size = 0
        

    def insert(self, value, father):
        """
        It inserts an element

        Args:
            value ([type]): [given value]
            father ([type]): [it is the father in the tree]
        """
        if self.root == None:
            # We create a new root with the class Csll()
            self.root = self.Csll()
            # We add an element
            self.root.append(value, None)
        else:
            current_node = self.root.head
            def go_through(node, test_node=None):
                """
                It is a function that goes through the tree 

                Args:
                    node ([type]): [pointer]
                    test_node ([type], optional): [it helps to go up or down]. Defaults to None.
                """
                aux_node = node.father
                if value == father:
                    return False
                elif node.value == father:
                    if node.child == None:
                        node.child = self.Csll()
                        node.child.append(value, node)
                        self.size += 1
                        return True
                    else:
                        node.child.append(value, node)
                        self.size += 1
                        return True
                else:
                    if node.child != None:
                        if node.child.head.value == test_node:
                            if node.value == self.root.head.value:
                                return False
                            elif node.next_node.value != aux_node.child.head.value:
                                return go_through(node.next_node, node.value)
                            else:
                                return go_through(node.father, node.next_node.value)
                        else:
                            return go_through(node.child.head, node.child.head.value)
                    elif node.next_node.value != aux_node.child.head.value:
                        return go_through(node.next_node, node.value)
                    else:
                        return go_through(node.father, node.next_node.value)
            return go_through(current_node)


    def find(self, value):
        """
        It looks for a node

        Args:
            value ([type]): [given value]
        """
        current_node = self.root.head
        def go_through(node, test_node=None):
            aux_node = node.father
            if node.value == value:
                # It found the node
                return node.value
            elif node.child != None:
                if node.child.head.value == test_node:
                    if node.value == self.root.head.value:
                        return 'It does not exist the node you are looking for'
                    elif node.next_node.value != aux_node.child.head.value:
                        return go_through(node.next_node, node.value)
                    else:
                        return go_through(node.father, node.next_node.value)
                else:
                    return go_through(node.child.head, node.child.head.value)
            elif node.next_node.value != aux_node.child.head.value:
                return go_through(node.next_node, node.value)
            else:
                return go_through(node.father, node.next_node.value)
        found_node = go_through(current_node)
        return print(found_node)
                    

    def preorder(self):
        """
        Preorder the list
        """
        container = []
        current_node = self.root.head
        def go_through(node, test_node=None):
            aux_node = node.father
            if node.child != None:
                if node.child.head.value == test_node:
                    if node.value == self.root.head.value:
                        return None
                    elif node.next_node.value != aux_node.child.head.value:
                        return go_through(node.next_node, node.value)
                    else:
                        return go_through(node.father, node.next_node.value)
                else:
                    container.append(node.value)
                    return go_through(node.child.head, node.child.head.value)
            elif node.next_node.value != aux_node.child.head.value:
                container.append(node.value)
                return go_through(node.next_node, node.value)
            else:
                container.append(node.value)
                return go_through(node.father, node.next_node.value)
        go_through(current_node)
        return print(container)


    def postorder(self):
        """
        Postorder
        """
        container = []
        current_node = self.root.head
        def go_through(node, test_node=None):
            aux_node = node.father
            if node.child != None:
                if node.child.head.value == test_node:
                    container.append(node.value)
                    if node.value == self.root.head.value:
                        return None
                    elif node.next_node.value != aux_node.child.head.value:
                        return go_through(node.next_node, node.value)
                    else:
                        return go_through(node.father, node.next_node.value)
                else:
                    return go_through(node.child.head, node.child.head.value)
            elif node.next_node.value != aux_node.child.head.value:
                container.append(node.value)
                return go_through(node.next_node, node.value)
            else:
                container.append(node.value)
                return go_through(node.father, node.next_node.value)
        go_through(current_node)
        return print(container)



tree = Tree()

tree.insert('a', None)
tree.insert('b', 'a')
tree.insert('c', 'a')
tree.insert('d', 'b')
tree.insert('w', 'b')
tree.insert('z', 'b')
tree.insert('m', 'd')
tree.insert('n', 'd')
tree.insert('y', 'd')
tree.insert('q', 'm')
tree.insert('i', 'n')
tree.insert('h', 'i')
tree.insert('g', 'i')
tree.insert('e', 'c')
tree.insert('f', 'c')
tree.insert('l', 'f')
tree.insert('s', 'f')
tree.insert('p', 'f')
tree.insert('o', 's')

tree.find('w')
print('*******')
tree.preorder()
print('********')
tree.postorder()

