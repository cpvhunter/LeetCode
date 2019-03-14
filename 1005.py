from typing import List

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        pos = sorted(filter(lambda x: x >= 0, A))
        neg = sorted(filter(lambda x: x < 0, A))
        for i in range(len(neg)):
            neg[i] = -neg[i]
            K -= 1
            if K == 0:
                break
        
        if K > 0 and K % 2 == 1:
            if not pos:
                neg[-1] = -neg[-1]
            elif not neg:
                pos[0] = -pos[0]
            else:
                if neg[-1] < pos[0]:
                    neg[-1] = -neg[-1]
                else:
                    pos[0] = -pos[0]

        return sum(pos) + sum(neg)


solution = Solution()
print(solution.largestSumAfterKNegations([4,2,3],1))
print(solution.largestSumAfterKNegations([3,-1,0,2],3))
print(solution.largestSumAfterKNegations([2,-3,-1,5,-4],2))
