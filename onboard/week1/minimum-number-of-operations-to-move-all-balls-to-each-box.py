class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        bLen = len(boxes) - 1
        left_op = {0: [0, 0]} if int(boxes[0]) == 0 else {0: [1, 0]}
        right_op = {bLen: [0, 0]} if int(boxes[bLen]) == 0 else {bLen: [1, 0]}
        tot_op = [0] * (bLen + 1)

        for i, n in enumerate(boxes):
            if i > 0:
                left_op[i] = [int(n) + left_op[i-1][0], sum(left_op[i - 1])]

        for i, n in reversed(list(enumerate(boxes))):
            if i < bLen:
                right_op[i] = [int(n) + right_op[i+1][0], sum(right_op[i + 1])]

        for i in range(bLen + 1):
            tot_op[i] = left_op[i][1] + right_op[i][1]
        
        return tot_op