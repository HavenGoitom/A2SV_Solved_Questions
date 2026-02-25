class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill)-1

        skill.sort()

        val = skill[left] + skill[right]
        res = 0
        while left < right:

            if skill[left] + skill[right] != val:
                return -1
            # print(skill[left] * skill[right])

            res += skill[left] * skill[right]

            left += 1
            right -= 1
            
        return res
            