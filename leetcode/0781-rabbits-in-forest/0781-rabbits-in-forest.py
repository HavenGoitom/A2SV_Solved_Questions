class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        count = 0
        freq = defaultdict(int)

        for num in answers:
            if num == 0:
                count += 1
            else:
                freq[num] += 1

                if freq[num] == num + 1:
                    count += num + 1
                    freq[num] = 0
        
        for num,freq in freq.items():
            if freq > 0:
                count += num + 1

        return count