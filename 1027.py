from typing import List
import collections

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        f = list()
        n = len(A)
        ans = 0
        for i in range(n):
            cur = collections.Counter()
            for j in range(i):
                d = A[i] - A[j]
                cur[d] = max(cur[d], f[j][d] + 1)
                ans = max(ans, cur[d])
            f.append(cur)
        return ans + 1


solution = Solution()
print(solution.longestArithSeqLength([3,6,9,12]))
print(solution.longestArithSeqLength([9,4,7,2,10]))
print(solution.longestArithSeqLength([20,1,15,3,10,5,8]))
