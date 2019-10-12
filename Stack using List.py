class stackList:
    def __init__(self):
        self.data =[None] * 10


    def push(self,value):

        self.data[len(self.data)] = value
        self.length = self.length + 1


    def pop(self):
        del self.data[self.length]
        self.length = self.length-1
        return self

    def peek(self):
        return self.data[self.length-1]

    def printList(self):
        print(self.data)

myStack = stackList()
myStack.push("123")
myStack.push("12321432")
myStack.push("12321432324324324")
print(myStack.printList())