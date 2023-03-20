
class HashTable:
    def __init__(self):

        self.MAX = 10 #2003. 10 for testing purposes
        self.array = [None for i in range(self.MAX)]

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
        probing_offset = 0
        found = False
        while not found:
            new_index = (array_index+(probing_offset**2))%self.MAX
            if self.array[new_index]["key"] == key:
                found = True
                return self.array[new_index]
            elif self.array[new_index] is None:
                return None
            else:
                probing_offset += 1


    def __setitem__(self,key,value):
        #get hash
        array_index = self.get_hash(key)
        probing_index = 1
        stop_probing = False
        # spot is empty
        if self.array[array_index]==None or self.array[array_index]["key"] == "Sentinel":
            self.array[array_index] = {"key":key,"values":value}
        # key is same, only change data
        elif self.array[array_index]["key"]==key:
            self.array[array_index]["values"]=value
        else:
        #quadratic probing
            while not stop_probing:
                new_index = (array_index+(probing_index**2))%self.MAX
                # empty spot found
                if self.array[new_index]==None or self.array[new_index]["key"]=="Sentinel":
                    stop_probing = True
                    self.array[new_index] = {"key":key,"values":value}
                else:
                    probing_index += 1


    def __delete__(self, key):
        array_index = self.get_hash(key)
        probing_offset = 0
        found = False
        while not found:
            new_index = (array_index + (probing_offset ** 2)) % self.MAX
            if self.array[new_index]["key"] == key:
                found = True
                #del self.array[new_index]
                self.array[new_index]["key"] = "Sentinel"
                del self.array[new_index]["values"]
            elif self.array[new_index] is None:
                print("Element does not exist.")
                return None
            else:
                probing_offset += 1


    # for testing purposes
    def print(self):
        for element in self.array:
            print(element)
