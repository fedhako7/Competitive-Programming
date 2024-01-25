class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indices = defaultdict(list)
        min_pick = float('inf')

        for idx, value in enumerate(cards):
            indices[value].append(idx)

        for key in indices:
            curr_list = indices[key]

            idx = 1
            while idx < len(curr_list):
                min_pick = min( min_pick, curr_list[idx] - curr_list[idx - 1] )
                idx += 1

        return (min_pick + 1) if min_pick != float('inf') else -1

        