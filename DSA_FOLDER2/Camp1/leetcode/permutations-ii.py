class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def backT(count, path):
            if len(path) == len(nums):
                perms.append(path[:])
                return 

            for elem in count:
                if count[elem]:
                    count[elem] -= 1
                    path.append(elem)
                    backT(count, path)
                    path.pop()
                    count[elem] += 1

                
        
        count = Counter(nums)
        perms = []
        backT(count, [])
        return perms
            
        