class Solution:
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        left, right = 0, len(skill) - 1
        teams_chem = []
        ref_team = [skill[left], skill[right]]

        while left < right:
            if skill[left] + skill[right] == ref_team[0] + ref_team[1]:
                teams_chem.append(skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1

        return sum(teams_chem)
