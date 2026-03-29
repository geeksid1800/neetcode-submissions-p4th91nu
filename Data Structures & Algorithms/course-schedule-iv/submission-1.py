from collections import defaultdict
'''
For this, we remember that for any prereq P of a course C, all prereqs of P are also prereqs of C.
So for immediate prereqs of C as P1,P2...Pn, we have all prereqs of C = Concat{Pi+prereqs(Pi)}.
The approach is thus recursive. Go on finding prereqs of a given course until you reach a course
without any prereqs. For each prereq P of C, add P and P's prereqs to ans for C.
Remember to track which courses you have already completely found all prereqs for.
Say 4 is a prereq of both 5 and 6, if you've already found 4's prereqs as part of finding prereqs
of 5, you don't need to find it again when you find all prereqs of 6. 
'''
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

            for prereq in prereqs[course]: #prereq is immediate prerequisite of course
                allreqs[course].add(prereq)
                findPrereqs(prereq)
                allreqs[course].update(allreqs[prereq])
            
            visited[course] = True
        
        ans = []
        for u,v in queries: #check if u is a prereq of v
            findPrereqs(v)
            ans.append(True if u in allreqs[v] else False)
        
        return ans