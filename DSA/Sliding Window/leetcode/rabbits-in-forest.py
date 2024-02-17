class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)

        count = dict(count)
        print(count)

        num = 0
        for key, val in count.items():
            print(key, val)
            num += (ceil(val / (key + 1)) * (key + 1))

        return num
        