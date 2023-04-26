def start(interval):
    return interval[0]

def end(interval):
    return interval[1]

def _merge(intervals):
    intervals.sort(key=lambda x: start(x))
    merged = []
    for interval in intervals:
        if merged == [] or end(merged[-1]) < start(interval):
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], end(interval))
    return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return _merge(intervals)
