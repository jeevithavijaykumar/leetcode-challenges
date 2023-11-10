#572. Subtree of Another Tree
#Given the roots of two binary trees root and subRoot,
#Return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

class TreeNode():
    def __init(self,data):
        self.data=data
        self.left=None
        self.right=None

class Subtree():
    def issubtree(self,root,subroot):
        if(not subroot):
            return(True)
        elif(not root):
            return(False)
        if self.helpertree(root,subroot):
            return(True)
        return(self.issubtree(root.left,subroot) or self.issubtree(root.right,subroot))

    def helpertree(self,r,s):
        if(not r and not s):
            return(True)
        elif(not r or not s):
            return(False)
        if(r.val!=s.val):
            return(False)
        return(self.helpertree(r.left,s.left) and self.helpertree(r.right,s.right))


