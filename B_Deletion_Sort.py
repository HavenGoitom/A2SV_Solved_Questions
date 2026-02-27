t = int(input())


def deleteSort(n,a):
    b = sorted(a)
    if a == b:
        return len(a)
    return 1

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split(" ")))
    print(deleteSort(n,a))

