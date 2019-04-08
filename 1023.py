from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = list()
        l = len(pattern)

        for query in queries:
            pos = 0
            flag = True

            for ch in query:
                if pos < l and ch == pattern[pos]:
                    pos += 1
                else:
                    if "A" <= ch <= "Z":
                        flag = False
                        break
            if pos < l:
                flag = False
            ans.append(flag)
        return ans


solution = Solution()
print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FB"))
print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBa"))
print(solution.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBaT"))
