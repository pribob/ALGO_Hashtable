
class HashTable:
    def __init__(self):

        self.MAX = 10 #2003. 10 for testing purposes
        self.array = [[]for i in range(self.MAX)]

    def get_hash(self, key):
        hash_value = 0
        #Java hashCode function
        for index, s in enumerate(key):
            hash_value += ord(s) * 31 ** (len(key) - (index + 1))

        return hash_value % self.MAX

    def __getitem__(self, key):
        #get hash
        array_index = self.get_hash(key)
        #if hash had has collisions, look for key
        for element in self.array[array_index]:
            if element["key"] == key:
                return element

    def __setitem__(self,key,value):
        #get hash
        array_index = self.get_hash(key)
        print(array_index)
        found = False
        for index, element in enumerate(self.array[array_index]):
            # in case element exists only change the value
            if element["key"] == key:
                self.array[array_index][index] = {"key":key,"values":value}
                found = True
        if not found:
            # value doesnt exist, add it to list
            self.array[array_index].append( {"key":key,"values":value})


    def __delete__(self, key):
        array_index = self.get_hash(key)
        for index, element in enumerate(self.array[array_index]):
            if element["key"]==key:
                del self.array[array_index][index]

    # for testing purposes
    def print(self):
        for element in self.array:
            print(element)
