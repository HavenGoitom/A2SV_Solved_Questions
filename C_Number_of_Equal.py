from collections import Counter

n,m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

a_counter = Counter(a)
b_counter = Counter(b)
count = 0

if len(a_counter) > len(b_counter):
    keys = a_counter
else:
    keys = b_counter

for key in keys:
    count += a_counter[key] * b_counter[key]

print(count)






