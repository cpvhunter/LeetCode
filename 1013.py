from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        a = [0] * 60
        for t in time:
            a[t % 60] += 1
        
        ans = a[0] * (a[0] - 1) // 2 + a[30] * (a[30] - 1) // 2
        for i in range(1, 30):
            ans += a[i] * a[60 - i]
        
        return ans


solution = Solution()
print(solution.numPairsDivisibleBy60([30,20,150,100,40]))
