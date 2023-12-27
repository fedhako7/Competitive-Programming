class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def comparator(item):
            if item in key_dic:
                return key_dic[item]

            else:
                return key_dic2[item]


        arr3 = [num for num in arr1 if num not in arr2]
  

        key_dic = {num : idx for idx, num in enumerate(arr2)}
        key_dic2 = {num : len(arr2) + num for idx, num in enumerate(arr3)}
        
        arr1.sort(key = comparator)

        return arr1
