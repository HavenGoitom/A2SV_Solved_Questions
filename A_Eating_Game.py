t = int(input())

for _ in range(t):

    n = int(input())
    eat = list(map(int, input().split(" ")))
    i = 0
    res = []

    max_num = max(eat)
    count = 0

    for num in eat:
        if num == max_num:
            count += 1
    print(count)



        
