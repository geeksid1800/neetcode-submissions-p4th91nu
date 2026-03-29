from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        allreqs = defaultdict(set) #stores ALL required courses for a given course
        prereqs = defaultdict(list) #course:[prereqs] mapping
        visited = [False]*numCourses

        for prereq, course in prerequisites:
            prereqs[course].append(prereq)
        
        def findPrereqs(course):
            if visited[course]:
                return
            if not prereqs[course]:
                visited[course] = True
                return

            for prereq in prereqs[course]: #for immediate prerequisites of course
                allreqs[course].add(prereq)
                findPrereqs(prereq)
                allreqs[course].update(allreqs[prereq])
            
            visited[course] = True
        
        ans = []
        for u,v in queries: #check if u is a prereq of v
            findPrereqs(v)
            if u in allreqs[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans