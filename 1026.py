class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = -1

    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int):
            cur_min = cur_max = node.val
            if node.left:
                x1, y1 = dfs(node.left)
                self.ans = max(self.ans, max(abs(node.val - x1), abs(node.val - y1)))
                cur_min = min(cur_min, x1)
                cur_max = max(cur_max, y1)
            if node.right:
                x1, y1 = dfs(node.right)
                self.ans = max(self.ans, max(abs(node.val - x1), abs(node.val - y1)))
                cur_min = min(cur_min, x1)
                cur_max = max(cur_max, y1)
            return cur_min, cur_max

        dfs(root)
        return self.ans
