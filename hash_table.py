# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Ethan Weikel

class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.data = [[] for __ in range(size)]
        self.keylist =[]
        self.valuelist = []

    def __setitem__(self, key, value):
        keyvalues = self.data[self.hash(key)]
        for kv in keyvalues:
            if kv[0] is key:
                kv[1] = value
                return
        keyvalues.append([key,value])

    def __getitem__(self, key):
        for kv in self.data[self.hash(key)]:
            if kv[0] is key:
                return kv[1]
        return None

    def delete(self, key):
        self.data[self.hash(key)].clear()

    def hash(self, key):
        return hash(key) % len(self.data)

    def keys(self):
        return self.keylist

    def values(self):
        return self.valuelist
    
    def clear(self):
        self.data.clear()
        self.data = [[] for __ in range(self.size)] 


    # Was implementing a hashing function
    #     index = 0
    #     try:
    #         for i in self.split_key(key):
    #             index += ord(i)
    #         return index % (len(self.masterArray)-1)
    #     except:
    #         if key < self.size:
    #             return key
    #         elif key > self.size:
    #             while key > self.size:
    #                 key -= self.size
    #             return key
    #         else:
    #             return 0

    # def split_key(self, key):
    #     return [char for char in key]

