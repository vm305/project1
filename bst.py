class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            print self.root.data
            return
        temp = self.root
        while(temp):
            if data > temp.data and temp.right==None:
                temp.right = new_node
                return
            elif(data < temp.data and temp.left==None):
                temp.left = new_node
                return
            elif(data > temp.data):
                temp = temp.right
                #print "temp.right"
            elif(data < temp.data):
                temp = temp.left
    

    
    def print_inorder(self):
        print "*******"
        temp = self.root
        while(temp):
            print temp.data
            if(temp.left!=None):
                temp = temp.left
            if(temp.right!=None):
                temp = temp.right

if __name__ == "__main__":
    bst_node = BST()
    bst_node.insert(6)
    bst_node.insert(2)
    bst_node.print_inorder()