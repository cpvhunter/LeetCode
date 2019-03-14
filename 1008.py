from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        class Idx:
            def __init__(self, root_val):
                self.x = 1
                self.q = [root_val]

            def get(self):
                return self.x

            def add(self, val):
                self.x += 1
                while self.q and self.q[-1] < val:
                    self.q.pop()
                self.q.append(val)

            def fit(self, val):
                if self.q:
                    if len(self.q) == 1 and val > self.q[-1]:
                        return True
                    elif self.q[-2] > val > self.q[-1]:
                        return True
                return False
            
            def clear(self, val):
                self.q.pop()

        def build(pa_node, node, idx, length):
            ii = idx.get()
            if ii >= length:
                return
            if preorder[ii] < node.val:
                node.left = TreeNode(preorder[ii])
                idx.add(preorder[ii])
                build(node, node.left, idx, length)
            
            ii = idx.get()
            if ii >= length:
                return
            if idx.fit(preorder[ii]):
                node.right = TreeNode(preorder[ii])
                idx.add(preorder[ii])
                build(node, node.right, idx, length)
            else:
                idx.clear(node.val)

        root = TreeNode(preorder[0])
        build(None, root, Idx(preorder[0]), len(preorder))
        return root


solution = Solution()
solution.bstFromPreorder([8,5,1,7,10,12])
