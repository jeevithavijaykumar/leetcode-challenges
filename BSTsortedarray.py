#108. Convert Sorted Array to Binary Search Tree
#Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.

class TreeNode():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST():
    def BSTsortedarray(self,nums):

        def helper(l,r):
            if(l>r):
                return(None)
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=helper(l,mid-1)
            root.right=helper(mid+1,r)
            return(root)
        return(helper(0,len(nums)-1))

b=BST()
print(b.BSTsortedarray([-10,-3,0,5,9]))

