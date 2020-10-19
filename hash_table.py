# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Ethan Weikel

class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.data = [[] for __ in range(size)] 

    def __setitem__(self, key, value):
        self.data[self.hash(key)].append([key, value])

    def __getitem__(self, key):
        for kv in self.data[self.hash(key)]:
            if kv[0] is key:
                return kv[1]
        return None

    def hash(self, key):
        return hash(key) % len(self.data)
    


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

