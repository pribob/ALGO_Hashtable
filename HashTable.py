# key-value: key is the name/shortsign/Wertpapiernumme of the stock
# every array-index stores one key-value-tuple
# value is an object in this case; DICTIONARY???
# TO-DO: decide which is the key and how to store the course information
# while value is the other two + filename for csv of the last 30 days of the course ???

class HashTable:
    def __init__(self):
        self.MAX = 1217
        self.array = [[]for i in range(self.MAX)]

    def get_hash(self, key):
        hash_value = 0
        # Copy of Java hashCode function
        for index, s in enumerate(key):
            hash_value += ord(s) * 31 ** (len(key) - (index + 1))
        # 1000 stocks at max.
        # 1217 is a primenumber greater than max amount of stocks.
        return hash_value % self.MAX

    def __getitem__(self,key):
        array_index = get_hash(self,key)
        for element in self.array[array_index]:
            if element[0] == key:
                return element[1]

    def __setitem__(self,key,value):
        array_index = self.get_hash(key)
        found = False
        for index, element in enumerate(self.array[array_index]):
            # in case element exists <=> value is equal
            # change value
            if len(element)==2 and element[0]==key:
                self.array[array_index][index] = (key,value)
                found = True
        if not found:
            self.array[array_index].append((key,value))

    def __delete__(self, key):
        array_index = self.get_hash(self,key)
        for index, element in enumerate(self.array[array_index]):
            if element[0]==key:
                del self.array[array_index][index]