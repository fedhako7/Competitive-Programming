class Solution:
    def getRow(self, rowIdx: int) -> List[int]:
        pTriang = [1] * (rowIdx + 1)

        if rowIdx == 0:
            return pTriang

        prevTriang = self.getRow(rowIdx - 1)

        for idx in range(1, len(pTriang) - 1):
            pTriang[idx] = prevTriang[idx - 1] + prevTriang[idx]

        
        return pTriang

