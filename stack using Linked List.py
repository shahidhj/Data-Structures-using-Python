class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top =  None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self,value):
        currentNode = Node(value=value)
        if(self.length == 0):
            self.top = currentNode
            self.bottom = currentNode
        else:
            holdingPointer = self.top
            self.top = currentNode
            self.top.next = holdingPointer
        self.length = self.length + 1

        return self



    def pop(self):
        self.top = self.top.next
        self.length = self.length -1




    def printList(self):
        currentNode = self.top
        while currentNode!= None:
            print(currentNode.value)
            currentNode = currentNode.next

myStack = Stack()
myStack.pushed(10)
myStack.pushed(123)
myStack.pushed(12312313)
myStack.pop()
myStack.pushed(123123131231)
myStack.printList()



