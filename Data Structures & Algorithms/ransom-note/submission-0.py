from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_map = defaultdict(int)
        for c in magazine:
            letter_map[c] += 1
        
        for c in ransomNote:
            if letter_map[c]: letter_map[c] -= 1
            else: return False

        return True