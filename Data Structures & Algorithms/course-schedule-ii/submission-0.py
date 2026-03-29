from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        ans, completed = [], [False]*numCourses
        currCourses = set()
        def dfs(course) -> bool:
            if completed[course]:
                return True #course already taken
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
                