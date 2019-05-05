from typing import List

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        f = [[0] * n for _ in range(n)]
        for span in range(3, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                f[i][j] = 10**9
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + A[i] * A[k] * A[j])

        return f[0][n - 1]


solution = Solution()
print(solution.minScoreTriangulation([1,2,3]))
print(solution.minScoreTriangulation([3,7,4,5]))
print(solution.minScoreTriangulation([1,3,1,4,1,5]))
