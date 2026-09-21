class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_to_st = defaultdict(list)

        for ind, st in enumerate(strs):
            curr = [0] * 26
            for char in st:
                curr[ord(char) - ord('a')] += 1
            curr = tuple(curr)
            list_to_st[curr].append(st)

        return list(list_to_st.values())

            