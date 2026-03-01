t = int(input())


def test(a):
    s = []
    for chr in a:
        s.append(chr)

    left = 0
    n = len(s)
    right = n - 1

    # print(s)

    if n % 2 == 0:
        while left <= right:
            s[left], s[left + 1] = s[left + 1],s[left]
            # print(s[left], s[left + 1])
            s[right], s[right - 1] = s[right - 1],s[right]

            # print(s)

            left += 1
            right -= 1

            if a != s:
                return "YES"
            
        return "NO"



    while left <= right and left < ((n//2) - 1) and right > ((n//2) + 1):
        s[left], s[left + 1] = s[left + 1],s[left]
        # print(s[left], s[left + 1])
        s[right], s[right - 1] = s[right - 1],s[right]

        # print(s)

        left += 1
        right -= 1

        if a != s:
            return "YES"
        
    return "NO"


for _ in range(t):
    a = list(input())

    print(test(a))

    
            


        

