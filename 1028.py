import re

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pattern = list()
        self.pattern_pos = 1

    def recoverFromPreorder(self, S: str) -> TreeNode:
        def dfs(node, depth):
            # left
            if self.pattern_pos >= len(self.pattern):
                return
            pattern = self.pattern[self.pattern_pos]
            if pattern[1] == depth + 1:
                node.left = TreeNode(pattern[0])
                self.pattern_pos += 1
                dfs(node.left, depth + 1)
            else:
                return
            # right
            if self.pattern_pos >= len(self.pattern):
                return
            pattern = self.pattern[self.pattern_pos]
            if pattern[1] == depth + 1:
                node.right = TreeNode(pattern[0])
                self.pattern_pos += 1
                dfs(node.right, depth + 1)

        p = [int(x) for x in re.findall(r"\d+", S)]
        q = [len(x) for x in re.findall(r"-+", S)]
        self.pattern.append((p[0], 0))
        for p0, q0 in zip(p[1:], q):
            self.pattern.append((p0, q0))

        root = TreeNode(p[0])
        dfs(root, 0)
        return root


solution = Solution()
print(solution.recoverFromPreorder("1-2--3--4-5--6--7"))
print(solution.recoverFromPreorder("1-2--3---4-5--6---7"))
print(solution.recoverFromPreorder("1-401--349---90--88"))