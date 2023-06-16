#124. Binary Tree Maximum Path Sum
#Given the root of a binary tree, return the maximum path sum of any non-empty path.

class TreeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinaryTreeMaxpathsum():
    def maxpathsum(self,root):
        if(not root):
            return(0)
        self.max_sum = float('-inf')

        def maxsumpathBT(node):
            if(not node):
                return(0)
            gain_on_left = max(maxsumpathBT(node.left),0)
            gain_on_right = max(maxsumpathBT(node.right),0)
            curr_path_sum = node.val + gain_on_left + gain_on_right
            self.max_sum = max(self.max_sum,curr_path_sum)
            return(node.val+ max(gain_on_left,gain_on_right))

        maxsumpathBT(root)
        return(self.max_sum)

root= TreeNode(1)
root.left = TreeNode(2)
root.right=TreeNode(-1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
b=BinaryTreeMaxpathsum()
print(b.maxpathsum(root))
