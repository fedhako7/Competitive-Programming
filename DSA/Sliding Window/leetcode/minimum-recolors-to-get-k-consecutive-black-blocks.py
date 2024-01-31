class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_recolor = blocks[ :k].count('W')
        min_recolor = curr_recolor

        for idx in range(k, len(blocks)):
            if blocks[idx] == 'W':
                curr_recolor += 1

            if blocks[idx - k] == 'W':
                curr_recolor -= 1

            min_recolor = min(curr_recolor, min_recolor)

        return min_recolor