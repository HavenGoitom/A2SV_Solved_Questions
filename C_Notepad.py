def can_type():

        n = int(input())
        s = input()

        seen = {}

        for i in range(n-1):
            substring = s[i:i+2]

            if substring in seen:
                prev_idx = seen[substring]
                if prev_idx < i:
                    return "YES"
            else:
                seen[substring] = i+1
        return "NO"

t = int(input())

for i in range(t):
    print(can_type())
            
