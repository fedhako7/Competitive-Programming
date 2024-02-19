class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L = len(nums1)
        L2 = len(nums2)
        nextDic = {}

        greaters = []
        for idx in range(L2):
            while greaters and nums2[idx] > nums2[greaters[-1]]:
                num = nums2[greaters[-1]]
                nextDic[num] = nums2[idx]
                greaters.pop()

            greaters.append(idx)

        
        nextG = [-1] * L

        for idx, num in enumerate(nums1):
            if num in nextDic:
                nextG[idx] = nextDic[num]


        return nextG


        