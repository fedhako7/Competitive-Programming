class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # The problem can be seen as arithmetic sum from maximum sum 
        # of list for k times.

        largest = max(nums)
        top_arith = (k + largest - 1) * (k + largest) / 2
        bot_arith = (largest - 1) * (largest) / 2
        score = int(top_arith - bot_arith)

        return score
        
        