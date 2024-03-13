class Solution:
    def pivotInteger(self, n: int) -> int:
        
        prefixSum = [0] * n
        postfixSum = [0] * n
        postfixSum[n - 1] = n
        prefixSum[0] = 1
        for idx in range(1, n):
            prefixSum[idx] = prefixSum[idx - 1] + (idx + 1)

        for idx in range(n - 2, -1, -1):
            postfixSum[idx] = postfixSum[idx + 1] + (idx + 1)

        print(prefixSum, postfixSum)
        for idx in range(n):
            if prefixSum[idx] == postfixSum[idx]:
                return (idx + 1)

        return -1
