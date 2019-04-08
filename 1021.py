class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cur, ans = "", ""
        cnt = 0
        for ch in S:
            cnt += 1 if ch == "(" else -1
            cur += ch
            if cnt == 0:
                ans += cur[1:-1]
                cur = ""

        return ans


solution = Solution()
print(solution.removeOuterParentheses("(()())(()))"))
print(solution.removeOuterParentheses("(()())(())(()(()))"))
print(solution.removeOuterParentheses("()()"))
