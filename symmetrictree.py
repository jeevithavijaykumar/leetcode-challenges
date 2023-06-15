#101. Symmetric Tree
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class Binarytree():
    def symmetrictree(self,root):
        if(not root):
            return(True)
        return(self.helperfn(root.left,root.right))

    def helperfn(self,r,s):
        if(not r and not s):
            return(True)
        if(r and s and r.val==s.val):
            return(self.helperfn(r.left,s.right) and self.helperfn(r.right,s.left))
        return(False)
