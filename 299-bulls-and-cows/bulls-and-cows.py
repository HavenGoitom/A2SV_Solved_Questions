class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s_dict = Counter(secret)
        g_dict = Counter(guess)

        b_count = 0
        c_count = 0

        bulls = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls.append(secret[i])
                b_count += 1

        for key in g_dict:
            c_count += min(s_dict[key], g_dict.get(key, 0))

        c_count = c_count - b_count

        ans = f'{b_count}A{c_count}B'

        return ans
        