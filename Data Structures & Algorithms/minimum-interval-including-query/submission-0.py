class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        interval_length = {}
        for interval in intervals:
            interval_length[(interval[0], interval[1])] = interval[1] - interval[0] + 1
        
        def bs(curr_list, query):
            
            i = 0
            minimum_length = float('inf')
            while i < len(curr_list):
                if query <curr_list[i][0]: 
                    i += 1
                    continue
                if query <= curr_list[i][1]:
                    minimum_length = min(minimum_length, interval_length[(curr_list[i][0],curr_list[i][1])])
                i += 1
            return minimum_length if minimum_length != float('inf') else -1
        
        result = []
        for query in queries:
            result.append(bs(intervals, query))

        return result
                