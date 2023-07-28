# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkMirrorImage(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        " utility to check if the left child value = right child of root1 and vice versa"

        flag = False
        if root1  and root2:
            if root1.val == root2.val:
                flag = True
            else:
                return False
        
        elif not root1 and not root2:
            return True
        
        else:
            return False

        return flag and self.checkMirrorImage(root1.left, root2.right) and self.checkMirrorImage(root1.right, root2.left)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root == None:
            return True
        # check if the left subtree and right subtree are mirror images of each other
        return self.checkMirrorImage(root.left, root.right)