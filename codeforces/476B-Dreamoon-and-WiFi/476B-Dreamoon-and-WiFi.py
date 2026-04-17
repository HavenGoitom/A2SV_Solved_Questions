def helper(idx, val):
    if idx == len(s2):
        if val == p1:
            return 1  
        else:
            return 0

    c = s2[idx]

    if c == '+':
        return helper(idx + 1, val + 1)

    elif c == '-':
        return helper(idx + 1, val - 1)

    else:
        return helper(idx + 1, val + 1) + helper(idx + 1, val - 1)


valid = helper(0, 0)
total = 2 ** s2.count('?')

print(valid / total)