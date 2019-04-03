from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        class SmpStack:
            def __init__(self):
                self.l = list()
                self.ans = list()
                
            def update(self, x):
                while self.l and self.l[-1] <= x:
                    self.l.pop()
                self.ans.append(self.l[-1] if self.l else 0)
                self.l.append(x)
                
        def dfs(cur, smp_stack):
            if cur.next:
                dfs(cur.next, smp_stack)
            smp_stack.update(cur.val)
        
        smpStack = SmpStack()
        dfs(head, smpStack)
        return list(reversed(smpStack.ans))
