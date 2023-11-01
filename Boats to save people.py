class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l, r = 0, len(people) - 1
        boat = 0
        if people[l] > limit:
            return len(people)
        while l < r:
            if people[l] + people[r] <= limit:    
                boat += 1
                l += 1
                r -= 1 
            else:
                boat += 1
                r -= 1
        if l == r or people[r] + people[r + 1] > limit:
            boat += 1

        return boat
