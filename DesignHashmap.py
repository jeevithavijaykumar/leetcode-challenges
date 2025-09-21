# Design a HashMap without using any built-in hash table libraries.

class Hashmap:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        for i, (k,v) in enumerate(self.map):
            if(k==key):
                self.map[i] = (key,value)
                return
        self.map.append((key,value))

    def get(self, key):
        for i, (k,v) in enumerate(self.map):
            if (k==key):
                return v
        return -1

    def remove(self, key):
        for i, (k,v) in enumerate(self.map):
            if(k==key):
                self.map.pop(i)
                return
h=Hashmap()
h.put(1,1)
h.put(2,2)
print(h.get(1))
h.remove(2)
print(h.get(2))
