def start(interval):
    return interval[0]

def end(interval):
    return interval[1]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        start_new, end_new = newInterval

        result = []
        i = 0

        # Before newInterval: Keep appending intervals as long as we don't have to do any merging.
        while i < n and end(intervals[i]) < start(newInterval):
            result.append(intervals[i])
            i += 1
        
        # Around newInterval: Keep merging intervals so accomadate newInterval.
        while i < n and start(intervals[i]) <= end(newInterval):
            newInterval[0] = min(start(intervals[i]), start(newInterval))
            newInterval[1] = max(end(intervals[i]), end(newInterval))
            i += 1
        result.append(newInterval)

        # After newInterval: Keep appending intervals.
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
