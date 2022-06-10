class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(self): #root -> left -> right 
        print(self.val)
        if self.left:
            self.left.traverse()

        if self.right:
            self.right.traverse()




def main():
    v1 = TreeNode(3) 
    v2 = TreeNode(9)
    v3 = TreeNode(20)
    v4 = TreeNode(15)
    v5 = TreeNode(7)
    
    v1.left = v2
    v1.right = v3
    v3.left = v4
    v3.right = v5
    
    v1.traverse()



if __name__ == '__main__':
    main()
