from collections import Counter

t = int(input())
for _ in range(t):
    s = input().strip()             
    s_counter = Counter(s)          
    t_counter = Counter(input().strip()) 
    output = ""

    if s_counter - t_counter:
        print("Impossible")
        continue


    t_temp = t_counter.copy()
    
    for ch in s:
        t_temp[ch] -= 1

    words = "abcdefghijklmnopqrstuvwxyz"

    for chr in s:
        for w in words:
            if w < chr and t_temp[w] > 0:
                output += t_temp[w] * w
                t_temp[w] = 0
        output += chr


    for w in words:
        if t_temp[w] > 0:
            output += t_temp[w] * w

    print(output)