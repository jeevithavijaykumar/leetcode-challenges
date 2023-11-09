class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Inorder(self):
        if (self.left):
            self.left.Inorder()
        if (self.data):
            print(self.data)
        if (self.right):
            self.right.Inorder()

    def Preorder(self):
        if (self.data):
            print(self.data)
        if (self.left):
            self.left.Preorder()
        if (self.right):
            self.right.Preorder()

    def Postorder(self):
        if (self.left):
            self.left.Postorder()
        if (self.right):
            self.right.Postorder()
        if (self.data):
            print(self.data)

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')
print('==========Printing Tree Traversals ============')
root.Inorder()
print('=========preorder=============')
root.Preorder()
print('===========postorder''===========')
root.Postorder()

