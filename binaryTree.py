from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, Newnumber):
        if self.root == None:
            self.root = Node(Newnumber, None)
        # if self.root.number > Newnumber:
        #     self.root.leftChild = Node(Newnumber, self.root)
        # if self.root.number < Newnumber:
        #     self.root.rightChild = Node(Newnumber, self.root)
        CurrentParent = self.root
        #add a while loop for CurrentParent
        if CurrentParent.number > Newnumber:
            if CurrentParent.leftChild != None:
                CurrentParent = CurrentParent.leftChild
            else:
                CurrentParent.leftChild = Node(Newnumber, CurrentParent)
        if CurrentParent.number < Newnumber:
            if CurrentParent.leftChild != None:
                CurrentParent = CurrentParent.rightChild
            else:
                CurrentParent.rightChild = Node(Newnumber, CurrentParent)

    def __str__(self):
        pass
        # inorder traversal


bt1 = BinaryTree()
print(bt1.root)
bt1.insert(10)
print(bt1.root)
