# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # break condition
        if root == None:
            return []
        # recursive preorder traversal i.e. root --> left subtree --> right subtree
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # break condition
        if root == None:
            return []
        
        # iterative, use stack
        res = []
        stack = [root]
        while len(stack):
            curr = stack[-1]
            res.append(curr.val)
            stack.pop()

            # check for right first so that right stays below left in the stack
            if curr.right:
                stack.append(curr.right)
            
            # check for left child after right so that left stays above right in the stack
            if curr.left:
                stack.append(curr.left)
        return res

        
