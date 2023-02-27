from node import Node


class BinaryTree:
    def __init__(self):
        self.root = None
    #This function takes an inputed number called Newnumber and goes down the binaryTree by using rules where if the Newnumber is > or < to the
    # CurrentParent being looked at. It keeps moving the node down left or right untill it reaches a spot where there is no already existing child.
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
        self.inorderTraversal(self.root)
        return ''
#Have a fucntion Called inorderTraversal that uses recursion to run through a BinaryTree and make a list of number orderd from smallest to biggest.
    def inorderTraversal(self,CurrentNode):
        if CurrentNode.leftChild != None:
            #check if the current node we are looking at has a left child
            self.inorderTraversal(CurrentNode.leftChild)
            #if it does then it goes throught the function again and now uses the CurrentNodes left child as the input.
        print(CurrentNode, end=" ")
        #this is the basecase
        if CurrentNode.rightChild != None:
            # check if the current node we are looking at has a right child
            self.inorderTraversal(CurrentNode.rightChild)
            # if it does then it goes throught the function again and now uses the CurrentNodes right child as the input.

        # inorder traversal


bt1 = BinaryTree()
#print(bt1.root)
bt1.insert(10)
#print(bt1.root)
bt1.insert(8)
bt1.insert(9)
bt1.insert(2)
bt1.insert(80)
bt1.insert(200)
bt1.insert(70)
#print(bt1.root.rightChild.rightChild)
print(bt1)
#print(bt1.root.leftChild.leftChild)
