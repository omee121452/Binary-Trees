class Node:
    def __init__(self,number,parent):
        self.number = number
        self.parent = parent
        self.leftChild = None
        self.rightChild = None
    def __str__(self):
        return str(self.number)

node1 = Node(10,None)
leftNode1 = Node(5,node1)
node1.leftChild = leftNode1
print(node1)