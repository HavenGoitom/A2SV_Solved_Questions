t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    right = 2*n -1
    left = right - 1
    count = 0
    moves = 0

    while left>=0 and right > 0:

        count += min(nums[left], nums[right])
        left -= 2
        right -= 2
        moves += 1
        if moves == n:
            break
    print(count)
