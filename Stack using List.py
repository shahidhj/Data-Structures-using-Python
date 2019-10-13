class stackList:
    def __init__(self):
        self.data =[]


    def push(self,value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def printList(self):
        print(self.data)

myStack = stackList()
myStack.push("123")
myStack.push("12321432")
myStack.pop()
myStack.push("12321432324324324")
a =myStack.peek()
print(myStack.printList())
print(a)