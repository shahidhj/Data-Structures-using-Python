class Arrays:
    def __init__(self):
        self.data = {}
        self.length = 0

    def get(self,index):
        return self.data[index]

    def append(self,item):
        self.data[self.length] = item
        self.length = self.length + 1

    def pop(self):
        del self.data[self.length-1]
        self.length = self.length-1

    def insert(self,index,value):
        self.length = self.length + 1
        for i in range(len(self.data)-1,index,-1):
            self.data[i+1] = self.data[i]
            self.data[i] = self.data[i-1]
        self.data[index] = value





myArray = Arrays()
myArray.append("shahid")
myArray.append("2345")
myArray.append("1233242")
myArray.append("213234")
myArray.append("8765435")
myArray.append("slim")
print(myArray.data)
print(myArray.insert(2,"abc"))
print(myArray.data)