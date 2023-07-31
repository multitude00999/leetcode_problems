# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSumHelper(self, root: Optional[TreeNode], targetSum: int, path: List[int], ans: List[List[int]]):

        # base case
        if root == None:
            return []

        # check if leaf node
        if not root.left and not root.right:

            # check if the sum of path is target sum
            if targetSum - root.val == 0:
                temp = path.copy() + [root.val]
                ans.append(temp)
            return


        # got to left and right subtree with updated path and sum
        self.pathSumHelper(root.left, targetSum - root.val, path + [root.val], ans) 
        self.pathSumHelper(root.right, targetSum - root.val, path + [root.val], ans)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        self.pathSumHelper(root, targetSum, [], ans)
        return ans
        