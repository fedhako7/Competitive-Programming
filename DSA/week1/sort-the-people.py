class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for idx in range(1, len(names)):
            key = heights[idx]
            curr_n = names[idx]
            idx2 = idx - 1
            while idx2 > -1 and key > heights[idx2]:
                heights[idx2 + 1] = heights[idx2]
                names[idx2 + 1] = names[idx2]                
                idx2 -= 1

            heights[idx2 + 1] = key
            names[idx2 + 1] = curr_n


        return names