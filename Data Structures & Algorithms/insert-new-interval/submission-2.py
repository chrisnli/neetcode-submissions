class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            prev_right = intervals[i - 1][1]
            if intervals[i][0] <= prev_right:
                prev_int = i - 1
                prev_left = intervals[i - 1][0]
                while i < len(intervals) and intervals[i][0] <= prev_right:
                    prev_right = max(prev_right, intervals[i][1])
                    i += 1
                
                intervals = intervals[:prev_int] + [[prev_left, prev_right]] + intervals[i:]
                i = prev_int + 1
            else:
                i += 1
        return intervals