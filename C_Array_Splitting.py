n,k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

total_cost = arr[n-1] - arr[0]
# print(total_cost)
costs = []

for i in range(1, n):
    costs.append((arr[i] - arr[i-1]))

costs.sort(reverse=True)
# print(costs)

for i in range(k-1):
    total_cost -= costs[i]


print(total_cost)