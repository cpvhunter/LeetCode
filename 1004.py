from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        r, n = 0, len(A)
        zeros = 0
        for i in range(n):
            if A[i] == 0:
                zeros += 1
                if zeros > K:
                    r = i - 1
                    break
        
        if zeros <= K:
            return n

        zeros -= 1
        ans = r + 1
        for i in range(1, n):
            if A[i - 1] == 0:
                zeros -= 1
            while r + 1 < n and zeros + (A[r + 1] == 0) <= K:
                r += 1
                zeros += (A[r] == 0)
            ans = max(ans, r - i + 1)
        
        return ans
    

solution = Solution()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
