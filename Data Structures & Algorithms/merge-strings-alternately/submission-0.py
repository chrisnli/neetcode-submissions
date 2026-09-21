class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        i = 0
        new_word = ""

        while i < len(word1) and i < len(word2):
            new_word = new_word + word1[i]
            new_word = new_word + word2[i]
            i += 1

        if i < len(word1): new_word = new_word + word1[i:]
        if i < len(word2): new_word = new_word + word2[i:]
        return new_word