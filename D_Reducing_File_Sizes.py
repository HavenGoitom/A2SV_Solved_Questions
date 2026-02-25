n,m = map(int, input().split(" "))
files = []

for i in range(n):
    a,b = map(int, input().split(" "))
    files.append([a,b])

files.sort(key=lambda x: x[0] - x[1], reverse=True)
# print(files)
count = 0
can_comp = False
sum = 0

for j in range(n):
    sum += files[j][0]

for i in range(n):
    # print(sum)
    if sum <= m:
        continue
    else:
        sum -= (files[i][0] - files[i][1])
        count += 1

if can_comp:
    print(count)
else:
    print(-1)

