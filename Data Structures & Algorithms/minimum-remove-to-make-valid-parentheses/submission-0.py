class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        result = ""
        for c in s:
            if c == ')':
                if right + 1 <= left:
                    result += c
                    right += 1
            elif c == '(':
                left += 1
                result += c
            else:
                result += c
        diff = left - right
        if left - right > 0:
            i = len(result) - 1
            while i >= 0 and left > right:
                if result[i] == '(':
                    result = result[:i] + result[i + 1:]
                    left -= 1
                    i -= 1
                else:
                    i -= 1

        return result

