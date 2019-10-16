class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value=value)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while (True):
                if value > currentNode.value:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right
                else:
                    if currentNode.left is None:
                        currentNode.left = currentNode
                        return self
                    currentNode = currentNode.left
