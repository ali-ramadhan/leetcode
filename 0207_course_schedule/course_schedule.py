# Perform a depth-first search on the graph to determine whether we can take course.
# We set the current course we are evaluating as -1.
def can_take(graph, visited, course):
    # We are current evaluating course i so there is a cycle and we cannot take course.
    if visited[course] == -1:
        return False
    
    # Already visited course.
    if visited[course] == 1:
        return True

    # Mark as currently visiting.
    visited[course] = -1

    # Visit all the neigbors.
    for next_course in graph[course]:
        if not can_take(graph, visited, next_course):
            return False
    
    # Done visiting course i, we can take it.
    visited[course] = 1

    return True

def can_finish(n_courses, prerequisites):
    # Construct directed graph of pre-reqs using a list.
    # graph[b] returns a list of courses [a1, a2, ...] you can take given that you've taken course b.
    graph = [[] for _ in range(n_courses)]
    for prereq in prerequisites:
        a, b = prereq
        graph[b].append(a)
    
    visited = [0 for _ in range(n_courses)]
    
    for course in range(n_courses):
        if not can_take(graph, visited, course):
            return False
    
    return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return can_finish(numCourses, prerequisites)
