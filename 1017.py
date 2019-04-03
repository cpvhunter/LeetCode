class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        
        ans = ""
        while N != 0:
            ans = str(N % 2) + ans
            N = -(N // 2) if N > 0 else (-N + 1) // 2
        return ans


solution = Solution()
print(solution.baseNeg2(2))
print(solution.baseNeg2(3))
print(solution.baseNeg2(4))
