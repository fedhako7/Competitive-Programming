class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        for num in nums1:
            temp.append(num)

        l, r, k = 0, 0, 0
        while l < m and r < n:
            if temp[l] <= nums2[r]:
                nums1[k] = temp[l]
                l += 1
            elif temp[l] > nums2[r]:
                nums1[k] = nums2[r]
                r += 1
            k += 1

        while l < m:
            nums1[k] = temp[l]
            l += 1
            k += 1
        while r < n:
            nums1[k] = nums2[r]
            r += 1
            k += 1

        return nums1
