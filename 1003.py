class Solution:
    def isValid(self, S: str) -> bool:
        stk = list()
        for ch in S:
            stk.append(ch)
            if len(stk) >= 3 and "".join(stk[-3:]) == "abc":
                stk.pop()
                stk.pop()
                stk.pop()
        
        return not stk


solution = Solution()
print(solution.isValid("aabcbc"))
print(solution.isValid("abcabcababcc"))
print(solution.isValid("abccba"))
print(solution.isValid("cababc"))
