# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        # recursive solution i.e left subtree --> root --> right subtree
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        # iterative, use stack
        res = []
        stack = [root]
        while len(stack):
            curr = stack[-1]
            res.append(curr.val)
            stack.pop()

            # check for left first so that right stays below left in the stack
            if curr.left:
                stack.append(curr.left)
            
            # check for right child after right so that left stays above right in the stack
            if curr.right:
                stack.append(curr.right)
        # reverse to get the post order traversal
        return res[::-1]