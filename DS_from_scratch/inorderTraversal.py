class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        # recursive solution i.e left subtree --> root --> right subtree
        return self.inorderTraversal(root.left) +  [root.val] + self.inorderTraversal(root.right)

class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if root == None:
            return []
        
        # iterative approach
        res = []
        stack = []
        curr = root
        while curr!= None or len(stack):

            # keep going to left subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res