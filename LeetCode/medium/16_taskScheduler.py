# https://leetcode.com/problems/task-scheduler/




def leastIntervalDict(tasks, n):

    # Time O (n) | Space O (n)     

    if n == 0:
        # Quick response for special case on n = 0
        # no requirement for cooling, just do those jobs in original order
        return len(tasks)
    
    
    # key   : task
    # value : occurrence of tasks 
    task_occ_dict = Counter( tasks )
    
    # max occurrence among tasks
    max_occ = max( task_occ_dict.values() )
    
    # number of tasks with max occurrence
    number_of_taks_of_max_occ = sum( ( 1 for task, occ in task_occ_dict.items() if occ == max_occ ) )
    
    # Make (max_occ-1) groups, each groups size is (n+1) to meet the requirement of cooling
    # Fill each group with uniform iterleaving as even as possible
    
    # At last, execute for the last time of max_occ jobs
    intervl_for_schedule = ( max_occ-1 )*( n+1 ) + number_of_taks_of_max_occ
    
    # Minimal length is original length on best case.
    # Otherswise, it need some cooling intervals in the middle
    return max( len(tasks), intervl_for_schedule)


import heapq
from collections import Counter

def leastIntervalHeap(tasks, n):
    
    # Time O (n log n) | Space O (n)

    # Each entry in the queue is of the form (priority, task_id)
    task_queue = [(-1*task_freq, task_id)
                    for task_id, task_freq in Counter(tasks).items()]
    
    heapq.heapify(task_queue)
    
    elapsed_time = 0
    
    while task_queue:
        
        cool_down_timer = 0
        
        # Temporary queue will store tasks which need additional CPU hours to finish
        # but they cannot be processed in the current cool down period.
        temporary_queue = []
        
        # Before processing the next task start the cool down timer.
        while cool_down_timer <= n:
            
            elapsed_time += 1
            
            if task_queue:
                # Pop the task which requires the most CPU hours
                task_priority, task_id = heapq.heappop(task_queue)
                
                if task_priority < - 1:
                    # If the popped task needs more CPU hours, we will 
                    # add it to our temporary queue. This task will never be processed 
                    # again in the current cool down period.  
                    temporary_queue.append((task_priority + 1, task_id))
            
            if not task_queue and not temporary_queue:
                # This can happen if the task_queue had 1 task [(-1, 'A')] and we processed
                # it in the current cool down period and have nothing else to process
                break
            else:
                cool_down_timer += 1
        
        # The cool down timer has timed out. Add the tasks in temporary queue 
        # to our task queue. 
        for task in temporary_queue:
            heapq.heappush(task_queue, task)
    
    return elapsed_time

n = 2
tasks = ["A","A","A","B","B","B"]
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.