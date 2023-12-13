class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx_dict = {}
        common_strs = []
        min_idx = float('inf')

        for idx in range(len(list1)):
            idx_dict[list1[idx]] = idx

        for idx in range(len(list2)):
            if list2[idx] in idx_dict:
                idx_sum = idx + idx_dict[list2[idx]]

                if idx_sum < min_idx:
                    min_idx = idx_sum
                    common_strs = []
                    common_strs = [list2[idx]]
                elif idx_sum == min_idx:
                    common_strs.append(list2[idx])

        return common_strs