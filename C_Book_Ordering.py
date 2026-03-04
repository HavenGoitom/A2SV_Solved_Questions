n = int(input())
books = []

for i in range(n):
    w,h = map(int,input().split(" "))
    books.append([w,h])
# print(books) [(3, 4), (4, 6), (3, 5)]

flag = True


previous_height = float('inf')

for w,h in books:
    big = max(w, h)
    small = min(w, h)

    if big <= previous_height:
        previous_height = big
    elif small <= previous_height:
        previous_height = small
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")