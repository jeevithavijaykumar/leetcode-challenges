#556. Next Greater Element III
#Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n.
# If no such positive integer exists, return -1

import bisect
from bisect import bisect_right


class Solution():
    def nextgreaterelement(self,n):
        digits = list(map(int, str(n)))
        stack = []
        for i in range(len(digits) - 1, -1, -1):
            if not stack or digits[stack[-1]] <= digits[i]:
                stack.append(i)
                continue

            swapIndex = stack[bisect_right(stack, digits[i], key=lambda x:digits[x])]

            digits[i], digits[swapIndex] = digits[swapIndex], digits[i]
            digits[i + 1:] = sorted(digits[i + 1:])
            break

        res = int(''.join(str(e) for e in digits))
        return res if len(stack) < len(digits) and res < 2 ** 31 else -1

s=Solution()
print(s.nextgreaterelement(12))