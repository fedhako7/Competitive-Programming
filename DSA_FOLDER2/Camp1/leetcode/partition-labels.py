class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        strings = []
        lengths =[]
        s_copy = list(s)

        for char in s:
            strings.append(char)
            s_copy.remove(char)

            splittable = all(ch not in s_copy for ch in strings)
            if splittable:
                lengths.append(len(strings))
                s_copy = list(s)[len(strings): ]
                strings = []
                
        return lengths
