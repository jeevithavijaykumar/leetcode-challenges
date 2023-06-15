#572. Subtree of Another Tree
#Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

class TreeNode():
    def __init(self,data):
        self.data=data
        self.left=None
        self.right=None

class Subtree():
    def issubtree(self,root,subroot):
        if( not subroot):
            return(True)
        if not root:
            return(False)
        if self.helpertree(root,subroot):
            return(True)
        return(self.helpertree(root.left,subroot) or self.helpertree(root.right,subroot))

    def helpertree(self,r,s):
        if not r and not s:
            return(True)
        if(r and s and r.val==s.val):
            return(self.helpertree(r.left,s.left) and self.helpertree(r.right,s.right))
        return(False)

