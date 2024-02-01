class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        population = [0] * 101

        for birth, death in logs:
            birth -= 1950
            death -= 1950

            population[birth] += 1
            population[death] -= 1

        for idx in range(1, 101):
            population[idx] += population[idx - 1]



        max_pop = max(population)
        for idx in range(101):
            if population[idx] == max_pop:
                return (1950 + idx)

        