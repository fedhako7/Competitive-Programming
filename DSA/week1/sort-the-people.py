class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(1, len(names)):
                if heights[j - 1] < heights[j]:
                    heights[j - 1], heights[j] = heights[j], heights[j - 1]
                    names[j - 1], names[j] = names[j], names[j - 1]

        return names