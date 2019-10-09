class Node:

    def __init__(self,value,previous=None,next=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList:

    def __init__(self,value,next=None,previous=None):
        self.head = Node(value=value)
        self.tail = self.head
        self.length = 1

    def append(self,value):
        self.CurrentNode = Node(value=value)
        self.tail.next = self.CurrentNode
        self.CurrentNode.previous = self.tail
        self.tail = self.CurrentNode
        self.length = self.length + 1

    def prepend(self,value):
        self.CurrentNode = Node(value=value)
        self.CurrentNode.next = self.head
        self.head.previous = self.CurrentNode
        self.head = self.CurrentNode
        self.length = self.length + 1

    def insert(self,index,value):
        self.CurrentNode = Node(value=value)
        leader = self.traverseToIndex(index - 1)
        headingPointer = leader.next
        leader.next = self.CurrentNode
        self.CurrentNode.previous = leader
        self.CurrentNode.next = headingPointer
        headingPointer.previous = self.CurrentNode


    def traverseToIndex(self,index):
        CurrentNode = self.head
        counter =0
        while(counter != index):
            CurrentNode = CurrentNode.next
            counter = counter + 1
        return CurrentNode

    def printList(self):
        currentNode = self.head
        while(currentNode != None):
            print("Current node value",currentNode.value)
            print("Current node next",currentNode.next)
            print("previous",currentNode.previous)
            currentNode = currentNode.next


myLinkedList = DoublyLinkedList(10)
myLinkedList.append(15)
myLinkedList.append(20)
myLinkedList.prepend(100)
myLinkedList.insert(1,300)
myLinkedList.printList()