from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def judge(mid):
            cnt, cur = 1, 0
            for w in weights:
                cur += w
                if cur > mid:
                    cnt += 1
                    cur = w
                    
            return cnt <= D

        l, r, ans = max(weights), sum(weights), 0
        while l <= r:
            mid = (l + r) // 2
            if judge(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        
        return ans

    
solution = Solution()
print(solution.shipWithinDays([3,2,2,4,1,4],3))
print(solution.shipWithinDays([1,2,3,1,1],4))
