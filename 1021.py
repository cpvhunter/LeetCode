from typing import List

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        n = len(A)
        cur = A[n - 1] - (n - 1)
        ans = 0
        for i in range(n - 2, -1, -1):
            ans = max(ans, cur + A[i] + i)
            cur = max(cur, A[i] - i)
        return ans


solution = Solution()
print(solution.maxScoreSightseeingPair([8,1,5,2,6]))
