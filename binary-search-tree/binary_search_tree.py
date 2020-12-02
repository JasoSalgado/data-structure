"""
Binary search
Branch left is less than branch right
"""

class BinarySearchTree:
    class Node:
        def __init__(self, value):
            """
            Constructor

            Args:
                value ([type]): [given value]
            """
            self.value = value
            self.left_branch = None
            self.right_branch = None
    

    def __init__(self):
        """
        Constructor
        """
        self.root = None
        self.size = None

    
    def insert(self, value):
        """
        It inserts an element

        Args:
            value ([type]): [given value]
        """
        new_node = self.Node(value)
        if self.root == None:
            self.root = new_node
        else:
            def go_through(value, node):
                """
                Function that goes through the tree

                Args:
                    value ([type]): [given value]
                    node ([type]): [node to go through]
                """
                if value == node.value:
                    return 'The element exists already'
                elif value < node.value:
                    if node.left_branch == None:
                        node.left_branch = new_node
                        return True
                    else:
                        return go_through(value, node.left_branch)
                elif value > node.value:
                    if node.right_branch == None:
                        node.right_branch = new_node
                        return True
                    else:
                        return go_through(value, node.right_branch)
            go_through(value, self.root)
    

    def find(self, value):
        """
        It finds an element

        Args:
            value ([type]): [given value]
        """
        def go_through(value, node):
            if value == node.value:
                return node.value
            elif value < node.value:
                if node.left_branch == None:
                    return 'It does not exist the node'
                else:
                    return go_through(value, node.left_branch)
            else:
                if node.right_branch == None:
                    return 'It does not exist the node'
                else:
                    return go_through(value, node.right_branch)
        found_node = go_through(value, self.root)
        return print(found_node)


    def delete(self, value):
        """
        It deletes a node through a given value

        Args:
            value ([type]): [given value]
        """
        def go_through(value, node, former_node):
            """
            It goes through all nodes
            Args:
                value ([type]): [given value]
                node ([type]): [it is the pointer]
                former_node ([type]): [it goes back]
            """
            # First case
            if value == node.value:
                if node.left_branch == None and node.right_branch == None:
                    if former_node.left_branch != None:
                        if former_node.left_branch.value == node.value:
                            former_node.left_branch = None
                    if former_node.right_branch != None:
                        if former_node.right_branch.value == node.value:
                            former_node.right_branch = None
                    node = None
                # Second case
                elif node.left_branch == None and node.right_branch != None:
                    if former_node.left_branch != None:
                        if former_node.left_branch.value == node.value:
                            former_node.left_branch = node.right_branch
                    if former_node.right_branch != None:
                        if former_node.right_branch.value == node.value:
                            former_node.right_branch = node.right_branch
                elif node.right_branch == None and node.left_branch != None:
                    if former_node.left_branch != None:
                        if former_node.left_branch.value == node.value:
                            former_node.left_branch = node.left_branch
                    if former_node.right_branch != None:
                        if former_node.right_branch.value == node.value:
                            former_node.right_branch = node.left_branch
                # Third case
                else: 
                    aux_node = None
                    former_node = node
                    node = node.right_branch

                    while node.left_branch != None:
                        aux_node = node
                        node = node.left_branch
                    former_node.value = node.value
                    if node.right_branch != None:
                        aux_node.left_branch = node.right_branch
                    else:
                        aux_node.left_branch = None
                    node = None
            elif value < node.value:
                if node.left_branch == None:
                    return 'It does not exist the node you are looking for'
                else:
                    return go_through(value, node.left_branch, node)
            else:
                if node.right_branch == None:
                    return 'It does not exist the node you are looking for'
                else:
                    return go_through(value, node.right_branch, node)
        go_through(value, self.root, self.root)


    def preorder(self):
        """
        Preorder method
        """
        container = []
        def go_through(node):
            container.append(node.value)
            if node.left_branch != None:
                go_through(node.left_branch)
            if node.right_branch != None:
                go_through(node.right_branch)
        go_through(self.root)
        return print(container)


    def inorder(self):
        """
        It gives us a middle value going vertically
        """
        container = []
        def go_through(node):
            if node.left_branch != None:
                go_through(node.left_branch)
            container.append(node.value)
            if node.right_branch != None:
                go_through(node.right_branch)
        go_through(self.root)
        return print(container)


    def postorder(self):
        """
        Postoder
        """
        container = []
        def go_through(node):
            if node.left_branch != None:
                go_through(node.left_branch)
            if node.right_branch != None:
                go_through(node.right_branch)
            container.append(node.value)
        go_through(self.root)
        return print(container)
    

    def breadth_first_search(self):
        """
        It makes a wide search
        """
        container_1 = [self.root]
        container_2 = [self.root.value]
        while len(container_1) != 0:
            node = container_1[0]
            if node.left_branch != None:
                container_1.append(node.left_branch)
                container_2.append(node.left_branch.value)
            if node.right_branch != None:
                container_1.append(node.right_branch)
                container_2.append(node.right_branch.value)
            container_1.pop(0)
        return print(container_2)




bst = BinarySearchTree()

bst.insert(500)
bst.insert(250)
bst.insert(750)
bst.insert(150)
bst.insert(350)
bst.insert(650)
bst.insert(950)
bst.insert(80)
bst.insert(280)
bst.insert(305)
bst.insert(680)
bst.insert(800)
bst.insert(990)

bst.breadth_first_search()