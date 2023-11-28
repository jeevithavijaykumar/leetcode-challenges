#13. Roman to Integer
#Given a roman numeral, convert it to an integer.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
class String():
    def romantointeger(self,s):
        rti = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(0, len(s)):
            if (i + 1 < len(s) and rti[s[i]] < rti[s[i + 1]]):
                res = res - rti[s[i]]
            else:
                res = res + rti[s[i]]
        return (res)

s=String()
print(s.romantointeger('MCMXCIV'))
