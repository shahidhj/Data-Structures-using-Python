class HashTable:

    def __init__(self):
        self.map = []

    def _get_hash(self,key):
        hash = 0
        for char in key:
            hash = hash + ord(key)
        return hash % len(self.map)

    def add(self,key,value):
        hash_address = self._get_hash(key)
        key_value = [key,value]
        if self.map[hash_address] is not None:
            key_value = list([key,value])
            self.map[hash_address] = key_value
            return True
        else:
            for pairs in self.map[hash_address]:
                if pairs[0] == key:
                    pairs[1] = value
                    return True
            self.map[hash_address].append(key_value)
            return True

    def get(self,key):
        hash_address = self._get_hash(key)
        if self.map[hash_address] is not None:
            for pairs in self.map[hash_address]:
                if pairs[0] == key:
                    return pairs[1]
        return None

    def delete(self,key):
        hash_address = self._get_hash(key)
        if self.map[hash_address] is not None:
            for i in range(0,len(self.map[hash_address])):
                if self.map[hash_address][i][0] == key:
                    self.map[hash_address].pop(i)
                    return True






