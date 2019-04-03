from typing import List

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cur = 0
        ans = list()
        
        for num in A:
            cur = (cur * 2 + num) % 5
            ans.append(True if cur == 0 else False)
        
        return ans


solution = Solution()
print(solution.prefixesDivBy5([0,1,1]))
print(solution.prefixesDivBy5([1,1,1]))
print(solution.prefixesDivBy5([0,1,1,1,1,1]))
print(solution.prefixesDivBy5([1,1,1,0,1]))
