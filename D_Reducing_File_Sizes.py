def compress():
    
    n,m = map(int, input().split(" "))
    files = []

    for i in range(n):
        a,b = map(int, input().split(" "))
        files.append([a,b])
        
    files.sort(key=lambda x: x[0] - x[1], reverse=True)
    # print(files)
    count = 0
    sum1 = 0
    sum2 = 0


    for j in range(n):
        sum1 += files[j][0]

    for j in range(n):
        sum2 += files[j][1]

    if sum1 <= m:
        return 0
    
    if sum2 > m:
        return -1
    
    
        
    for i in range(n):
        # print(sum)
        sum1 -= (files[i][0] - files[i][1])
        count += 1

        if sum1 <= m:
            return count

    return -1



print(compress())
