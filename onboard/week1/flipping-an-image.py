class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()

            for idx in range(len(row)):
                if row[idx]:
                    row[idx] = 0
                else:
                    row[idx] = 1

        return image
               