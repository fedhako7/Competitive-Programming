class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = 0
        freq = defaultdict(int)

        curr_len = 0
        longer = 0
        left = 0
        for idx in range(len(answerKey)):
            curr_len += 1
            freq[answerKey[idx]] += 1
            longer = max(freq['F'], freq['T'])

            while curr_len - longer > k:
                freq[answerKey[left]] -= 1
                curr_len -= 1
                left += 1

            length = max(length, curr_len)


        return length


            
        