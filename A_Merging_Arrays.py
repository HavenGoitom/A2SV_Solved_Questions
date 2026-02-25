len_n, len_m = map(int, input().split(" "))
n = list(map(int, input().split(" ")))
m = list(map(int, input().split(" ")))

def checkOrder(n,m):
    new = []
    p1,p2 = 0, 0
    while p1<len_n and p2<len_m:
        if n[p1]<m[p2]:
            new.append(n[p1])
            p1 += 1
        else:
            new.append(m[p2])
            p2 += 1
    
    new.extend(n[p1:])
    new.extend(m[p2:])
    
    print(*new)
    


checkOrder(n,m)
    