from typing import List

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        f = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            cur = i & 1
            prev = 1 - cur
            for j in range(1, n + 1):
                f[cur][j] = max(max(f[prev][j], f[cur][j - 1]), f[prev][j - 1] + (A[i - 1] == B[j - 1]))
        
        return f[m & 1][n]


solution = Solution()
print(solution.maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
print(solution.maxUncrossedLines([1,3,7,1,7,5],[1,9,2,5,1]))
