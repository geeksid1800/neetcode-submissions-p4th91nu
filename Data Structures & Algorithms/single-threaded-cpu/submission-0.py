'''
Sort tasks by starting time, so you pick the earliest starting tasks first.
Then while that task is processing, add all tasks that will become available in the meantime to
a pq (min-heap) of [processingTime, index, enqueTime].
Then pick from the pq if there are available tasks, or wait and pick from array if there aren't. 
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        myTasks = [[task[0], ix, task[1]] for ix,task in enumerate(tasks)]
        myTasks.sort(reverse=True) #sorted in reverse so popping is easy
        freeTime = 0 #when CPU is free next to process tasks
        waiting = [] #available tasks waiting to be processed [processingTime, index, enqueTime].
        heapq.heapify(waiting)
        ans = []
        while waiting or myTasks:
            while myTasks and myTasks[-1][0] <= freeTime:
                #myTasks[i] = [enqueTime, ix, processingTime]
                availableTask = myTasks.pop()
                heapq.heappush(waiting, availableTask[::-1])
            
            if waiting:
                bestTask = heapq.heappop(waiting)
                ans.append(bestTask[1])
                freeTime += bestTask[0]
            else:
                #no available tasks, timeskip to next starting time
                if myTasks: freeTime = myTasks[-1][0]
        
        return ans