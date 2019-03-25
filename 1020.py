from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s, n = sum(A), len(A)
        if s % 3 != 0:
            return False
        s //= 3

        p, sump, q, sumq = -1, 0, -1, 0
        for i in range(n):
            sump += A[i]
            if sump == s:
                p = i
                break

        for i in range(n):
            sumq += A[n - 1 - i]
            if sumq == s:
                q = n - 1 - i
                break

        return -1 < p < q


solution = Solution()
print(solution.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(solution.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(solution.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
