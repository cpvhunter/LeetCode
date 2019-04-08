class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        class Dummy:
            def __init__(self):
                self.ans = 0

            def update(self, x):
                self.ans += x

        def dfs(node, cur, dummy):
            cur = cur * 2 + node.val
            if not node.left and not node.right:
                dummy.update(cur)
                return
            if node.left:
                dfs(node.left, cur, dummy)
            if node.right:
                dfs(node.right, cur, dummy)

        dummy = Dummy()
        dfs(root, 0, dummy)
        return dummy.ans % 1000000007
