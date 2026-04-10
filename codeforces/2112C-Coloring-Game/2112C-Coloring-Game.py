t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    arr.sort(reverse=True)
    max = arr[0]

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            if arr[left] + arr[right] > arr[i] and arr[i] + arr[left] + arr[right] > max:
                ans += (right - left)
                left += 1
            else:
                right -= 1
    print(ans)