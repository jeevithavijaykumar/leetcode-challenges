#1720. Decode XORed Array

class DecodeXORedArray():
    def DecodeXORed(self,encoded,first):
        arr = [first]
        for i in range(0, len(encoded)):
            next = encoded[i] ^ arr[i]
            arr.append(next)
        return (arr)


d = DecodeXORedArray()
encode=[1,2,3]
print(d.DecodeXORed(encode,1))


