class BinaryTreeNode():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchildnode(self,data):
        if(self.data==data):
            return
        if(self.data<data):
            if(self.left):
                self.left.addchildnode(data)
            else:
                self.left=BinaryTreeNode(data)
        else:
            if(self.right):
                self.right.addchildnode(data)
            else:
                self.right = BinaryTreeNode(data)

    def PrintTree(self):
        if(self.left):
            self.left.PrintTree()
        print(self.data)
        if(self.right):
            self.right.PrintTree()

root = BinaryTreeNode(10)
root.addchildnode(5)
root.addchildnode(15)
root.addchildnode(3)
root.addchildnode(7)
root.addchildnode(6)
root.addchildnode(8)
root.addchildnode(13)
root.addchildnode(18)
root.addchildnode(17)
root.addchildnode(20)
root.PrintTree()




