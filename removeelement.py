class Removeelement():
    def removeele(self,nums,val):
        l = 0
        r = len(nums) - 1
        while (l <= r):
            if (nums[l] == val):
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r = r - 1
            else:
                l = l + 1
        return (l)

r = Removeelement()
num = [1,4,2,2,3,7,6]
val = 3
print(r.removeele(num,val))


