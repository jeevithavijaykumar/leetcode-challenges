class Palindromenumber():
    def palindrome(self,x):
        res = 0
        num = x
        if (x < 0):
            return (False)
        while (x > 0):
            res = res * 10 + x % 10
            x = x // 10
        return (res == num)

p = Palindromenumber()
print(p.palindrome())
