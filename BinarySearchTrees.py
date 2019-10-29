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

    def lookup(self,value):
        if self.root is  None:
            return False
        else:
            currentNode = self.root
            while currentNode is not None:
                if value < currentNode.value:
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    currentNode = currentNode.right
                elif value == currentNode.value :
                    return currentNode
        return False
    """
    def remove(self,value): i will start this today0
        if self.root is None:
            return False
        else:
            currentNode = self.root
            previousNode = None
            while currentNode is not None:
                if value < currentNode.value:
                    previousNode = currentNode
                    currentNode = currentNode.left
                elif value > currentNode.value:
                    previousNode = currentNode
                    currentNode = currentNode.right
                elif value == currentNode.value :
                     if(currentNode.right):
                         currentNode = currentNode.right
                         if currentNode.left:
                             currentNode = currentNode.left
                             previousNode.right = currentNode
                         else:
                             previousNode.right = currentNode
                     else:
                         currentNode = currentNode.left
                         previousNode
                         
        Too complicated:( WILL COMPLETE IT"""




