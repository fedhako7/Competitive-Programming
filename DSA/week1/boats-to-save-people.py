class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat_num = 0
        
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                boat_num += 1
                left += 1
                right -= 1
            #elif left == right:
            else:
                boat_num += 1
                right -= 1

        return boat_num