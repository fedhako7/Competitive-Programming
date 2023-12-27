from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        count1, count2, answer = Counter(nums1), Counter(nums2), []
        for key in count1.keys():
            if count2.get(key, 0):
                temp = [key] * min(count1[key], count2[key])
                answer.extend(temp)

        return answer