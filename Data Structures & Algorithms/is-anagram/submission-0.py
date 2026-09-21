class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # parse string s and put the char and the number of char into a dict
        d = {}
        for i in range(len(s)):
            d[s[i:i+1]] = d.get(s[i:i+1], 0) + 1

        for j in range(len(t)):
            if d.get(t[j:j+1], 0) == 0: return False
            d[t[j:j+1]] = d[t[j:j+1]] - 1

        for x, y in d.items():
            if y > 0:
                return False
        
        return True

