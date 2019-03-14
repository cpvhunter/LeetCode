from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ans = -1
        for i in range(1, 7):
            u, d, flag = 0, 0, True
            for j in range(len(A)):
                if A[j] != i and B[j] != i:
                    flag = False
                    break
                if A[j] == i and B[j] == i:
                    continue
                if A[j] == i:
                    d += 1
                else:
                    u += 1
            
            cur = min(u, d)
            if flag and (ans == -1 or cur < ans):
                ans = cur

        return ans


solution = Solution()
print(solution.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(solution.minDominoRotations([3,5,1,2,3],[3,5,1,2,3]))
