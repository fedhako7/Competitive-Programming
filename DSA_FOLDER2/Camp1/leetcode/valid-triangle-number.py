class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        L = len(nums)
        if L < 3:
            return 0
            

        nums.sort()
        right = 2
        triangles = 0
        while right < L:
            idx1, idx2 = 0, right - 1
            
            while idx1 < idx2:
                if nums[idx1] + nums[idx2] > nums[right]:
                    triangles += (idx2 - idx1)
                    idx2 -= 1
                    idx1 -= 1

                idx1 += 1

            right += 1

        return triangles


                


