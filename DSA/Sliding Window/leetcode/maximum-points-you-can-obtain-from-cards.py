class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        first_parts = cardPoints[ :k] 
        end_parts = cardPoints[-k: ]

        end_parts.extend(first_parts)
        cardPoints = end_parts

        print(cardPoints)
        curr_sum = sum(cardPoints[ :k])
        sum_ = curr_sum

        for idx in range(k, len(cardPoints)):
            curr_sum += (cardPoints[idx] - cardPoints[idx - k])
            sum_ = max(sum_, curr_sum)


        return sum_