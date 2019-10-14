class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self,value):
        cuurentNode = Node(value=value)
        if(self.length == 0):
            self.last = cuurentNode
            self.first = cuurentNode
        else:
            self.last.next = cuurentNode
            self.last = cuurentNode
        self.length = self.length + 1

    def dequeue(self):
        self.first = self.first .next
        self.length = self.length -1

    def printList(self):
        currentNode = self.first
        while(currentNode != None):
            print(currentNode.value)
            currentNode = currentNode.next

myQueue = Queue()
myQueue.enqueue(10)
myQueue.enqueue(123)
myQueue.enqueue(12312313)
myQueue.enqueue(123123131231)
myQueue.printList()
myQueue.dequeue()
myQueue.printList()




