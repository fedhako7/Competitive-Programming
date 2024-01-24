class Solution:
    def maxScore(self, s: str) -> int:
        scores = {} #Total score
        right_scores = {} #Right part score
        max_score = 0

        scores[0] = 1 if s[0] == '0' else 0
        right_scores[len(s) - 1] = 0
        for idx in range(1, len(s)):
            scores[idx] = scores[idx -1]
            if s[idx] == '0':
                scores[idx] += 1

        for idx in range(len(s) - 2, -1, -1):
            right_scores[idx] = right_scores[idx + 1]
            if s[idx + 1] == '1':
                right_scores[idx] += 1

            scores[idx] += right_scores[idx]
            

        #You can't split on the last element
        #It leaves the right part empty
        for key in range(len(s) - 1): 
            max_score = max(max_score, scores[key])
        
        return max_score



