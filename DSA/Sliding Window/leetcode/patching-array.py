class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        tot = sum(nums)
        patch = 0
        prefix = 0
        freq = Counter(nums)
        exists = set(nums)

        idx = 1
        while idx <= n:
            num = idx
            if num in exists:
                prefix += (num * freq[num])

            elif prefix >= n:
                return patch

            elif num > prefix:
                prefix += num
                patch += 1
                print(num)

            idx += 1

            if prefix > tot:
                while True:
                    if prefix >= n:
                        return patch

                    else:
                        print(prefix)
                        prefix += (prefix + 1)
                        patch += 1

        return patch