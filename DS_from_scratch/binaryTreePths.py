class Solution:
    def binaryTreePathsHelper(self, root: Optional[TreeNode], path: List[int], ans: List[str]):
        if root == None:
            return
        
        if not root.left and not root.right:
            temp = path.copy() + [str(root.val)]
            ans.append("->".join(temp))

        self.binaryTreePathsHelper(root.left, path + [str(root.val)], ans)
        self.binaryTreePathsHelper(root.right, path + [str(root.val)], ans)
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        ans = []
        self.binaryTreePathsHelper(root, path, ans)
        return ans