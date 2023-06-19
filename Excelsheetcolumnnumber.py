#171. Excel Sheet Column Number
#Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

class Excelsheetcolumn():
    def columnnumber(self,columnTitle):
        list1= list(columnTitle)
        res = 0
        for i in list1:
            res = res*26 + (ord(i)-ord('A')+1)
        return (res)

e = Excelsheetcolumn()
print(e.columnnumber('AB'))


#Aproach 2

class Excelsheetcolumn():
    def columnnumber(self,columnTitle):
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
             'N': 14,
             'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': '23', 'X': 24, 'Y': 25,
             'Z': 26}

        res = 0

        for i in columnTitle:
            res = res * 26 + int(d[i])
        return (res)
e = Excelsheetcolumn()
print(e.columnnumber('AB'))


