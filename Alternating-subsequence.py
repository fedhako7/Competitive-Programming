def biggest_alternating(nums):
    nums.append(-nums[-1]) #last element is for transition

    sub_nums =[]
    extreme_num = -float("inf")
    in_positives = nums[0] > 0

    for num in nums:
        to_negatives = in_positives and num < 0
        to_positives = (not in_positives )and num > 0

        if to_negatives or to_positives:
            in_positives = not in_positives
            sub_nums.append(extreme_num)
            extreme_num = -float("inf")
            
        extreme_num = max(extreme_num, num)
    return sub_nums

def main():
    num_testcases = int(input())
    for _ in range(num_testcases):
        length = int(input())
        nums = list(map(int, input().split()))
        print(sum(biggest_alternating(nums)))


main()
