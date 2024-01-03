class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        indices = [0] * (max(costs) + 1)
        sorted_costs = [0] * len(costs)
        ice_cream = 0

        for cost in costs:
            indices[cost] += 1

        for idx in range(1, len(indices)):
            indices[idx] += indices[idx - 1]

        i = len(costs) - 1
        while i > -1:
            sorted_costs[indices[costs[i]] - 1] = costs[i]
            indices[costs[i]] -= 1
            i -= 1

        for cost in sorted_costs:
            if coins - cost >= 0:
                ice_cream += 1
                coins -= cost

        return ice_cream
        
