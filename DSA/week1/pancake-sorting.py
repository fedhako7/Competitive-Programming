class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        [32154]  [51234 [43215]]

        arr = arr[:max + 1][::-1] + [ma + 1:]
        arr = arr[: i + 1][::-1] + [i + 1:]

        '''
        correct = sorted(arr)

        flips = []
        length = len(arr)                   
        for i in range(length - 1, -1, -1):
            if arr == correct: break
            min_id = i
            for j in range(i, -1, -1):
                if arr[j] > arr[min_id]:
                    min_id = j
                    

            if min_id != i:

                arr = arr[ :min_id + 1][::-1] + arr[min_id + 1: ]
                print(arr)
                arr = arr[ :i + 1][::-1] + arr[i + 1: ]
                print(arr)

                flips.append(min_id + 1)
                flips.append(i + 1)

        i = [i for i in range(100, 0, -1)]
        print(i)

           

        
        return flips