class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        hash_map = {}
        output = []

        changed_sort = sorted(changed, reverse = True)

        for num in changed_sort:
            if num % 2 == 0 and num not in hash_map:
                hash_map[num//2] = num
            elif len(output) < len(changed)//2:
                output.append(num)
            
        if len(output) != len(changed)//2:
            return []
        for num in output:
            if num not in hash_map:
                return []
        return output