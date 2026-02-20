class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        sorted_arr = sorted(arr)
        res = []
  
        right = len(arr)

        while right != 1:

            max_num = max(arr[0:right])
            flip = arr.index(max_num) + 1

            if flip == right:
                right -= 1
                continue

            if flip == 1:
                arr[0:right] = arr[0:right][::-1]
                res.append(right)
                right -= 1
                continue

            arr[0:flip] = arr[0:flip][::-1]
            arr[0:right] = arr[0:right][::-1]

            res.extend([flip,right])

            right -= 1

        return res

