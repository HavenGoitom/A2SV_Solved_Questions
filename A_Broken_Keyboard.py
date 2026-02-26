t = int(input())

for i in range(t):
    s = input()

    left = 0 
    right = 1
    res = set()
    if len(s) == 1:
        res.add(s[0])

    while right < len(s):
        
        if s[left] == s[right] and right < len(s):
            left += 2
            right += 2
        else:
            res.add(s[left])
            left += 1
            right += 1
        if left == len(s) - 1:
            res.add(s[left])
    print("".join(sorted(res)))


