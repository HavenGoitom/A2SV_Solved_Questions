# prefix sums for horizontal and vertical domino placements
hor = [[0] * (h + 1) for _ in range(w + 1)]
ver = [[0] * (h + 1) for _ in range(w + 1)]

# build prefix arrays
for y in range(h):
    for x in range(w):
        hor[x + 1][y + 1] = (
            hor[x][y + 1]
            + hor[x + 1][y]
            - hor[x][y]
        )
        ver[x + 1][y + 1] = (
            ver[x][y + 1]
            + ver[x + 1][y]
            - ver[x][y]
        )

        if grid[y][x] != '.':
            continue

        # horizontal domino
        if x != w - 1 and grid[y][x + 1] == '.':
            hor[x + 1][y + 1] += 1

        # vertical domino
        if y != h - 1 and grid[y + 1][x] == '.':
            ver[x + 1][y + 1] += 1

q = int(input())
for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())

    x1 -= 1
    y1 -= 1

    ans = 0

    # horizontal dominos in rectangle
    ans += (
        hor[x2 - 1][y2]
        - hor[x1][y2]
        - hor[x2 - 1][y1]
        + hor[x1][y1]
    )

    # vertical dominos in rectangle
    ans += (
        ver[x2][y2 - 1]
        - ver[x1][y2 - 1]
        - ver[x2][y1]
        + ver[x1][y1]
    )

    print(ans)