class NumArray(object):

    def __init__(self, nums):
        self.prefix = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix.append(curr)

    def sumRange(self, left, right):
      rightSum = self.prefix[right]
      leftSum = self.prefix[left - 1] if left > 0 else 0

      return rightSum - leftSum
