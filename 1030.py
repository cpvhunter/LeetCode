from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def upd(a, x, y):
            if 0 <= x < R and 0 <= y < C:
                a.append([x, y])
                return True
            return False

        ans = [[r0, c0]]
        for dis in range(1, 200):
            find = upd(ans, r0 - dis, c0) | upd(ans, r0 + dis, c0) | upd(ans, r0, c0 - dis) | upd(ans, r0, c0 + dis)
            for i in range(1, dis):
                j = dis - i
                find |= upd(ans, r0 - i, c0 - j) | upd(ans, r0 - i, c0 + j) | upd(ans, r0 + i, c0 - j) | upd(ans, r0 + i, c0 + j)
            if not find:
                break

        return ans


solution = Solution()
print(solution.allCellsDistOrder(1,2,0,0))
print(solution.allCellsDistOrder(2,2,0,1))
print(solution.allCellsDistOrder(2,3,1,2))
