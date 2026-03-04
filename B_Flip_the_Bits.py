def can_be_equal():
    n = int(input())
    a = input()
    b = input()
    a += '0'
    b += '0'
    # print(a)
    # print(len(a),len(b),n)
    count_0 = 0
    count_1 = 0

    for i in range(n):

        if a[i] == "1":
                count_1 += 1
        else:
            count_0 += 1

        if (a[i] == b[i] and a[i+1] != b[i+1]) or (a[i] != b[i] and a[i+1] == b[i+1]):
            
            if count_1 != count_0:
                return "NO"
            
    return "YES"

t = int(input())

for _ in range(t):
    print(can_be_equal())