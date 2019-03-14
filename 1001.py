from typing import List

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        dict_1, dict_2, dict_3, dict_4 = dict(), dict(), dict(), dict()
        pos = set()
        for x, y in lamps:
            dict_1[x] = dict_1.get(x, 0) + 1
            dict_2[y] = dict_2.get(y, 0) + 1
            dict_3[x + y] = dict_3.get(x + y, 0) + 1
            dict_4[x - y] = dict_4.get(x - y, 0) + 1
            pos.add((x, y))

        ans = list()
        for x, y in queries:
            if dict_1.get(x, 0) > 0 or dict_2.get(y, 0) > 0 or dict_3.get(x + y, 0) > 0 or dict_4.get(x - y, 0) > 0:
                ans.append(1)
            else:
                ans.append(0)
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in pos:
                        pos.remove((nx, ny))
                        dict_1[nx] -= 1
                        dict_2[ny] -= 1
                        dict_3[nx + ny] -= 1
                        dict_4[nx - ny] -= 1

        return ans


solution = Solution()
print(solution.gridIllumination(5,[[0,0],[4,4]],[[1,1],[1,0]]))
