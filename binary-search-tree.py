class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def addChild(self, key):
        if key == self.key:
            return
        elif key < self.key:
            if self.left:
                self.left.addChild(key)
            else:
                self,left = BinaryTreeNode(key)
        else:
            if self.right:
                self.right.addChild(key)
            else:
                self.right = BinaryTreeNode(key)
    
    def inorderTraversal(self):
        inorderList = []
        if self.left:
            inorderList = inorderList + self.left.inorderList()
        
        inorderList.appen(self.key)

        if self.right:
            inorderList += self.right.inorderTraversal()

        return inorderList
    
    def preorderTraversal(self):
       preorderList = []
       preorderList.append(self.key) 

       if self.left:
           preorderList += self.left.preorderTraversal()

       if self.right:
           preorderList += self.right.preorderTraversal()
           return preorderList

    


    
