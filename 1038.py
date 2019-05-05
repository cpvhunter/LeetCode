class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        class BigSum:
            def __init__(self, _val):
                self.val = _val
            
            def subtract(self, _x):
                self.val -= _x

        def get_sum(node):
            if not node:
                return 0
            return get_sum(node.left) + get_sum(node.right) + node.val
        
        def modify(node, big_sum):
            if not node:
                return
            modify(node.left, big_sum)
            big_sum.subtract(node.val)
            node.val += big_sum.val
            modify(node.right, big_sum)
        
        big_sum = BigSum(get_sum(root))
        modify(root, big_sum)
        return root
