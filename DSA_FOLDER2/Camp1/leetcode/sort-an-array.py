class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(lHalf, rHalf):
            merged = []
            leftIdx, rightIdx = 0, 0
            while (leftIdx < len(lHalf) and (rightIdx) < len(rHalf)):
                if lHalf[leftIdx] <= rHalf[rightIdx]:
                    merged.append(lHalf[leftIdx])
                    leftIdx += 1

                else:
                    merged.append(rHalf[rightIdx])
                    rightIdx += 1

            merged.extend(rHalf[rightIdx: ])
            merged.extend(lHalf[leftIdx: ])
            return merged


        def devide(left, right, arr):
            if left == right:
                return [arr[left]]

            mid = (left + right) // 2

            leftHalf = devide(left, mid, arr)
            rightHalf = devide(mid + 1, right, arr)

            return merge(leftHalf, rightHalf)


        return devide(0, len(nums) - 1, nums)