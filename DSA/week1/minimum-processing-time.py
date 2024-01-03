class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        # Change tasks to the longer ones only for each processor
        tasks = [tasks[idx] for idx in range(0, len(tasks), 4)] 

        time = 0
        for core, task in zip(processorTime, tasks):
            time = max(time, core + task)

        return time