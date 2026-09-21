from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        letters = defaultdict(int)
        for word in words:
            for c in word:
                letters[c] += 1
            
        result = True
        for key in letters: 
            result = result & (letters[key] % len(words) == 0)

        return result