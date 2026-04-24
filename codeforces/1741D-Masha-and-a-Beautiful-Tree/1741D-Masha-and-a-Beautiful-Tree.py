def mergeSort(left, right):
        global count

        if left == right:
            return p[left], p[left]

        mid = (left + right) // 2

        left_res = mergeSort(left, mid)

        if left_res is None:
            return None

        right_res = mergeSort(mid + 1, right)
        
        if right_res is None:
            return None

        left_min, left_max = left_res
        right_min, right_max = right_res

        if left_max < right_min:
            return left_min, right_max

        elif right_max < left_min:
            count += 1
            return right_min, left_max

        else:
            return None

    result = mergeSort(0, n - 1)

    if result is None:
        print(-1)
    else:
        print(count)