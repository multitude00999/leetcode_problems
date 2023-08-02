class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return root

        # check if value found
        if root.val == val:
            return root
        
        # if root is smaller go to right subtree
        elif root.val < val:
            return self.searchBST(root.right, val)
        
        # else go to left subtree
        else:
            return self.searchBST(root.left, val)