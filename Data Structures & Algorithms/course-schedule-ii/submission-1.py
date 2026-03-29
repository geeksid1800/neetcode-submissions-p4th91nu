from collections import defaultdict
'''
Very similar solution to #207.Course Schedule, but we also have a completed[course] bool array.
When we get to the base case of a course we want to take having no pending prereqs, we don't
know if it's the first time reaching that base case, so we may end up adding that course multiple
times. To prevent that, use the completed[course] to make sure to not process any cases where it's
already True.
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        ans, completed = [], [False]*numCourses
        currCourses = set()
        def dfs(course) -> bool:
            if completed[course]:
                return True #course already taken, don't add to answer twice
            if not prereqs[course]:
                ans.append(course)
                completed[course] = True
                return True
            if course in currCourses:
                return False
            
            currCourses.add(course)
            for prereq in prereqs[course][::-1]:
                if not dfs(prereq):
                    return False
                prereqs[course].pop()
            
            currCourses.remove(course)
            completed[course] = True
            ans.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans
                