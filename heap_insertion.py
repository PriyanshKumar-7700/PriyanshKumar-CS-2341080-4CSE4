class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursively(self.root, new_node)
        self.size += 1
        return self.root

    def _insert_recursively(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursively(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursively(current_node.right, new_node)
        