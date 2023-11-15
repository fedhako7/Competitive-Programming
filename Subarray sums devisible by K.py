class Solution(object):
    def subarraysDivByK(self, nums, k):

        hashMap = {0:1}
        curr, answer =0, 0
        for num in nums:
            curr += num
            reminder = curr % k
            if reminder in hashMap:
                answer += hashMap[reminder]
                hashMap[reminder] += 1
            else:
                hashMap[reminder] = 1


        return answer 
