from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        p = list()
        cur, mx = sum(A[:L]), sum(A[:L])
        p.append((cur, mx))
        for i in range(1, n - L + 1):
            cur += A[i + L - 1] - A[i - 1]
            mx = max(mx, cur)
            p.append((cur, mx))

        q = list()
        cur, mx = sum(A[:M]), sum(A[:M])
        q.append((cur, mx))
        for i in range(1, n - M + 1):
            cur += A[i + M - 1] - A[i - 1]
            mx = max(mx, cur)
            q.append((cur, mx))

        ans = 0
        for i in range(L, n - M + 1):
            ans = max(ans, p[i - L][1] + q[i][0])
        for i in range(M, n - L + 1):
            ans = max(ans, p[i][0] + q[i - M][1])

        return ans


solution = Solution()
print(solution.maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4],1,2))
print(solution.maxSumTwoNoOverlap([3,8,1,3,2,1,8,9,0],3,2))
print(solution.maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))
