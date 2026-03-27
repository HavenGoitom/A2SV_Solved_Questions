from collections import defaultdict

n = int(input())
flag = True
hashmap = {} # i want hashmap[1] = [2,3,4]

for i in range(2, n+1):
    parent = int(input())
    if parent in hashmap:
        hashmap[parent].append(i)
    else:
        hashmap[parent] = [i]

# print(hashmap)

for parent in hashmap:
    
    leaf_node = 0

    for children in hashmap[parent]:
        if children not in hashmap:
            leaf_node += 1
    
    if leaf_node < 3:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")