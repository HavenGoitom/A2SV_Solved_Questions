n = int(input())
levels = list(map(int, input().split(" ")))

levels.sort()

for i in range(n):
    if n == i+1:
        print(i+1)
        break
    if levels[i] != i+1:
        print(i+1)
        break
    