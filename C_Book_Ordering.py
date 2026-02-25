n = int(input())
books = []

for i in range(n):
    w,h = map(int,input().split(" "))
    books.append([w,h])
# print(books) [(3, 4), (4, 6), (3, 5)]

flag = True

if books[0][0] > books[0][1]:
    books[0][1] , books[0][0] = books[0][0] , books[0][1]

for i in range(n-1):
    if books[i][1] >= books[i+1][1]:
        continue
    if books[i][1] >= books[i+1][0]:
        books[i+1][0],books[i+1][1] =  books[i+1][1], books[i+1][0]
        continue
    flag = False
    break
    
if flag:
    print("YES")
else:
    print("NO")
