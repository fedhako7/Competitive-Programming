class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        L = len(arr)
        arr.sort()
        arr[0] = 1
        start = 1
        max_ = float('-inf')

        idx = 0
        while idx < L:
            if abs(arr[idx] - start) > 1:
                start += 1

            else:
                start = arr[idx]

            max_ = max(max_, start)
            idx += 1


        return max_
                
        