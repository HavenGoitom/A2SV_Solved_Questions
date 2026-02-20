n = int(input())
contests = list(map(int, input().split(" ")))
contests.sort()
i = 1
count = 0


for contest in contests:
    if contest >= i:
        count += 1
        i += 1
print(count)