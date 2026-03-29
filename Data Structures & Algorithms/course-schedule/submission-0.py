from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list) #create an adjacency map of course->[prereqs]
        #tracks courses we are currently enrolled in as part of recursive stack to find loops
        currCourses = set()
        for course,prereq in prerequisites:
            prereqs[course].append(prereq)
        
        def dfs(course) -> bool: #return whether course can be taken without any order hiccups
            if course in currCourses:
                return False #found a circular dependency
            if not prereqs[course]:
                #course has no remaining prereqs, can be taken now itself
                return True
            
            currCourses.add(course)
            for prereq in prereqs[course][::-1]:
                if not dfs(prereq):
                    return False
                prereqs[course].pop() #could take that prereq without any issue
            
            currCourses.remove(course) #could take course without running into any prereq issues
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
