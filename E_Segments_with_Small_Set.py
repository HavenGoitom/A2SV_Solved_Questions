from collections import defaultdict
n,s = map(int, input().split(" "))
a = list(map(int, input().split(" ")))


def small_set(n,s,a):

    dic = defaultdict(int)
    count = 0
    unique = 0
    left = 0

    for right in range(n):

        if dic[a[right]] == 0:
            unique += 1
        dic[a[right]] += 1

        while unique > s:
            dic[a[left]] -= 1
            if dic[a[left]] == 0:
                unique -= 1
            left += 1
        
        count += (right-left + 1)


    return count

print(small_set(n,s,a))



# def small_set(n,s,a):

#     count = 0
#     left = 0

#     for i in range(n):
#         sets = set()
#         left = i
#         while len(sets)<s and left<n:

#             sets.add(a[left])
#             left += 1
#             count += 1
        
#         while left<n and len(sets) == s and a[left] in sets:
#             count += 1
#             left += 1

#     return count

# print(small_set(n,s,a))