##Given a string s, find the length of the longest substring without repeating characters.

class Longestsubstring():
    def substring(self,s):
        if (s == ""):
            return 0

        dic = {}
        start_index = 0
        length = 0
        sl = list(s)

        for i in range(0, len(sl)):
            if (sl[i] in dic):
                if (dic[sl[i]] < start_index):
                    dic[sl[i]] = i
                else:
                    start_index = dic[sl[i]] + 1
                    dic[sl[i]] = i
                l = i - start_index + 1
            else:
                dic[sl[i]] = i
                l = i - start_index + 1
            length = max(length, l)
        return (length)

l=Longestsubstring()
print(l.substring('pwwkew'))
