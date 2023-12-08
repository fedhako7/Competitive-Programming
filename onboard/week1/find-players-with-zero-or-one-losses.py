class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Extract winners and losers to sepate lists
        winners = [w[0] for w in matches]
        losers = [l[1] for l in matches]

        # Count number of times each losers loses
        l_count = Counter(losers)

        # Convert winners and losers to set, removes winners who are losers too
        winners = set(winners)
        losers = set(losers)
        winners.difference_update(losers)
        winners = list(winners)
        winners.sort()

        # Update losers to those who loses once only and sort
        losers = [l for l in l_count if l_count[l] == 1]
        losers.sort()

        return [winners, losers]
