n = int(input())

block_pos = {}
value = []

for block in range(n):
    a = list(map(int, input().split(" ")))
    k = a[0]
    b = a[1:]

    for idx,val in enumerate(b):
        block_pos[val] = [block, idx]
        value.append(val)

value.sort()
good = 0

for i in range(len(value)-1):
    b1,p1 = block_pos[value[i]]
    b2,p2 = block_pos[value[i+1]]

    if b1==b2 and p2 == p1 + 1:
        good += 1

blocks = len(value) - good # will give us all the blocks after splited including good
combine = blocks - 1
split = blocks - n # we init have 2 block but after the split we have 3 so 3 - 2 will give us the amount of splits we need

print(split,combine)





