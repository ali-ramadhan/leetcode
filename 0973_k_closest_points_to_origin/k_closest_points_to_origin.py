import heapq
from math import sqrt

# Solution using sorting.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for p in points:
            x, y = p
            d = sqrt(x**2 + y**2)
            distances.append((p, d))
        
        distances = sorted(distances, key=lambda e: e[1])
        nearest = [e[0] for e in distances[:k]]
        return nearest

# Solution using a min heap.
# dist is negative so that closest points to the origin will have the largest value in the heap,
# allowing us to easily retrieve the k closest points.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p
            d = -sqrt(x**2 + y**2)
            if len(heap) == k:
                heapq.heappushpop(heap, (d, p))
            else:
                heapq.heappush(heap, (d, p))
        
        return [e[1] for e in heapq.nsmallest(k, heap)]
