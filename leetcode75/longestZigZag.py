class Solution:
    def longestZigZagHelper(self, root: Optional[TreeNode], direction: int, path_length: int):
        if not root :
            return
        self.ans = max(self.ans, path_length)

        # direction left
        if direction == 0:
            # go to left subtree
            self.longestZigZagHelper(root.left, 1, 1 + path_length)

            # or go to right even if the direction is left and reset path length = 1
            self.longestZigZagHelper(root.right, 0, 1)
        else:
            # go to right subtree
            self.longestZigZagHelper(root.right, 0, 1 + path_length)

            # or go to left even if the direction is right and reset path length = 1
            self.longestZigZagHelper(root.left, 1, 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        # check longest zigzag in left and right subtree
        self.longestZigZagHelper(root, 0, 0)
        self.longestZigZagHelper(root, 1, 0)
        return self.ans