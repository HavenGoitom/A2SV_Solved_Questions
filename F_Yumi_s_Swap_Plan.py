# Fixed sliding window if it is a circle question move 2n times and use mode or make the arrart 2*n and loop over it

n = int(input())
s = input()

h_count = s.count("H")
# print(h_count) #5
s = s+s
t_count = 0
window = 0
left = 0
min_swap = n*2

for i in range(n*2):
    
    if window == h_count:
        # print(t_count)
        min_swap = min(min_swap, t_count)

    if s[i] == "T":
        t_count += 1
    window += 1


    if window > h_count:
        if s[left] == "T":
            t_count -= 1
        window -= 1
        left += 1

    
print(min_swap)
    
    


