from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, Newnumber):
        NodeCreated = False
        if self.root == None:
            self.root = Node(Newnumber, None)
            NodeCreated = True
        # if self.root.number > Newnumber:
        #     self.root.leftChild = Node(Newnumber, self.root)
        # if self.root.number < Newnumber:
        #     self.root.rightChild = Node(Newnumber, self.root)
        CurrentParent = self.root
        # add a while loop for CurrentParent
        while NodeCreated != True:
            if Newnumber < CurrentParent.number:
                if CurrentParent.leftChild != None:
                    CurrentParent = CurrentParent.leftChild
                else:
                    CurrentParent.leftChild = Node(Newnumber, CurrentParent)
                    NodeCreated = True
            elif Newnumber > CurrentParent.number:
                if CurrentParent.rightChild != None:
                    CurrentParent = CurrentParent.rightChild
                else:
                    CurrentParent.rightChild = Node(Newnumber, CurrentParent)
                    NodeCreated = True

    def __str__(self):
        return self.inorderTraversal(self.root)
    def inorderTraversal(self,CurrentNode):
        self.inorderTraversal(CurrentNode.leftchild)

        # inorder traversal


bt1 = BinaryTree()
print(bt1.root)
bt1.insert(10)
print(bt1.root)
bt1.insert(8)
bt1.insert(2)
bt1.insert(80)
bt1.insert(200)
print(bt1.root.rightChild.rightChild)
#print(bt1.root.leftChild.leftChild)
