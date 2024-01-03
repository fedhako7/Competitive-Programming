class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem = 0
        tot = skill[0] + skill[-1]
        
        left, right = 0, len(skill) - 1
        while left < right:
            if skill[left] + skill[right] == tot:
                chem += (skill[left] * skill[right])
                left += 1
                right -= 1

            else:
                return -1

        return chem