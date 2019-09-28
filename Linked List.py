class LinkedList:
    def __init__(self, value):
        self.head = {
            value:value,
            next: None
        }
        self.tail = self.head
        self.length = 1
        self.NewNode = {}

    def append(self,value):
        self.NewNode = {
            value:value,
            next:None
        }
        self.tail[next] = self.NewNode
        self.tail = self.NewNode
        self.length = self.length + 1

    def prepend(self,value):
        self.PrependNode = {
            value:value,
            next :None
        }
        self.PrependNode[next]= self.head
        self.head = self.PrependNode
        self.length = self.length +1

    def __str__(self):
        return str(self.head)


    def insert(self,index,value):
        self.NewNode ={
            value:value,
            next:None
        }




myLinkedList = LinkedList(10)
myLinkedList.append(12)
myLinkedList.append(4)
myLinkedList.append((3))
myLinkedList.prepend(14)
myLinkedList.prepend(190)
