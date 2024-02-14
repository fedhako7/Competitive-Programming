class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(reverse = True, key = lambda a: a[1] - a[0])
        target = len(costs) / 2
        count = 1
        cost = 0


        for city in costs:
            if count <= target:
                cost += city[0]
                count += 1

            else:
                cost += city[1]


        return cost