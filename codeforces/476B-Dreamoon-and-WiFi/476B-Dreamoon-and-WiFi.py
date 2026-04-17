def helper(val, idx):
    if idx == len(s2):
        res.append(val)
        return
    
    c = s2[idx]

    if c == '+':
        helper(val + 1, idx + 1)

    elif c == '-':
        helper(val - 1, idx + 1)

    else:
        helper(val + 1,idx + 1)
        helper(val - 1, idx + 1) 


helper(0, 0)
valid = res.count(p1)


print(valid / len(res))