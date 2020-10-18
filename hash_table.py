# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Ethan Weikel


class HashTable:

    def __init__(self, size = 10):
        self.size = size
        self.space_used = 0
        self.masterArray = [None for __ in range(size)]

    def __setitem__(self, key, value):
        self.space_used = self.space_used + 1
        index = self.hash_func(key)
        print(index)
        self.masterArray.insert(index, value)

    def __getitem__(self, key):
        index = self.hash_func(key)
        print(index)
        return self.masterArray[index]

    def hash_func(self, key):
        index = 0
        for i in self.split_key(key):
           index = index + ord(i)
        return index % len(self.masterArray)

    def split_key(self, key):
        return [char for char in key]
    
    pass
