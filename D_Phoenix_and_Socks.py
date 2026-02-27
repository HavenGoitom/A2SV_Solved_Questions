from collections import Counter

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    if l<=r:
        count = 0

        socks_right = Counter(socks[l:])
        need = r-l//2

        # check for a match
        for i in range(l):
            if socks_right[socks[i]] > 0:
                socks_right[socks[i]] -= 1
            else:
                count += 1
        
        #checks if there is a need and finds duplicates and removes them all

        if need > 0:

            for key in socks_right:

                if socks_right[key] > 1:
                    sub = socks_right[key] // 2 # 5//2 = 2 4//2 = 2

                    need -= sub
                    count += sub

                    socks_right[key] -= sub * 2 #update the hash_map

                if need == 0:
                    break

        if need:
            count += need
        
        print(count)

    else:        
        count = 0

        socks_left = Counter(socks[:r])
        need = l-r//2

        # check for a match
        for i in range(r):
            if socks_left[socks[i]] > 0:
                socks_left[socks[i]] -= 1
            else:
                count += 1
        
        #checks if there is a need and finds duplicates and removes them all

        if need > 0:

            for key in socks_left:

                if socks_left[key] > 1:
                    sub = socks_left[key] // 2 # 5//2 = 2 4//2 = 2

                    need -= sub
                    count += sub

                    socks_right[key] -= sub * 2 #update the hash_map

                if need == 0:
                    break

        if need:
            count += need
        
        print(count)
            


    
