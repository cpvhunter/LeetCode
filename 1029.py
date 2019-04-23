from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = 0
        for cost in costs:
            ans += cost[0]

        transfer = sorted([cost[1] - cost[0] for cost in costs])
        ans += sum(transfer[:len(transfer) // 2])
        return ans


solution = Solution()
print(solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
